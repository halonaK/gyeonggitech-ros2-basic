"""위치에 따라 set_pen을 호출해 좌우 선 색을 바꾸는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import SetPen


class PenColor(Node):
    """왼쪽은 빨강, 오른쪽은 파랑 선을 그립니다."""

    def __init__(self):
        super().__init__('pen_color')
        self.side = None
        # 실습 1: /turtle1/set_pen의 Client를 만들고 서버를 기다립니다.
        self.client = self.create_client(SetPen, '/turtle1/set_pen')
        self.client.wait_for_service()
        # 실습 2: /turtle1/pose를 구독합니다.
        self.sub = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )

    def on_pose(self, msg):
        """영역이 바뀔 때만 펜 색을 바꿉니다."""
        # 실습 3: x < 5.5이면 left, 아니면 right로 구분합니다.
        side = 'left' if msg.x < 5.5 else 'right'
        # 실습 4: 이전과 같은 영역이면 호출하지 않습니다.
        if side == self.side:
            return
        self.side = side
        # 실습 5: 왼쪽은 빨강, 오른쪽은 파랑으로 요청합니다.
        req = SetPen.Request()
        req.width = 5
        if side == 'left':
            req.r, req.g, req.b = 255, 0, 0
        else:
            req.r, req.g, req.b = 0, 0, 255
        self.client.call_async(req)
        self.get_logger().info(f'Pen: {side}')


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = PenColor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
