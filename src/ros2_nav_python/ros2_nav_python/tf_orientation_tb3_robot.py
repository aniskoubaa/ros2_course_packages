#!/usr/bin/env python3

"""
This is a simple program that subscribes to the odom topic and gets the
position and orientation of the robot.
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time
#import tf.transformations as tf_trans


class OdomPose(Node):
    def __init__(self):
        super().__init__('odom_pose_node')

        # Subscribe to the odom topic
        self.pose_subscriber = self.create_subscription(
            Odometry, '/odom', self.odom_pose_callback, 10)

    def odom_pose_callback(self, odom_msg: Odometry):
        """
        Callback function for the odom pose (position + orientation) of the robot.
        """
        self.get_logger().info("Odom pose callback")

        # Get the position of the robot
        position_x = odom_msg.pose.pose.position.x
        position_y = odom_msg.pose.pose.position.y

        # Get the velocity of the robot
        linear_x = odom_msg.twist.twist.linear.x
        angular_z = odom_msg.twist.twist.angular.z

        # Print the position and velocity of the robot
        self.get_logger().info(f"Position: x={position_x}, y={position_y}")
        self.get_logger().info(f"Velocity: vx={linear_x}, vz={angular_z}")

        # Get the orientation of the robot in quaternion form
        orientation = odom_msg.pose.pose.orientation
        quaternion = (orientation.x, orientation.y, orientation.z, orientation.w)

        # Convert the quaternion to roll-pitch-yaw
        rpy = tf_trans.euler_from_quaternion(quaternion)

        # Extract the values of roll, pitch, and yaw from the array
        roll, pitch, yaw = rpy

        # Print the roll, pitch, and yaw
        self.get_logger().info(f"Roll={math.degrees(roll)}, Pitch={math.degrees(pitch)}, Yaw={math.degrees(yaw)}")


def main(args=None):
    rclpy.init(args=args)

    odom_pose = OdomPose()

    rclpy.spin(odom_pose)

    # Clean up
    odom_pose.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
