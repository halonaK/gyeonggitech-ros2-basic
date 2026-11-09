"""거북이 바닥 색상 토픽을 구독하는 완성 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Color


class ColorSubscriber(Node):
    """RGB 색상을 출력합니다."""

    def __init__(self):
        super().__init__('color_sub')
        # 실습 1: 메시지 타입과 토픽 이름을 선택합니다.
        self.subscription = self.create_subscription(
            Color, '/turtle1/color_sensor', self.on_color, 10
        )

    def on_color(self, message):
        """새 색상을 출력합니다."""
        # 실습 2: 메시지의 값을 출력합니다.
        self.get_logger().info(
            f'색상 R={message.r}, G={message.g}, B={message.b}'
        )


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = ColorSubscriber()
    try:
        # 실습 3: 콜백을 계속 처리합니다.
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
