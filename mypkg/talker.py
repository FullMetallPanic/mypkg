import rclpy
from rclpy.node import Node
from person_msgs.msg import Query

rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "春川翔":
          responce.age = 20
    else:
         responce.age = 255

    return response



def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)
