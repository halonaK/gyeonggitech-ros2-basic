"""배터리 잔량을 구독해 낮으면 경고하는 예제입니다."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class BatterySub(Node):
    """잔량이 20 이하이면 경고를 출력합니다."""

    def __init__(self):
        super().__init__('battery_sub')
        # 실습 2: /battery를 구독하는 Subscription을 만듭니다.
        self.sub = self.create_subscription(
            Int32, 'battery', self.listener_callback, 10)

    def listener_callback(self, msg):
        """잔량에 따라 일반 로그 또는 경고를 출력합니다."""
        # 실습 2: 20 이하이면 warn, 아니면 info로 출력합니다.
        if msg.data <= 20:
            self.get_logger().warn(f'Battery low: {msg.data}%')
        else:
            self.get_logger().info(f'Battery: {msg.data}%')


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = BatterySub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
