#include <plugin_first/yes_sum.h>

namespace yes_sum
{
    sum_nikaidou::sum_nikaidou(){}

    many_message::array sum_nikaidou::operate()
    {
        if (array_.size() <= 0)
        {
            ROS_ERROR("Array is empty");
            many_message::array error;
            error.detail = -1;
            error.fwat = -1;
            return error;    
        }
        many_message::array sum;
        sum.fwat = 0;
        sum.detail = 0;
        for (std::vector<many_message::array>::iterator it = array_.begin(); it != array_.end(); ++it)
        {
            sum.fwat += it->fwat;
            sum.detail += it->detail;
        }
        return sum;
        
    }
}

namespace yes_average
{
    many_message::array average_nikaidou::operate()
    {
        if (array_.size() <= 0)
        {
            ROS_ERROR("Array is empty");
            many_message::array error;
            error.detail = -1;
            error.fwat = -1;
            return error;    
        }
        many_message::array average;
        average.detail = 0;
        average.fwat = 0;
        for (std::vector<many_message::array>::iterator it = array_.begin(); it != array_.end(); ++it)
        {
            average.detail += it->detail;
            average.fwat += it->fwat;
        }
        average.detail = average.detail / array_.size();
        average.fwat = (int)(average.fwat / array_.size());
        return average;
    }
}

namespace yes_max
{
    many_message::array max_nikaidou::operate()
    {
        if (array_.size() <= 0)
        {
            ROS_ERROR("Array is empty");
            many_message::array error;
            error.detail = -1;
            error.fwat = -1;
            return error;        }
        many_message::array max = array_[0];
        for (std::vector<many_message::array>::iterator it = array_.begin(); it != array_.end(); ++it)
        {
            if (max.detail < it->detail)
            {
                max = *it;
            }
        }
        return max;
    }
}

namespace yes_min
{
    many_message::array min_nikaidou::operate()
    {
        if (array_.size() <= 0)
        {
            ROS_ERROR("Array is empty");
            many_message::array error;
            error.detail = -1;
            error.fwat = -1;
            return error;    
        }
        many_message::array min = array_[0];
        for (std::vector<many_message::array>::iterator it = array_.begin(); it != array_.end(); ++it)
        {
            if (min.detail > it->detail)
            {
                min = *it;
            }
        }
        return min;
    }
}
PLUGINLIB_EXPORT_CLASS(yes_sum::sum_nikaidou, yes_base::nikaidou)
PLUGINLIB_EXPORT_CLASS(yes_average::average_nikaidou, yes_base::nikaidou)
PLUGINLIB_EXPORT_CLASS(yes_max::max_nikaidou, yes_base::nikaidou)
PLUGINLIB_EXPORT_CLASS(yes_min::min_nikaidou, yes_base::nikaidou)