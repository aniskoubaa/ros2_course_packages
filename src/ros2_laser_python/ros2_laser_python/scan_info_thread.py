#!/usr/bin/env python3

import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math
import threading


class Scanner(Node):
    def __init__(self):
        super().__init__('scan_node')
        self.lock = threading.Lock()
        self.scan_data = None
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10)
        rclpy.spin_once(self, timeout_sec=0.1)

    def scan_callback(self, scan_data):
        with self.lock:
            self.scan_data = scan_data
            print('scan')

    def run(self):
        rclpy.spin_once(self, timeout_sec=0.1)
        while rclpy.ok():
            with self.lock:
                if self.scan_data is not None:
                    scan_data = self.scan_data
                    # Find minimum range
                    min_value, min_index = self.min_range_index(scan_data.ranges)
                    print("\nThe minimum range value is: ", min_value)
                    print("The minimum range index is: ", min_index)

                    # Find maximum range
                    max_value, max_index = self.max_range_index(scan_data.ranges)
                    print("\nThe maximum range value is: ", max_value)
                    print("The maximum range index is: ", max_index)

                    # Find average range
                    average_value = self.average_range(scan_data.ranges)
                    print("\nThe average range value is: ", average_value)

                    # Find average range between indices
                    average2 = self.average_between_indices(scan_data.ranges, 2, 7)
                    print("\nThe average between 2 indices is: ", average2)

                    # Print field of view
                    print("The field of view: ", self.field_of_view(scan_data))

            rclpy.spin_once(self, timeout_sec=0.1)
            time.sleep(5)

    def field_of_view(self, scan_data):
        return (scan_data.angle_max - scan_data.angle_min) * 180.0 / 3.14

    def min_range_index(self, ranges):
        ranges = [x for x in ranges if not math.isnan(x)]
        return (min(ranges), ranges.index(min(ranges)))

    def max_range_index(self, ranges):
        ranges = [x for x in ranges if not math.isnan(x)]
        return (max(ranges), ranges.index(max(ranges)))

    def average_range(self, ranges):
        ranges = [x for x in ranges if not math.isnan(x)]
        return (sum(ranges) / float(len(ranges)))

    def average_between_indices(self, ranges, i, j):
        ranges = [x for x in ranges if not math.isnan(x)]
        slice_of_array = ranges[i: j + 1]
        return (sum(slice_of_array) / float(len(slice_of_array)))


def main(args=None):
    rclpy.init(args=args)
    scanner = Scanner()
    scanner.run()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
