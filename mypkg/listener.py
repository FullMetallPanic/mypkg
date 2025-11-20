import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


rclpy.init()
node = Node("listener")


def cd(msg):
    global node
    node.get_logger().info("listen: %d" % msg.data)


def main():
    pub = node.create_subscription(Int16, "countup", cd ,10)
    rclpy.spin(node)
