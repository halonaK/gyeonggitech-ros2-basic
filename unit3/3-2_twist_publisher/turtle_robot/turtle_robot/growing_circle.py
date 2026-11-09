"""점점 커지는 원을 그리는 확장 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node


class GrowingCirclePublisher(Node):
    """전진 속도를 증가시켜 원의 반지름을 키웁니다."""

    def __init__(self):
        super().__init__('growing_circle')
        # 실습 1: /turtle1/cmd_vel Publisher를 만듭니다.
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        # 실습 2: 선속도와 각속도를 저장하고 0.1초 Timer를 만듭니다.
        self.linear_speed = 0.2
        self.angular_speed = 1.0
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        """회전 속도는 유지하고 전진 속도를 증가시킵니다."""
        # 실습 3: Twist를 발행한 뒤 linear_speed를 조금 증가시킵니다.
        message = Twist()
        message.linear.x = self.linear_speed
        message.angular.z = self.angular_speed
        self.publisher.publish(message)
        self.linear_speed += 0.002


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = GrowingCirclePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
