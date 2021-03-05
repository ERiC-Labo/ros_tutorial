#include <client_yes_plugin/yes_client.h>

namespace yes_client
{
    void Ganbare_nikaidou::loadAllPlugins()
    {
        std::cout << plugin_size << std::endl;
        for (int i = 0; i < plugin_size; ++i)
        {
            //std::cout << "nin1" << std::endl;
            //std::cout << PLUGIN_NAME[i] << std::endl;
            pluglin_instances_.push_back(yes_loader_.createInstance(PLUGIN_NAME[i]));
        }
        for (std::vector<LoadPtr>::iterator it = pluglin_instances_.begin(); it != pluglin_instances_.end(); ++it)
        {
            //std::cout << "nin2" << std::endl;
            (*it)->setArray(array_);
        }
    }

    void Ganbare_nikaidou::operateAllPlugins()
    {
        for (std::vector<LoadPtr>::iterator it = pluglin_instances_.begin();
                it != pluglin_instances_.end(); ++it)
        {
            int index = std::distance(pluglin_instances_.begin(), it);
            many_message::array lin = (*it)->operate();
            ROS_INFO_STREAM(PLUGIN_NAME[index] << " : " << std::fixed << 
                std::setprecision(2) << std::setw(5) << lin.fwat << "  " << lin.detail);
        }
    }
    void Ganbare_nikaidou::run()
    {
        //std::cout << "run1" << std::endl;
        loadAllPlugins();
        //std::cout << "run2" << std::endl;
        operateAllPlugins();
    }
}