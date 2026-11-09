"""위치를 보며 지그재그로 움직이는 거북이 청소기 예제입니다."""

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class Cleaner(Node):
    """상태를 바꿔 가며 화면 위쪽까지 지그재그로 청소합니다."""

    def __init__(self):
        super().__init__('cleaner')
        self.pose = None
        # 실습 2: 상태, 진행 방향, 틱 횟수를 저장합니다.
        self.state = 'FORWARD'
        self.direction = 1  # 1: 오른쪽으로 진행, -1: 왼쪽으로 진행
        self.count = 0
        # 실습 1: /turtle1/pose를 구독하고 /turtle1/cmd_vel에 발행합니다.
        self.sub = self.create_subscription(
            Pose, '/turtle1/pose', self.on_pose, 10
        )
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.move)

    def on_pose(self, msg):
        """최신 위치를 저장합니다."""
        self.pose = msg

    def change(self, state):
        """다음 상태로 바꾸고 틱 횟수를 초기화합니다."""
        self.state = state
        self.count = 0

    def move(self):
        """현재 상태에 맞는 속도를 발행합니다."""
        if self.pose is None:
            return
        cmd = Twist()

        # 실습 2: FORWARD → TURN1 → SHIFT → TURN2 순서로 상태를 바꿉니다.
        if self.state == 'FORWARD':
            cmd.linear.x = 2.0
            at_right = self.direction == 1 and self.pose.x > 9.5
            at_left = self.direction == -1 and self.pose.x < 1.5
            if at_right or at_left:
                self.change('TURN1')

        elif self.state == 'TURN1':
            cmd.angular.z = 1.57 * self.direction
            self.count += 1
            if self.count >= 10:
                self.change('SHIFT')

        elif self.state == 'SHIFT':
            cmd.linear.x = 2.0
            self.count += 1
            if self.count >= 5:
                self.change('TURN2')

        elif self.state == 'TURN2':
            cmd.angular.z = 1.57 * self.direction
            self.count += 1
            if self.count >= 10:
                self.direction = -self.direction
                if self.pose.y > 9.0:
                    self.change('DONE')
                else:
                    self.change('FORWARD')

        self.pub.publish(cmd)


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = Cleaner()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
