#include <cstdio>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <vector>
#include <string>
#include "bh_msgs/srv/sample_map.hpp"

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  auto node = std::make_shared<rclcpp::Node>("map_node");

  std::vector<std::vector<char>> map;

  auto map_sub = node->create_subscription<std_msgs::msg::String>("/map", 10, [node, &map](std_msgs::msg::String::SharedPtr msg) {
    // RCLCPP_INFO(node->get_logger(), msg->data.c_str());
    map.clear();
    map.push_back({});
    for (auto letter : msg->data) {
      if (letter == '\n') {
        map.push_back({});
      } else {
        map.at(map.size()-1).push_back(letter);
      }
    }
  });

  auto map_srv = node->create_service<bh_msgs::srv::SampleMap>("/sample_map", [&map](bh_msgs::srv::SampleMap::Request::SharedPtr req,
                                                                                    bh_msgs::srv::SampleMap::Response::SharedPtr res) {
    if (req->row >= 0 && req->row < (long int)map.size() && req->col >= 0 && map.size() > 0 && req->col < map.at(0).at(req->col)) {
      res->value = map.at(req->row).at(req->col);
    } else {
      res->value = "outside";
    }
    return res;
  });

  rclcpp::spin(node);

  rclcpp::shutdown();

  return 0;
}
