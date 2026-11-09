"""Twist를 발행해 거북이가 사각형으로 움직이게 하는 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class CmdVelPub(Node):
    """직진 2초, 회전 1초를 반복합니다."""

    def __init__(self):
        super().__init__('cmd_vel_pub')
        # 실습 1: /turtle1/cmd_vel에 Twist를 발행하는 Publisher를 만듭니다.
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # 실습 2: 0.1초마다 늘어나는 tick으로 구간을 나눕니다.
        self.tick = 0
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        """구간(tick)에 따라 직진 또는 회전 속도를 발행합니다."""
        msg = Twist()
        # 실습 2: 30틱 중 앞 20틱은 직진, 나머지 10틱은 90도 회전합니다.
        if self.tick % 30 < 20:
            msg.linear.x = 1.0
        else:
            msg.angular.z = 1.57
        self.tick += 1
        self.pub.publish(msg)


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = CmdVelPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
