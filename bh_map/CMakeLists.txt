cmake_minimum_required(VERSION 3.8)
project(bh_map)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(bh_msgs REQUIRED)

add_executable(map_node src/map_node.cpp)
ament_target_dependencies(map_node rclcpp std_msgs bh_msgs)

# find_package(rosidl_default_generators REQUIRED)

# rosidl_generate_interfaces(${PROJECT_NAME}
#   "srv/SampleMap.srv"
# )

# ament_export_dependencies(rosidl_default_runtime)

# # Only needed when using message in same package
# # https://docs.ros.org/en/foxy/Tutorials/Single-Package-Define-And-Use-Interface.html
# rosidl_target_interfaces(map_node
#   ${PROJECT_NAME} "rosidl_typesupport_cpp")

target_include_directories(map_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(map_node PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17

install(TARGETS map_node
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # uncomment the line when a copyright and license is not present in all source files
  #set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # uncomment the line when this package is not in a git repo
  #set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
