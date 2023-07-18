#! /usr/bin/python3

import rclpy
from rclpy.node import Node

class firstNode(Node):
    def __init__(self):
        super().__init__("firstNode")
        self.get_logger().info("firstNode has been started")
        self.create_timer(1.0, self.timer_callback)
        self.counter = 0 
        
    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("Hello World: %d" % self.counter)
         



def main(args = None):
    rclpy.init(args=args)
    # Create a node
    node = firstNode()
    rclpy.spin(node)
    # Create a timer
    timer = node.create_timer(1.0, node.timer_callback)
    print("Timer has been created")
    


if __name__ == '__main__':
    main()
    