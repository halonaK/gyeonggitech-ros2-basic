"""실행 인자로 청소할 거북이를 고르는 청소기 예제입니다."""

import sys

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
# 실습 1: SetBool 서비스 타입을 가져옵니다.
from std_srvs.srv import SetBool
from turtlesim.msg import Pose


class Cleaner(Node):
    """상태를 바꿔 가며 화면 위쪽까지 지그재그로 청소합니다."""

    def __init__(self, turtle):
        # 실습 5: 거북이 이름으로 노드·토픽·서비스 이름을 만듭니다.
        super().__init__(f'{turtle}_cleaner')
        self.pose = None
        self.state = 'FORWARD'
        self.direction = 1  # 1: 오른쪽으로 진행, -1: 왼쪽으로 진행
        self.count = 0
        self.sub = self.create_subscription(
            Pose, f'/{turtle}/pose', self.on_pose, 10
        )
        self.pub = self.create_publisher(
            Twist, f'/{turtle}/cmd_vel', 10
        )
        self.timer = self.create_timer(0.1, self.move)
        # 실습 2: 청소 상태를 저장하고 시작·중지 서비스를 만듭니다.
        self.running = False
        self.srv = self.create_service(
            SetBool, f'/{turtle}/cleaner/enable', self.enable_callback
        )

    def on_pose(self, msg):
        """최신 위치를 저장합니다."""
        self.pose = msg

    def enable_callback(self, request, response):
        """요청 값으로 청소를 시작하거나 멈춥니다."""
        # 실습 3: request.data를 저장하고 응답을 채워 반환합니다.
        self.running = request.data
        if not request.data:
            self.pub.publish(Twist())
        response.success = True
        response.message = f'running={self.running}'
        return response

    def change(self, state):
        """다음 상태로 바꾸고 틱 횟수를 초기화합니다."""
        self.state = state
        self.count = 0

    def move(self):
        """현재 상태에 맞는 속도를 발행합니다."""
        # 실습 4: 청소 중이 아니면 움직이지 않습니다.
        if not self.running:
            return
        if self.pose is None:
            return
        cmd = Twist()

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
    turtle = sys.argv[1] if len(sys.argv) > 1 else 'turtle1'
    node = Cleaner(turtle)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
