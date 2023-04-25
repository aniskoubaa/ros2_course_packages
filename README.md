# ROS2 for Beginners: Udemy Course Packages

Welcome to the **ROS2 for Beginners** Udemy course Git repository. This repository contains the packages and materials designed to help you learn essential ROS2 concepts and gain hands-on experience in both C++ and Python languages.

## Course Packages

The repository contains the following packages:

* `ros2_essential_cpp`: Covers essential ROS2 concepts and examples using the C++ language.
* `ros2_essential_python`: Explores essential ROS2 concepts and examples using the Python language.
* `ros2_interfaces_cpp`: Provides tutorials on defining and using custom ROS2 interfaces with the C++ language.
* `ros2_motion_cpp`: Offers tutorials on robot motion control using ROS2 and the C++ language.
* `ros2_motion_python`: Presents tutorials on robot motion control using ROS2 and the Python language.
* `ros2_laser_python`: Includes tutorials on working with laser scanners in ROS2 using Python.

## Getting Started

Before using these packages, ensure that ROS2 is installed on your system. Follow the [ROS2 installation guide](https://index.ros.org/doc/ros2/Installation/) for detailed instructions on how to install ROS2.

To set up the course packages on your local machine, follow the steps below:

1. Clone this Git repository into the `src` directory of your ROS2 workspace:

   ```bash
   cd ~/ros2_ws/src
   git clone https://github.com/riotu-lab/ros2_course_packages.git

2. Move the content of the ros2_course_packages folder to the src directory:
  ```bash
  cd ~/ros2_ws/
  mv src/ros2_course_packages/* src/
