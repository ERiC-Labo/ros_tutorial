#pragma once
#include <plugin_first/yes_base.h>
#include <ros/ros.h>

namespace yes_sum
{
    class sum_nikaidou : public yes_base::nikaidou
    {
    public:
        sum_nikaidou();
        many_message::array operate();
    };
}

namespace yes_average
{
    class average_nikaidou : public yes_base::nikaidou
    {
    public:
        average_nikaidou(){}
        many_message::array operate();
    };
}

namespace yes_max
{
    class max_nikaidou : public yes_base::nikaidou
    {
    public:
        max_nikaidou(){}
        many_message::array operate();
    };
}

namespace yes_min
{
    class min_nikaidou : public yes_base::nikaidou
    {
    public:
        min_nikaidou(){}
        many_message::array operate();
    };
}