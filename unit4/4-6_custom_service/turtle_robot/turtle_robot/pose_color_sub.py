"""위치(Pose)와 바닥 색(Color) 두 토픽을 함께 구독하는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Color, Pose


class PoseColorSub(Node):
    """최신 색을 저장해 두고 위치와 함께 출력합니다."""

    def __init__(self):
        super().__init__('pose_color_sub')
        self.color = None
        # 실습 1: /turtle1/pose와 /turtle1/color_sensor를 각각 구독합니다.
        self.pose_sub = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10)
        self.color_sub = self.create_subscription(
            Color, '/turtle1/color_sensor', self.on_color, 10)

    def on_color(self, msg):
        """최신 색을 저장합니다."""
        self.color = msg

    def on_pose(self, msg):
        """색을 받은 뒤부터 위치와 색을 한 줄로 출력합니다."""
        if self.color is None:
            return
        c = self.color
        self.get_logger().info(f'x={msg.x:.2f} rgb=({c.r}, {c.g}, {c.b})')


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = PoseColorSub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
