"""거북이 위치(Pose)를 구독해 출력하는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class PoseSub(Node):
    """/turtle1/pose의 x, y, theta를 출력합니다."""

    def __init__(self):
        super().__init__('pose_sub')
        # 실습 1: /turtle1/pose를 구독하는 Subscription을 만듭니다.
        self.sub = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )

    def on_pose(self, msg):
        """받은 위치를 소수 둘째 자리까지 출력합니다."""
        self.get_logger().info(
            f'x={msg.x:.2f}, y={msg.y:.2f}, theta={msg.theta:.2f}'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = PoseSub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
