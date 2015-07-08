/////////////////////////Car tracking project with laser_radar_data_fusion/////////////////////////////////////////
//////////////////////////////////////////////////////////////////////Copyright 2009-10 Akihiro Takeuchi///////////

/////get_boxes_func.h functions about get boundary boxes (to extend get_boxes.cc) /////////////////////////////////

#include <stdio.h>
#include "MODEL_info.h"		//File information

#include "switch_float.h"

#ifndef INCLUDED_GET_BOXES_Functions_
#define INCLUDED_GET_BOXES_Functions_

//fconvsMT.cpp
//convolute filter and feature
FLOAT **fconvsMT(FLOAT*feat,FLOAT*flfeat,FLOAT**filter,int *sym_info,int start,int end,int *A_SIZE,int **B_SIZE,int *M_size);

//dt.h
extern FLOAT *dt(FLOAT *vals,FLOAT ax,FLOAT bx,FLOAT ay,FLOAT by,int *dims,int *Ix,int *Iy);		//decide optimum part position
extern void add_part_calculation(FLOAT *score, FLOAT*M,int *rootsize,int *partsize,int ax,int ay);	//add part score

//hyp_reduction.cpp
extern bool **hyp_reduction(FLOAT **rootmatch,int *RSIZE,int NoC,FLOAT thresh);

#endif
