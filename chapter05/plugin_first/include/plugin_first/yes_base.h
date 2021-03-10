#pragma once

#include <vector>
#include <many_message/array.h>
#include <pluginlib/class_list_macros.h>
#include <ros/ros.h>


namespace yes_base
{
    class nikaidou
    {
    public:
        nikaidou(){}
        virtual ~nikaidou(){}
        virtual many_message::array operate() = 0;
        void setArray(const std::vector<many_message::array> &array);
        std::vector<many_message::array> array_;
    };
}