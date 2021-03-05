#include <plugin_first/yes_base.h>


namespace yes_base
{
    void nikaidou::setArray(const std::vector<many_message::array> &array)
    {
        if (array.size() <= 0)
        {
            ROS_ERROR("input array is empty");
            return;
        }
        if (array_.size() > 0)
            array_.clear();
        array_ = array;
    }
}