"""위치, 색상, 속도를 함께 구독하는 완성 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Color, Pose


class PoseColorVelocitySubscriber(Node):
    """세 가지 메시지를 1초마다 출력합니다."""

    def __init__(self):
        super().__init__('pose_color_vel_sub')
        self.pose = None
        self.color = None
        self.velocity = None
        # 실습 1: 위치 구독 타입을 선택합니다.
        self.pose_subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        self.color_subscription = self.create_subscription(
            Color, '/turtle1/color_sensor', self.on_color, 10
        )
        # 실습 2: 속도 구독 타입을 선택합니다.
        self.velocity_subscription = self.create_subscription(
            Twist, '/turtle1/cmd_vel', self.on_velocity, 10
        )
        # 실습 3: 세 값을 출력할 타이머를 만듭니다.
        self.timer = self.create_timer(1.0, self.print_values)

    def on_pose(self, message):
        """최근 위치를 저장합니다."""
        self.pose = message

    def on_color(self, message):
        """최근 색상을 저장합니다."""
        self.color = message

    def on_velocity(self, message):
        """최근 속도 명령을 저장합니다."""
        self.velocity = message

    def print_values(self):
        """세 메시지가 준비되면 값을 출력합니다."""
        if any(value is None for value in (
            self.pose, self.color, self.velocity
        )):
            return
        self.get_logger().info(
            f'위치=({self.pose.x:.2f}, {self.pose.y:.2f}) | '
            f'색상=({self.color.r}, {self.color.g}, {self.color.b}) | '
            f'속도=({self.velocity.linear.x:.2f}, '
            f'{self.velocity.angular.z:.2f})'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = PoseColorVelocitySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
