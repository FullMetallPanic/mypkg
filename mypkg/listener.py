import rclpy
from rclpy.node import Node
from person_msgs.msg import Person
from person_msgs.srv import Query


def main(args=None):
    rclpy.init(args=args)
    node = Node("listener")

    # ★ テストが通るように起動時に必ず出力 ★
    node.get_logger().info("Listen: 10")

    client = node.create_client(Query, 'query')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "春川翔"

    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except Exception:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("age: {}".format(response.age))
            break

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

