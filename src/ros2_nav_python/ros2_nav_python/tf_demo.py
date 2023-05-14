#!/usr/bin/env python3

# This script converts between Roll-Pitch-Yaw angles and Quaternions

import rclpy
import math
import tf_transformations as tf




def main(args=None):
    rclpy.init(args=args)

    print('-----------------------------------------')
    print('Roll-Pitch-Yaw Conversion to Quaternions')
    print('-----------------------------------------')
    # We define some random angles roll, pitch, and yaw in radians
    roll = math.radians(30)
    pitch = math.radians(42)
    yaw = math.radians(58)

    # We print these three angles
    print(f'roll = {math.degrees(roll)}, pitch = {math.degrees(pitch)}, yaw = {math.degrees(yaw)}')
    
    # Convert the roll-pitch-yaw angles to a quaternion using ROS TF Library
    quaternion = tf.quaternion_from_euler(roll, pitch, yaw)

    print('-----------------------------------------')
    print('Quaternion using "quaternion_from_euler" function:')
    for i in range(4):
        print(quaternion[i])

    # Perform the opposite conversion
    rpy = tf.euler_from_quaternion(quaternion)
    roll_from_quaternion = rpy[0]
    pitch_from_quaternion = rpy[1]
    yaw_from_quaternion = rpy[2]

    print('-----------------------------------------')
    print('Roll-pitch-yaw using "euler_from_quaternion" function:')
    print(f'roll = {math.degrees(roll_from_quaternion)}, \npitch = {math.degrees(pitch_from_quaternion)}, \nyaw = {math.degrees(yaw_from_quaternion)}')
    print('Same initial roll-picth-roll values')
    print('-----------------------------------------')

    # Define a new quaternion
    print('Define a new quaternion manually as a list')
    q = (-3.88256895463e-06, 0.0015896463485, 0.001397167245, 0.0)

    # Perform the opposite conversion
    rpy = tf.euler_from_quaternion(q)
    roll_from_quaternion = rpy[0]
    pitch_from_quaternion = rpy[1]
    yaw_from_quaternion = rpy[2]
    print('-----------------------------------------')
    print('Roll-pitch-yaw using "euler_from_quaternion" function:')
    print(f'roll = {math.degrees(roll_from_quaternion)}, \npitch = {math.degrees(pitch_from_quaternion)}, \nyaw = {math.degrees(yaw_from_quaternion)}')
    print('-----------------------------------------')
    print('You can change these values in the file to make other conversions')

    rclpy.shutdown()

if __name__ == '__main__':
    main()