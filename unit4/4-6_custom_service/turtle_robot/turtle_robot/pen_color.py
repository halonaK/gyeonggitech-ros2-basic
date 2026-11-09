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
        # 실습 1: /turtle1/set_pen의 Client와 /turtle1/pose 구독을 만듭니다.
        self.pen = self.create_client(SetPen, '/turtle1/set_pen')
        self.create_subscription(Pose, '/turtle1/pose', self.on_pose, 10)

    def set_pen(self, r, b):
        """펜 색과 굵기를 담아 set_pen을 요청합니다."""
        req = SetPen.Request()
        req.r = r
        req.g = 0
        req.b = b
        req.width = 5
        self.pen.call_async(req)

    def on_pose(self, msg):
        """영역이 바뀔 때만 펜 색을 바꿉니다."""
        # 실습 1: x < 5.5이면 left, 아니면 right로 구분합니다.
        side = 'left' if msg.x < 5.5 else 'right'
        # 실습 1: 이전과 같은 영역이면 호출하지 않습니다.
        if side == self.side:
            return
        self.side = side
        if side == 'left':
            self.set_pen(255, 0)
        else:
            self.set_pen(0, 255)


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
