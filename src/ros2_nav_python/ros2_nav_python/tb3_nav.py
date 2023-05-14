
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
import tf_transformations as tf

locations_str = """
[
    {"name": "point1", "x": 2.5, "y": 1.6, "theta": 0.0},
    {"name": "point2", "x": 2.5, "y": 1.6, "theta": 0.0}
]
"""
import json
locations_json = json.loads(locations_str) 

class LocationNavigationNode(Node):
    def __init__(self):
        super().__init__('location_navigation_node')
        self.nav_action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        
        
        self.go_to_goal("point1")
        #self.go_to_goal("point2")
        #self.go_to_goal("point3")



    def get_coordinate_from_location(self, target_location:str):
        for location in locations_json:
            if location["name"] in target_location:
                return location["x"], location["y"], location["theta"]
            else:
                print("ERROR:No location found in the received JSON command")


    def go_to_goal(self, target_location:str):

        x_goal, y_goal, yaw_goal = self.get_coordinate_from_location(target_location) 
        print(target_location, x_goal, y_goal, yaw_goal)
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.pose.position.x = x_goal
        goal_msg.pose.pose.position.y = y_goal
        goal_msg.pose.pose.position.z = 0.0
        quaternion = tf.quaternion_from_euler(0.0, 0.0, yaw_goal)
        goal_msg.pose.pose.orientation.x = quaternion[0]
        goal_msg.pose.pose.orientation.y = quaternion[1]
        goal_msg.pose.pose.orientation.z = quaternion[2]
        goal_msg.pose.pose.orientation.w = quaternion[3]

        self.get_logger().info(f'Sending navigation goal')
        self.nav_action_client.wait_for_server()
        goal_handle = self.nav_action_client.send_goal_async(goal_msg)
        goal_handle.add_done_callback(self.navigation_goal_done_callback)

        

def main(args=None) -> None:
    rclpy.init(args=args)
    location_navigation_node = LocationNavigationNode()

    # Start keyboard input thread
    #keyboard_input_thread = threading.Thread(target=location_navigation_node.read_keyboard_input)
    #keyboard_input_thread.daemon = True
    #keyboard_input_thread.start()

    rclpy.spin(location_navigation_node)
    location_navigation_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()