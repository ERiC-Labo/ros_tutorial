#include <client_yes_plugin/yes_client.h>

int main(int argc, char** argv)
{
    try {
        ros::init(argc, argv, "yes_node");
        ros::NodeHandle n;
        ros::Rate loop(1);
        int loop_cout = 0;
        while (ros::ok())
        {
            ROS_INFO_STREAM("Loop cout: " << ++loop_cout);
            yes_client::Ganbare_nikaidou ganbare;
            ganbare.run();
            ros::spinOnce();
            loop.sleep();
        }
    }
    catch (pluginlib::PluginlibException& ex)
    {
        ROS_ERROR_STREAM("The plugin failed" << ex.what());
    }
    return 0;
    
}