/*
自分から認識した物体の種類と位置情報をデータベースに送信する

簡単な仕様：
１、pedestrian_pos_xyzとcar_pos_xyzから画面上のxy座標とdistanceを取得する
２、取得したxyとdistanceから上から見たxy座標を求める
３、このxy座標はカメラから見た座標なのでvelodyneからみ見た座標に変換する
４、これでvelodyneから座標が得られるのでこれを東西南北を軸とする直交座標に変換する
５、直交座標を緯度・経度に変換する
６、データベースサーバに対して1秒ごとに送信する

送信データのフォーマットは
緯度、経度、物体の種類、自動車のid

データは認識した物体ごとに送る

*/


#include "std_msgs/String.h"
#include "ros/ros.h"
#include "CarPositionXYZ.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <pthread.h>
#include <vector>
#include <boost/array.hpp>
#include <iostream>
#include <string>
#include <sstream>
#include "opencv/cv.h" 
#include "opencv/highgui.h" 
#include "opencv/cxcore.h" 
#include "std_msgs/Float64.h"
#include "scan_to_image/ScanImage.h"
#include "geometry_msgs/TwistStamped.h"
#include "sensor_msgs/NavSatFix.h"
#include "structure.h"
#include "SendData.h"
#include "calcoordinates.h"
#include "axialMove.h"
#include "geo_pos_conv.hh"

using namespace std;


/*
  our rectangular plane is 7 in Japan.
*/
const double LAT_PLANE = 36;//136.906565;
const double LON_PLANE = 137.1;//35.180188;



typedef struct _CARPOS{
  int x1;
  int y1;
  int x2;
  int y2;
  float distance;
}CARPOS;

pthread_mutex_t mutex;
pthread_mutex_t pos_mutex;

selfLocation sl;
vector<CARPOS> global_cp_vector;

const char serverName[100] = "db1.ertl.jp";
string dbres;
SendData sd;

LOCATION my_loc;
ANGLE angle;

double cameraMatrix[4][4] = {
  {-7.8577658642752374e-03, -6.2035361880992401e-02,9.9804301981022692e-01, 5.1542126095196206e-01},
  {-9.9821250329813849e-01, 5.9620033356180935e-02,-4.1532977104442731e-03, -2.9214878315161133e-02},
  {-5.9245706805522491e-02, -9.9629165684497312e-01,-6.2392954139163306e-02, -6.6728858508628075e-01},
  {0, 0, 0, 1}
 
};


void printDiff(struct timeval begin, struct timeval end){
  long diff;
  diff = (end.tv_sec - begin.tv_sec)*1000*1000 + (end.tv_usec - begin.tv_usec);
  printf("Diff: %ld us (%ld ms)\n",diff,diff/1000);
}

//wrap SendData class
void* wrapSender(void *tsd){
  
  //get values from sample_corner_point , convert latitude and longitude,
  //and send database server.
  vector<CARPOS> car_position_vector(global_cp_vector.size());
  vector<CARPOS>::iterator cp_iterator;
  string value = "";
  ostringstream oss;

  char magic[5] = "MPWC";
  short major = 1;
  short minor = 0;
  int sql_num = global_cp_vector.size();
  char header[12];
  memcpy(header,magic,4);
  memcpy(&header[4],&major,2);
  memcpy(&header[6],&minor,2);
  memcpy(&header[8],&sql_num,4);
  //value.append(header,12);

  //thread safe process for vector

  pthread_mutex_lock( &mutex );
  std::copy(global_cp_vector.begin(), global_cp_vector.end(), car_position_vector.begin());
  global_cp_vector.clear();
  pthread_mutex_unlock( &mutex );
  cp_iterator = car_position_vector.begin();

  pthread_mutex_lock( &pos_mutex );
  double my_xloc = my_loc.X;
  double my_yloc = my_loc.Y;
  double my_zloc = my_loc.Z;
  pthread_mutex_unlock( &pos_mutex );

  while(cp_iterator != car_position_vector.end()){

    //middle of right-lower and left-upper
    double U = (cp_iterator->x1 + cp_iterator->x2)/2;
    double V = (cp_iterator->y1 + cp_iterator->y2)/2;


    //convert
    sl.setOriginalValue(U,V,cp_iterator->distance);
    LOCATION ress = sl.cal();

    axiMove am;
    //convert axes from camera to velodyne
    LOCATION velocoordinate = am.cal(ress,cameraMatrix);

    //convert axes to north direction 0 angle.
    LOCATION anglefixed = am.cal(velocoordinate,angle);


    /*
      rectangular coordinate is that axial x is the direction to left and right,
      axial y is the direction to front and backend and axial z is the direction to upper and lower.
      So convert them.
     */
    LOCATION rescoord;
    rescoord.X = anglefixed.X;
    rescoord.Y = anglefixed.Z;
    rescoord.Z = anglefixed.Y;

    /*
      I got my GPS location too.it`s my_xloc,my_yloc.
      and I convert to plane rectangular coordinate  from latitude and longitude.
     */

    //sample Longitude and Latitude 3513.1345669,N,13658.9971525,E

    geo_pos_conv geo;
    geo.set_plane(7);
    geo.set_llh_nmea_degrees(my_xloc,my_yloc,my_zloc);

    printf("X,Y,Z = %f,%f,%f\n",rescoord.X,rescoord.Y,rescoord.Z);

    //add plane rectangular coordinate to that of target car.
    rescoord.X += geo.x();
    rescoord.Y += geo.y();
    rescoord.Z += 0;

    printf("geo : %f\t%f\n",rescoord.X,rescoord.Y);


    //covert plane rectangular coordinate to latitude and longitude.
    calcoordinates cc;
    RESULT res = cc.cal(rescoord.X,rescoord.Z,LAT_PLANE,LON_PLANE);

    printf("object position : lat:%f\tlon:%f\n",res.lat,res.lon);

    //I assume that values has 4 value ex: "0 0 0 0"   "1 2 3 4"
    //And if setting the other number of value , sendData will be failed.

    //    oss << "\"INSERT INTO POS(id,x,y,area,type,self) ";
    //oss << "values(0," << rescoord.X << "," << rescoord.Y << ",0,0,1" << ");\"";

    oss << "0 " << rescoord.X << " " << rescoord.Y << " 0,";

    cp_iterator++;
  
  }

  oss << "<E>";

  value += oss.str();
  //  printf("%s\n",value.c_str());
  //  printf("%d\n",value.size());
  

  sd.setValue(value);
  sd.Sender();

}


void* intervalCall(void *a){

  pthread_t th;

  while(1){
    if(global_cp_vector.size()<=0) continue;
    //create new thread for socket communication.      
    if(pthread_create(&th, NULL, wrapSender, NULL)){
      printf("thread create error\n");
    }
    sleep(1);
    if(pthread_join(th,NULL)){
      printf("thread join error.\n");
    }
  }
}

void car_position_xyzCallback(const sensors_fusion::CarPositionXYZ& car_position_xyz)
{
  int i;
  CARPOS cp;

  pthread_mutex_lock( &mutex );

  //認識した車の数だけ繰り返す
  for (i = 0; i < car_position_xyz.car_num; i++){
    cp.x1 = car_position_xyz.corner_point.at(0+i*4);//x-axis of the upper left
    cp.y1 = car_position_xyz.corner_point.at(1+i*4);//y-axis of the upper left
    cp.x2 = car_position_xyz.corner_point.at(2+i*4);//x-axis of the lower right
    cp.y2 = car_position_xyz.corner_point.at(3+i*4);//y-axis of the lower right
    cp.distance = car_position_xyz.distance.at(i);

    printf("%d,%d,%d,%d\n",cp.x1,cp.y1,cp.x2,cp.y2);

    global_cp_vector.push_back(cp);
      
  }
  pthread_mutex_unlock( &mutex );

  printf("car position get\n\n");

}

void azimuth_getter(const geometry_msgs::TwistStamped& azi)
{

  angle.thiX = 0;
  angle.thiY = azi.twist.angular.z*180/M_PI;
  angle.thiZ = 0;
  printf("azimuth : %f\n",angle.thiY);
  //printf("ok\n");

}

void position_getter(const sensor_msgs::NavSatFix& pos)
{

  pthread_mutex_lock( &pos_mutex );
  my_loc.X = pos.latitude;
  my_loc.Y = pos.longitude;
  my_loc.Z = 0;
  pthread_mutex_unlock( &pos_mutex );
  
  //printf("my position : %f %f %f\n",my_loc.X,my_loc.Y,my_loc.Z);

}


//test
void set_car_position_xyz()
{
  int i;
  CARPOS cp;

  pthread_mutex_lock( &mutex );

  global_cp_vector.clear();

  //認識した車の数だけ繰り返す
  //    for (i = 0; i < car_position_xyz.car_num; i++){
  for (i = 0; i < 3; i++){
    //各認識した車へのデータのアクセス例
    cp.x1 = 10*i;
    cp.y1 = 20*i;
    cp.x2 = 30*i;
    cp.y2 = 40*i;
    cp.distance = 20;
    global_cp_vector.push_back(cp);
      
  }
  pthread_mutex_unlock( &mutex );
  printf("ok\n");

}


int main(int argc, char **argv){
  
  ros::init(argc ,argv, "obj_uploader") ;  
  cout << "obj_uploader" << endl;

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  //car_pos_xyzトピックが更新されるとcar_position_xyzCallback関数が呼ばれる
  //第二引数の100は受信側のバッファであり、最新の100個を保持している。自由に変更可能です。
  //100個以上になると古いものから欠損します
  ros::Subscriber car_pos = n.subscribe("car_pos_xyz", 10, car_position_xyzCallback);
  ros::Subscriber azm = n.subscribe("vel", 10, azimuth_getter);
  ros::Subscriber my_pos = n.subscribe("fix", 10, position_getter);

  /*
  cv::Mat intrinsic;
  std::string camera_yaml; 
  n.param<std::string>("/scan_to_image/camera_yaml", camera_yaml,"scan_to_image/camera.yaml"); 
  cv::FileStorage fs_auto_file(camera_yaml.c_str(), cv::FileStorage::READ); 
  if(!fs_auto_file.isOpened()){
    fprintf(stderr,"%s, : cannot open file\n",camera_yaml.c_str());
    exit(EXIT_FAILURE);
  }
  fs_auto_file["intrinsic"] >> intrinsic; 
  fs_auto_file.release(); 
  */

  /*
  double fkx = intrinsic.at<float>(0,0);  
  double fky = intrinsic.at<float>(1,1); 
  double Ox = intrinsic.at<float>(0,2);
  double Oy = intrinsic.at<float>(1,2); 
  */

  double fkx = 7.97983032e+02;
  double fky = 3.74826355e+02;
  double Ox =  7.97696411e+02;
  double Oy = 2.54657837e+02;


  sl.setCameraParam(fkx,fky,Ox,Oy);

  //set_car_position_xyz();

  sd = SendData(const_cast<char*>(serverName),5777);

  my_loc.X = 3513.1345669;
  my_loc.Y = 13658.9971525;
  my_loc.Z = 0;

  pthread_t th;
  if(pthread_create(&th, NULL, intervalCall, NULL)){
    printf("thread create error\n");
  }

  pthread_detach(th);

  ros::spin();

}
