#pragma once

#include <plugin_first/yes_base.h>
#include <boost/shared_ptr.hpp>
#include <pluginlib/class_loader.h>

namespace yes_client
{
    const float ARRAY[] = {2.5, 5.4, 4.6, 2.6, 1.5};
    const int array_size = 5;
    const std::string PLUGIN_NAME[] = {
        "plugin_first/yes_sum", "plugin_first/yes_average",
        "plugin_first/yes_max", "plugin_first/yes_min"
    };
    const int plugin_size = 4;
    class Ganbare_nikaidou
    {
        typedef boost::shared_ptr<yes_base::nikaidou> LoadPtr;
    public:
        Ganbare_nikaidou() :
            yes_loader_("plugin_first", "yes_base::nikaidou")
        {
            for (int i = 0; i < array_size; i++) {
                many_message::array message;
                message.detail = ARRAY[i];
                message.fwat = (int)ARRAY[i];
                array_.push_back(message);
            }
            
        }
        void run();
    private:
        void loadAllPlugins();
        void operateAllPlugins();
        std::vector<many_message::array> array_;
        pluginlib::ClassLoader<yes_base::nikaidou> yes_loader_;
        std::vector<LoadPtr> pluglin_instances_;
    };
}