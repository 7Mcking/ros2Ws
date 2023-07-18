#! /usr/bin/python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

class TurtleController(Node):
    def __init__(self):
        super().__init__("turtleController")
        self.previousX = 0
        self.get_logger().info("turtleController has been started")
        self.cmd_velocity_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.create_subsciber =  self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        self.counter = 0

    def pose_callback(self, pose: Pose):
        cmd = Twist()
               
                
        if pose.x > 9 or pose.x < 2 or pose.y > 9 or pose.y < 2:
            cmd.linear.x = 2.0
            cmd.angular.z = 1.3
        else:
            cmd.linear.x = 5.0 
            cmd.angular.z = 0.0
        
        self.cmd_velocity_publisher.publish(cmd)
        
        if pose.x>5.5 and self.previousX<5.5:
            self.previousX = pose.x
            self.get_logger().info("Red")
            self.call_set_pen_service(255, 0, 0, 2, 0)
        elif self.previousX>5.5 and pose.x<5.5:
            self.previousX = pose.x
            self.get_logger().info("Green")
            self.call_set_pen_service(0, 255, 0, 2, 0)
        
        self.get_logger().info("Pose: x: %f, y: %f, theta: %f" 
                               % (pose.x, pose.y, pose.theta))
    def call_set_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server SetPen")
            
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off
        
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))
        
    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service called failed: %r" % (e,))
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()
    
    