/*
 * Copyright 2015-2019 Autoware Foundation. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef NDT_SLAM_CORE_H
#define NDT_SLAM_CORE_H

#include <array>
#include <deque>
#include <memory>
#include <string>

#include <ros/ros.h>

#include <message_filters/subscriber.h>
#include <message_filters/sync_policies/approximate_time.h>
#include <message_filters/synchronizer.h>

#include <tf/tf.h>
#include <tf/transform_broadcaster.h>
#include <tf/transform_datatypes.h>
#include <tf/transform_listener.h>

#include <tf2/transform_datatypes.h>
#include <tf2_ros/transform_listener.h>
#include <tf2_sensor_msgs/tf2_sensor_msgs.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>


#include <autoware_config_msgs/ConfigNDTSlam.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <geometry_msgs/TwistStamped.h>
#include <nav_msgs/Odometry.h>
#include <sensor_msgs/PointCloud2.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Float64.h>

#include <lidar_localizer/map_manager/map_manager.h>
#include <lidar_localizer/matching_score/matching_score.h>
#include <lidar_localizer/matching_score/matching_score_histogram.h>
#include <lidar_localizer/ndt/ndt_slam_pcl.h>
#include <lidar_localizer/ndt/ndt_slam_pcl_anh.h>
#include <lidar_localizer/ndt/ndt_slam_pcl_anh_gpu.h>
#include <lidar_localizer/ndt/ndt_slam_pcl_omp.h>
#include <lidar_localizer/pose_linear_interpolator/pose_linear_interpolator.h>

class NdtSlam {
  using PointSource = pcl::PointXYZI;
  using PointTarget = pcl::PointXYZI;
  using SyncPolicyPoints =
      message_filters::sync_policies::ApproximateTime<sensor_msgs::PointCloud2,
                                                      sensor_msgs::PointCloud2>;

  using SyncPolicyPointsAndPose =
      message_filters::sync_policies::ApproximateTime<sensor_msgs::PointCloud2,
                                                      sensor_msgs::PointCloud2,
                                                      geometry_msgs::PoseStamped>;

  enum class MethodType {
    PCL_GENERIC = 0,
    PCL_ANH = 1,
    PCL_ANH_GPU = 2,
    PCL_OPENMP = 3,
  };

public:
  NdtSlam(ros::NodeHandle nh, ros::NodeHandle private_nh);
  ~NdtSlam();

private:
  void configCallback(const autoware_config_msgs::ConfigNDTSlam::ConstPtr &config_msg_ptr);
  void pointsMapUpdatedCallback(const sensor_msgs::PointCloud2::ConstPtr &pointcloud2_msg_ptr);
  void initialPoseCallback(const geometry_msgs::PoseWithCovarianceStamped::ConstPtr &pose_conv_msg_ptr);
  void mappingAndLocalizingPointsCallback(
      const sensor_msgs::PointCloud2::ConstPtr &mapping_points_msg_ptr,
      const sensor_msgs::PointCloud2::ConstPtr &localizing_points_msg_ptr);

  void mappingAndLocalizingPointsAndCurrentPoseCallback(
      const sensor_msgs::PointCloud2::ConstPtr &mapping_points_msg_ptr,
      const sensor_msgs::PointCloud2::ConstPtr &localizing_points_msg_ptr,
      const geometry_msgs::PoseStamped::ConstPtr &current_pose_msg_ptr);

  Pose getPredictPose();
  void mapping(const boost::shared_ptr<pcl::PointCloud<PointTarget>> &mapping_points_ptr, const Pose &sensor_pose);
  void processMatchingScore(const boost::shared_ptr<pcl::PointCloud<PointTarget>> &points_ptr);
  void updateMatchingScore(const boost::shared_ptr<pcl::PointCloud<PointTarget>> &points_ptr);
  void getMatchAndUnmatchPoints(const boost::shared_ptr<pcl::PointCloud<PointTarget>> &match_points_ptr,
                                const boost::shared_ptr<pcl::PointCloud<PointTarget>> &unmatch_points_ptr);
  std::array<double, 32> createCovariance(const double score);
  void estimateVelocity(const Pose &pose);
  Velocity transformBaseLinkTFVelocity(const Velocity& velocity, const bool is_move_forward);

  void publish(const ros::Publisher &publisher, const double value);
  void publish(const ros::Publisher &publisher, const std::string frame_id, const Pose &pose);
  void publish(const ros::Publisher &publisher, const std::string frame_id, const Pose &pose, const std::array<double, 32> cov);
  void publish(const ros::Publisher &publisher, const std::string frame_id, const Velocity &velocity);
  void publish(const ros::Publisher &publisher, const std::string frame_id, const std::vector<HistogramWithRangeBin> &histogram_bin_array);
  template<class PointType>
  void publish(const ros::Publisher &publisher, const std::string frame_id, const boost::shared_ptr<pcl::PointCloud<PointType>> &points_ptr);
  void publishTF(const std::string &frame_id, const std::string &child_frame_id, const Pose &pose);

  bool getTransform(const std::string &target_frame, const std::string &source_frame, const geometry_msgs::TransformStamped::Ptr &transform_stamped_ptr);

  ros::NodeHandle nh_;
  ros::NodeHandle private_nh_;

  ros::Publisher points_map_pub_;
  ros::Publisher ndt_pose_pub_;
  ros::Publisher predict_pose_pub_;
  ros::Publisher ndt_pose_with_covariance_pub_;
  ros::Publisher sensor_pose_pub_;
  ros::Publisher estimate_twist_pub_;
  ros::Publisher matching_score_pub_;
  ros::Publisher matching_score_histogram_pub_;
  ros::Publisher matching_points_pub_;
  ros::Publisher unmatching_points_pub_;
  ros::Publisher time_ndt_matching_pub_;

  ros::Subscriber config_sub_;
  ros::Subscriber points_map_sub_;
  ros::Subscriber initial_pose_sub_;

  std::unique_ptr<message_filters::Subscriber<sensor_msgs::PointCloud2>> mapping_points_sub_;
  std::unique_ptr<message_filters::Subscriber<sensor_msgs::PointCloud2>> localizing_points_sub_;
  std::unique_ptr<message_filters::Subscriber<geometry_msgs::PoseStamped>> current_pose_sub_;
  std::unique_ptr<message_filters::Synchronizer<SyncPolicyPoints>> points_synchronizer_;
  std::unique_ptr<message_filters::Synchronizer<SyncPolicyPointsAndPose>> points_and_pose_synchronizer_;

  tf::TransformBroadcaster tf_broadcaster_;
  tf::TransformListener tf_listener_;

  tf2_ros::Buffer tf2_buffer_;
  tf2_ros::TransformListener tf2_listener_;

  std::unique_ptr<NdtSlamBase<PointSource, PointTarget>> localizer_ptr_;
  MapManager<PointTarget> map_manager_;
  MatchingScore<PointTarget> matching_score_class_; //TODO
  PoseLinearInterpolator pose_interpolator_;

  MethodType method_type_;
  Eigen::Matrix4f base_link_to_sensor_matrix_;
  Eigen::Matrix4f target_to_map_matrix_;
  Pose base_link_to_sensor_pose_;
  Pose target_to_map_pose_;
  bool with_mapping_;
  bool separate_mapping_;
  bool use_nn_point_z_when_initial_pose_;
  bool publish_tf_;
  std::string sensor_frame_;
  std::string base_link_frame_;
  std::string map_frame_;
  std::string target_frame_;  //TODO rename??
  std::string log_file_directory_path_;
  double min_scan_range_;
  double max_scan_range_;
  double min_add_scan_shift_;
  double matching_score_;

  PoseStamped init_pose_stamped_;
  ros::Time current_scan_time_;
};

#endif
