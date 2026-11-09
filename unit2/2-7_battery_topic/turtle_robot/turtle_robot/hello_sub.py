"""/hello 토픽을 구독하는 Hello Subscriber 예제입니다."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloSub(Node):
    """받은 인사말을 출력합니다."""

    def __init__(self):
        super().__init__('hello_sub')
        # 실습 1: /hello를 구독하는 Subscription을 만듭니다.
        self.sub = self.create_subscription(
            String, 'hello', self.listener_callback, 10)

    def listener_callback(self, msg):
        """메시지가 올 때마다 내용을 출력합니다."""
        # 실습 1: 받은 msg.data를 출력합니다.
        self.get_logger().info(f'I heard: {msg.data}')


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = HelloSub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
