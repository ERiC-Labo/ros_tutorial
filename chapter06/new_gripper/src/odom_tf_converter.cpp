#include <ros/ros.h>
#include <nav_msgs/Odometry.h>
#include <tf/transform_broadcaster.h>
#include <string>
#include <math.h>

class Converter
{
public:
    Converter(void)
    {
        pnh = ros::NodeHandle("~");
        joy_sub_ = nh_.subscribe("/tracker", 10, &Converter::odomCallback, this);
    }
    void odomCallback(const nav_msgs::Odometry& msg)
    {
        tf::Transform transform;
        std::string odom_name = "odom";
        pnh.getParam("odom", odom_name);
        tf::poseMsgToTF(msg.pose.pose, transform);
        br_.sendTransform(tf::StampedTransform(transform, msg.header.stamp, odom_name,
        msg.child_frame_id));
        
    }
    
    
private:
    ros::NodeHandle nh_;
    ros::NodeHandle pnh;
    ros::Subscriber joy_sub_;
    ros::Subscriber joy_sub_1;
    tf::TransformBroadcaster br_;
    tf::TransformBroadcaster br_1;
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "odom_tf");
    Converter converter;
    ros::spin();
    return 0;
}