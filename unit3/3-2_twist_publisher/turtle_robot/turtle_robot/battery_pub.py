"""배터리 잔량을 정수로 발행하는 예제입니다."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class BatteryPub(Node):
    """1초마다 배터리 잔량을 5씩 줄이며 발행합니다."""

    def __init__(self):
        super().__init__('battery_pub')
        # 실습 1: /battery에 Int32를 발행하는 Publisher를 만듭니다.
        self.pub = self.create_publisher(Int32, 'battery', 10)
        self.level = 100
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        """현재 잔량을 발행합니다."""
        # 실습 1: Int32 메시지에 잔량을 담아 발행합니다.
        msg = Int32()
        msg.data = self.level
        self.pub.publish(msg)
        # 실습 1: 0보다 크면 잔량을 5 줄입니다.
        if self.level > 0:
            self.level -= 5


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = BatteryPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
