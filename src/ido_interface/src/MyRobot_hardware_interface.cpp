#include <ido_interface/MyRobot_hardware_interface.h>

MyRobot::MyRobot(ros::NodeHandle& nh) : nh_(nh) {


// Declare all JointHandles, JointInterfaces and JointLimitInterfaces of the robot.
    init();
    
// Create the controller manager
    controller_manager_.reset(new controller_manager::ControllerManager(this, nh_));
    
//Set the frequency of the control loop.
    loop_hz_=10;
    ros::Duration update_freq = ros::Duration(1.0/loop_hz_);
   
//Run the control loop
    my_control_loop_ = nh_.createTimer(update_freq, &MyRobot::update, this);
    
    
}


MyRobot::~MyRobot() {
}

void MyRobot::init() {
        
// Create joint_state_interface for JointA (left wheel)
    hardware_interface::JointStateHandle jointStateHandleA("wheel_left_joint", &joint_position_[0], &joint_velocity_[0], &joint_effort_[0]);
    joint_state_interface_.registerHandle(jointStateHandleA);
// Create effort joint interface as JointA accepts effort command.
    hardware_interface::JointHandle jointVelocityHandleA(jointStateHandleA, &joint_velocity_command_[0]);
    velocity_joint_interface_.registerHandle(jointVelocityHandleA);    

   
// Create joint_state_interface for JointB (right wheel)
    hardware_interface::JointStateHandle jointStateHandleB("wheel_right_joint", &joint_position_[1], &joint_velocity_[1], &joint_effort_[1]);
    joint_state_interface_.registerHandle(jointStateHandleB);
// Create effort joint interface as JointB accepts effort command.
    hardware_interface::JointHandle jointVelocityHandleB(jointStateHandleB, &joint_velocity_command_[1]);
    velocity_joint_interface_.registerHandle(jointVelocityHandleB); 



// Register all joints interfaces    
    registerInterface(&joint_state_interface_);
    registerInterface(&velocity_joint_interface_);  
    
    // Advertise the publishers
    left_wheel_vel_pub_ = nh_.advertise<std_msgs::Float32>("my_robot/left_wheel_vel", 1);
    right_wheel_vel_pub_ = nh_.advertise<std_msgs::Float32>("my_robot/right_wheel_vel", 1); 
    
    // Subscribe to the required topics
    left_wheel_angle_sub_ = nh_.subscribe("my_robot/left_wheel_angle", 1, &MyRobot::leftWheelAngleCallback, this);
    right_wheel_angle_sub_ = nh_.subscribe("my_robot/right_wheel_angle", 1, &MyRobot::rightWheelAngleCallback, this);
}


//This is the control loop
void MyRobot::update(const ros::TimerEvent& e) {
    elapsed_time_ = ros::Duration(e.current_real - e.last_real);
    read();
    controller_manager_->update(ros::Time::now(), elapsed_time_);
    write(elapsed_time_);
}

// This function gets called to input data into the controller
void MyRobot::read() {

  joint_position_[0] = _wheel_vel[0];
  joint_position_[1] = _wheel_vel[1];

}

// This function gets called to output data from the controller
void MyRobot::write(ros::Duration elapsed_time)
{
	//Create a new message and fill it with the data, then publish it 
	std_msgs::Float32 left_wheel_vel_msg;
	std_msgs::Float32 right_wheel_vel_msg;
	left_wheel_vel_msg.data = joint_velocity_command_[0];
	right_wheel_vel_msg.data = joint_velocity_command_[1];
	left_wheel_vel_pub_.publish(left_wheel_vel_msg);
	right_wheel_vel_pub_.publish(right_wheel_vel_msg);

}


int main(int argc, char** argv)
{
	
    //Initialze the ROS node.
    ros::init(argc, argv, "MyRobot_hardware_interface_node");
    ros::NodeHandle nh;
    
    // Create the object of the robot hardware_interface class and spin the thread. 
    MyRobot ROBOT(nh);
    
    //Separate Spinner thread for the Non-Real time callbacks such as service callbacks to load controllers
    ros::MultiThreadedSpinner spinner(0); 
    spinner.spin();
    
    return 0;
}
