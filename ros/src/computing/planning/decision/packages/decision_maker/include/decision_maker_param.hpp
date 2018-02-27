#ifndef __DECISION_MAKER_PARAM_HPP__
#define __DECISION_MAKER_PARAM_HPP__

namespace decision_maker
{
//#define DEBUG_PRINT

#define DEFAULT_DISPLAY_FLAG false
#define DEFAULT_FORCE_STATE_CHANGE true

#define VEL_AVERAGE_COUNT 10
#define DEFAULT_CONVERGENCE_COUNT 5
#define DEFAULT_CONVERGENCE_THRESHOLD 0.01

#define DOUBLE_MAX 1.7976931348623158e308
#define DEFAULT_TARGET_WAYPOINT 14
#define DEFAULT_STR_WAYPOINTS_AHEAD 25

#define DEFAULT_STOP_DECELERATION 0.2
#define DEFAULT_STOP_TIME 1
#define DEFAULT_STOPLINE_TARGET_WAYPOINT 10
#define DEFAULT_STOPLINE_TARGET_RATIO 0.0
#define DEFAULT_STOPLINE_PAUSE_TIME 1.0
#define DEFAULT_SHIFT_WIDTH 1.0
#define DEFAULT_CRAWL_VELOCITY 4.0
#define DEFAULT_DETECTION_AREA_RATE 1.0

#define ANGLE_NEUTRAL 0
#define ANGLE_CURVE 40
#define ANGLE_LEFT (ANGLE_NEUTRAL - ANGLE_CURVE)
#define ANGLE_RIGHT (ANGLE_NEUTRAL + ANGLE_CURVE)

#define TPNAME_BASED_LANE_WAYPOINTS_ARRAY "/based/lane_waypoints_array"
#define TPNAME_CONTROL_LANE_WAYPOINTS_ARRAY "/lane_waypoints_array"
#define LAMP_EMPTY 0
#define LAMP_LEFT 1
#define LAMP_RIGHT 2
#define LAMP_HAZARD 3
#define LAMP_ON 1
#define LAMP_OFF 0

#define DEFAULT_DETECTION_AREA_X1 80.0
#define DEFAULT_DETECTION_AREA_X2 0.0
#define DEFAULT_DETECTION_AREA_Y1 50.0
#define DEFAULT_DETECTION_AREA_Y2 -50.0
}

#endif
