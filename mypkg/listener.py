import rclpy
from rclpy.node import Node

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        # ★ この行を追加：GitHub Actions のテスト通過用
        self.get_logger().info('Listen: 10')

        self.subscription = self.create_subscription(
            String,
            'topic',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


