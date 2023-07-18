#! /usr/bin/python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__("poseSubscriber")
        self.get_logger().info("poseSubscriber has been started")
        self.pose_subscriber =  self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info("Pose: x: %f, y: %f, theta: %f, linear_velocity: %f, angular_velocity: %f" % (msg.x, msg.y, msg.theta, msg.linear_velocity, msg.angular_velocity))


def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()