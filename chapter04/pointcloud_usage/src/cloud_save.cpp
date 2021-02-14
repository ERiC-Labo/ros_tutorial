#include <pointcloud_usage/create_cloud.h>
#include <pointcloud_usage/child_cloud.h>

static int cout = 0;
void point_callback(const sensor_msgs::PointCloud2ConstPtr &cloud_msg)
{
    pcl::PointCloud<pcl::PointXYZ> cloud;
    pcl::fromROSMsg(*cloud_msg, cloud);
    PointCloud_class::save_pcd(cloud, "/home/tsuchidashinya/yes_1.pcd");
    cout++;
    std::cout << cout << std::endl;

}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "niit");
    ros::NodeHandle pnh("~");
    std::string topic_name = "/photoneo_center/sensor/points";
    std::string save_name = "/home/tsuchidashinya/yes_1.pcd";
    pnh.getParam("topic_name", topic_name);
    pnh.getParam("save_name", save_name);
    //pcl::PointCloud<pcl::PointXYZI> pointcloud;
   // sensor_msgs::PointCloud2 tr = Point_and_ROS::get_topic_message_1(topic_name);
   ros::Subscriber sub;
   ros::NodeHandle nh;
   sub = nh.subscribe(topic_name, 1, point_callback);
   int count = 0;
   ros::Rate loop_rate(10);
   while (count++ <= 20)
   {
       std::cout << topic_name << std::endl;
       ros::spinOnce();
       loop_rate.sleep();
   }
    //PointCloud_class::save_pcd(pointcloud, save_name);
    return 0;
}