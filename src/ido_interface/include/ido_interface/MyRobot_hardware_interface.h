#include <hardware_interface/joint_state_interface.h>
#include <hardware_interface/joint_command_interface.h>
#include <hardware_interface/robot_hw.h>
#include <controller_manager/controller_manager.h>
#include <boost/scoped_ptr.hpp>
#include <ros/ros.h>
#include <std_msgs/Float32.h>

class MyRobot : public hardware_interface::RobotHW 
{
    public:
        MyRobot(ros::NodeHandle& nh);
        ~MyRobot();
        void init();
        void update(const ros::TimerEvent& e);
        void read();
        void write(ros::Duration elapsed_time);
        
    protected:
        hardware_interface::JointStateInterface joint_state_interface_;
        hardware_interface::VelocityJointInterface velocity_joint_interface_;
        //hardware_interface::EffortJointInterface effort_joint_interface_;
        //hardware_interface::PositionJointInterface position_joint_interface_;
        
        //joint_limits_interface::JointLimits limits;
        //joint_limits_interface::VelocityJointInterface velocityJointSaturationInterface
        //joint_limits_interface::EffortJointSaturationInterface effortJointSaturationInterface;
        //joint_limits_interface::PositionJointSaturationInterface positionJointSaturationInterface;
        

        double joint_position_[2];
        double joint_velocity_[2];
        double joint_effort_[2];
        double joint_velocity_command_[2];
        //double joint_effort_command_[2];
        //double joint_position_command_;
        double _wheel_vel[2];
        
        ros::Subscriber left_wheel_angle_sub_;
  	ros::Subscriber right_wheel_angle_sub_;
  	ros::Publisher left_wheel_vel_pub_;
  	ros::Publisher right_wheel_vel_pub_;
        
        void leftWheelAngleCallback(const std_msgs::Float32& msg) {
    		_wheel_vel[0] = msg.data;
  	}

  	void rightWheelAngleCallback(const std_msgs::Float32& msg) {
    		_wheel_vel[1] = msg.data;
  	}
        
        ros::NodeHandle nh_;
        ros::Timer my_control_loop_;
        ros::Duration elapsed_time_;
        double loop_hz_;
        boost::shared_ptr<controller_manager::ControllerManager> controller_manager_;
};
