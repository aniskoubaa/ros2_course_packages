#! /usr/bin/env python3

import rclpy
import sys

from geometry_msgs.msg import TransformStamped
from rclpy.node import Node
from scipy.spatial.transform import Rotation as R
from tf2_ros.transform_broadcaster import TransformBroadcaster
from turtlesim.msg import Pose

class DynamicTransformBroadcaster(Node):

    def __init__(self, turtle_name):
        super().__init__('dynamic_broadcaster')
        self.name_ = turtle_name
        self.get_logger().info("Broadcasting pose of : {}".format(self.name_))
        self.tfb_ = TransformBroadcaster(self)
        self.sub_pose = self.create_subscription(Pose, "{}/pose".format(self.name_), self.handle_pose, 10)

    def handle_pose(self, msg):
        
        tfs = TransformStamped()
        tfs.header.stamp = self.get_clock().now().to_msg()
        tfs.header.frame_id="world"
        tfs._child_frame_id = self.name_
        tfs.transform.translation.x = msg.x
        tfs.transform.translation.y = msg.y
        tfs.transform.translation.z = 0.0  

        r = R.from_euler('xyz',[0,0,msg.theta])

        tfs.transform.rotation.x = r.as_quat()[0]
        tfs.transform.rotation.y = r.as_quat()[1]
        tfs.transform.rotation.z = r.as_quat()[2]
        tfs.transform.rotation.w = r.as_quat()[3]

        self.tfb_.sendTransform(tfs)    

def main(argv=sys.argv[1:]):
    rclpy.init(args=argv)
    print('start\n')
    node = DynamicTransformBroadcaster(sys.argv[1])

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()