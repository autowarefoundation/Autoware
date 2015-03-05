#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <queue>

#include "mainwindow.h"
#include "autoware_socket.h"

HevState _hev_state;

double cycle_time = 0.0;
double estimate_accel = 0.0;
int ndrv = 0;
int nbrk = 0;
double nstr = 0.0;

int pdrv = 0;
int pbrk = 0;
double pstr = 0.0;

std::vector<std::string> split(const std::string& input, char delimiter)
{
  std::istringstream stream(input);
  std::string field;
  std::vector<std::string> result;
  while (std::getline(stream, field, delimiter)) {
    result.push_back(field);
  }
  return result;
}

void Getter(CMDDATA &cmddata)
{
  std::string request;
  std::string cmdRes;
  char recvdata[32];

  struct sockaddr_in server;
  int sock;
  //  char deststr[80] = serverIP.c_str();
  unsigned int **addrptr;

  sock = socket(AF_INET, SOCK_STREAM, 0);
  if (sock < 0) {
    perror("socket");
    return;
  }

  server.sin_family = AF_INET;
  server.sin_port = htons(10001);

  server.sin_addr.s_addr = inet_addr(ros_ip_address.c_str());
  if (server.sin_addr.s_addr == 0xffffffff) {
    struct hostent *host;

    host = gethostbyname(ros_ip_address.c_str());
    if (host == NULL) {
      if (h_errno == HOST_NOT_FOUND) {
        fprintf(stdout,"cmd : ROS PC not found : %s\n", ros_ip_address.c_str());
      } else {
        fprintf(stdout,"cmd : %s : %s\n", hstrerror(h_errno), ros_ip_address.c_str());
      }
      return;
    }

    addrptr = (unsigned int **)host->h_addr_list;

    while (*addrptr != NULL) {
      server.sin_addr.s_addr = *(*addrptr);

      /* break the loop when connected. */
      if (connect(sock, (struct sockaddr *)&server, sizeof(server)) == 0) {
        break;
      }

      addrptr++;
      // let's try another IP address if not successfully connected.
    }
   
    // if all connections failed...
    if (*addrptr == NULL) {
      perror("cmd : connect");
      return;
    }
  } else {
    if (connect(sock,
		(struct sockaddr *)&server, sizeof(server)) != 0) {
      perror("cmd : connect");
      return;
    }
  }
  int n;

  while (true) {
    memset(recvdata, 0, sizeof(recvdata));
    n = recv(sock, recvdata, sizeof(recvdata),0);
    if (n < 0) {
      perror("cmd : read erro");
      return;
    }else if(n == 0){
      break;
    }
    cmdRes.append(recvdata,n);
  }

  // string version
  std::vector<std::string> cmdVector;
  cmdVector = split(cmdRes,',');
  if(cmdVector.size() == 7){
    cmddata.vel.tv = atof(cmdVector[0].c_str());
    cmddata.vel.sv = atof(cmdVector[1].c_str());
    cmddata.mode = atoi(cmdVector[2].c_str());
    cmddata.gear = atoi(cmdVector[3].c_str());
    cmddata.accel = atoi(cmdVector[4].c_str());
    cmddata.steer = atoi(cmdVector[5].c_str());
    cmddata.brake = atoi(cmdVector[6].c_str());
    
    cout << endl << endl;
    cout << "cmddata.vel.tv = " << cmddata.vel.tv << endl;
    cout << "cmddata.vel.sv = " << cmddata.vel.sv << endl;
  } else{
    fprintf(stderr,"cmd : Recv data is invalid\n");
  }
  printf("cmd : return data : %s\n",cmdRes.c_str());

  close(sock);

  return;
}

/*
void CMDGetter(){
  pthread_t _getter;
  while(1){
    if(pthread_create(&_getter, NULL, Getter, NULL)){
      fprintf(stderr,"cmd : pthread create error");
      return;
    }
    pthread_detach(_getter);
    usleep(10*1000);
  }
}
*/

bool Operate(int mode, int gear, int accel, int steer, int brake, void* p) 
{
  static int old_mode = -1;
  static int old_gear = -1;
  MainWindow* main = (MainWindow*)p;

  if (mode != old_mode) {
    main->SetMode(mode);
    old_mode = mode;
  }

  if (gear != old_gear) {
    double current_velocity = _hev_state.drvInf.veloc; // km/h
    // never change the gear when driving!
    if (current_velocity == 0) {
      main->SetGear(gear);
      old_gear = gear;
    }
  }

  return true;
}

bool Control(vel_data_t vel, void* p) 
{
  MainWindow* main = (MainWindow*)p;
  static long long int old_tstamp = 0;

  // update Hev's drvinf/strinf/brkinf.
  main->UpdateState();

  // calculate current time
  cycle_time = (_hev_state.tstamp - old_tstamp) / 1000.0;

  queue<double> vel_buffer;
  static uint vel_buffer_size = 10; 

  double old_velocity = 0.0;

  double current_velocity = _hev_state.drvInf.veloc; // km/h
  double current_steering_angle = _hev_state.strInf.angle; // degree
 
  int cmd_velocity = vel.tv*3.6;
  int cmd_steering_angle;

  // We assume that the slope against the entire arc toward the 
  // next waypoint is almost equal to that against 
  // $l = 2 \pi r \times \frac{\theta}{360} = r \times \theta$
  // \theta = cmd_wheel_angle
  // vel.sv/vel.tv = Radius
  // l \simeq VEHICLE_LENGTH
  if (vel.tv < 1) {// just avoid divided by zero.
    cmd_steering_angle = current_steering_angle;
  }
  else {
    double wheel_angle_pi = (vel.sv/vel.tv) * WHEEL_BASE;// + ANGLE_ERROR;
    double wheel_angle = (wheel_angle_pi / M_PI) * 180.0;
    cmd_steering_angle = wheel_angle * WHEEL_TO_STEERING;
  }

  // estimate current acceleration.
  vel_buffer.push(fabs(current_velocity));
  
  if (vel_buffer.size() > vel_buffer_size) {
    old_velocity = vel_buffer.front();
    vel_buffer.pop();
    estimate_accel = (fabs(current_velocity)-old_velocity)/(cycle_time*vel_buffer_size);
  }

  cout << "Current " << "vel : " << current_velocity << ", str : "<< current_steering_angle << endl; 
  cout << "Command " << "vel : " << cmd_velocity << ", str : "<< cmd_steering_angle << endl; 
  cout << "Estimate Accel : " << estimate_accel << endl; 

  // TRY TO INCREASE STEERING
  //  sv +=0.1*sv;

  // if tv non zero then check if in drive gear first
  //--------------------------------------------------------------
  // if in neutral and get +'ve cmd vel
  //    - put brake on
  //    - change shift to drive
  // if in neutral and vel cmd 0
  //    - release brake if pressed
  
  //------------------------------------------------------
  // if shift in drive
  //     - if cmd vel > 0 && brake pressed
  //              - release brake
  //     - if cmd vel == 0
  //              - if cur_vel < 0.1, nearly stopped
  //                     - full brake too stop, wait, and shift to neutral
  //              - else - brake to HEV_MED_BRAKE
  //                       - decellerate until nearly stopped
  // now motion if in drift mode and shift is in drive
  
 
  //////////////////////////////////////////////////////
  // Accel and Brake
  //////////////////////////////////////////////////////
  if (fabs(cmd_velocity) >= fabs(current_velocity) 
      && fabs(cmd_velocity) > 0.0 
      && fabs(current_velocity) <= KmhToMs(SPEED_LIMIT) ) {
    //accelerate !!!!!!!!!!!!!!!!
    cout << "Acceleration" << endl;
    main->AccelerateControl(current_velocity, cmd_velocity);
  } else if (fabs(cmd_velocity) < fabs(current_velocity) 
             && fabs(cmd_velocity) > 0.0) {
    //decelerate!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    cout << "Deceleration" << endl;
    main->DecelerateControl(current_velocity, cmd_velocity);
  }
  else if (cmd_velocity == 0.0 && fabs(current_velocity) != 0) {
    //Stopping!!!!!!!!!!!
    cout << "Stopping" << endl;
    main->StoppingControl(current_velocity, cmd_velocity);
  }
    
  //////////////////////////////////////////////////////
  // Steering
  //////////////////////////////////////////////////////
  main->SteeringControl(current_steering_angle, cmd_steering_angle);

  // save the time stamp.
  old_tstamp = _hev_state.tstamp;

  return true;
  
}

void MainWindow::TestPrint(){
#ifdef DEBUG
  printf("test print,%d,%d,%d,%d,%f,%f,(Str is a 10x value)\n",ndrv,ndrv-pdrv,nbrk,nbrk-pbrk,nstr,nstr-pstr);
#endif
}

void initPrintValue(){
  pdrv = ndrv;  
  pbrk = nbrk;
  pstr = nstr;

  ndrv = 0;  
  nbrk = 0;
  nstr = 0;

}


void *MainWindow::CMDGetterEntry(void *a)
{
  MainWindow* main = (MainWindow*)a;
  CMDDATA cmddata;
  cout << "test print,accel,diff previous accel,brake,diff previous brake,str,diff previous str,(Str is a 10x value)" << endl;
  while(1){
    Getter(cmddata); // get commands from ROS.
    Operate(cmddata.mode, cmddata.gear, cmddata.accel, cmddata.steer, cmddata.brake, main);
    Control(cmddata.vel, main);
    main->TestPrint();
    initPrintValue();
    
    usleep(cmd_rx_interval*1000);
  }
  return NULL;
}
