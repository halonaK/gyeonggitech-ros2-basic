"""두 거북이 사이 거리를 보고 turtle2를 멈추는 예제입니다."""

import math
import random
import time

from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


SAFE_DISTANCE = 2.0


def distance_between(first_pose, second_pose):
    """두 위치 사이의 유클리드 거리를 계산합니다."""
    return math.hypot(
        first_pose.x - second_pose.x, first_pose.y - second_pose.y
    )


def should_stop(distance, safe_distance=SAFE_DISTANCE):
    """안전거리보다 가까우면 정지 여부를 반환합니다."""
    return distance < safe_distance


class DistanceGuard(Node):
    """turtle2만 안전거리 안에서 정지시킵니다."""

    def __init__(self):
        super().__init__('distance_guard')
        self.safe_distance = SAFE_DISTANCE
        self.turtle1_pose = None
        self.turtle2_pose = None
        self.turn_speed = 0.0
        self.next_turn_change = 0.0
        self.was_stopped = None
        self.turtle1_subscription = self.create_subscription(
            Pose, '/turtle1/pose', self.on_turtle1_pose, 10
        )
        self.turtle2_subscription = self.create_subscription(
            Pose, '/turtle2/pose', self.on_turtle2_pose, 10
        )
        self.publisher = self.create_publisher(
            Twist, '/turtle2/cmd_vel', 10
        )
        self.timer = self.create_timer(0.1, self.control_turtle2)

    def on_turtle1_pose(self, message):
        """turtle1 위치를 저장합니다."""
        self.turtle1_pose = message

    def on_turtle2_pose(self, message):
        """turtle2 위치를 저장합니다."""
        self.turtle2_pose = message

    def control_turtle2(self):
        """거리 조건에 따라 turtle2 속도를 발행합니다."""
        if self.turtle1_pose is None or self.turtle2_pose is None:
            return

        distance = distance_between(self.turtle1_pose, self.turtle2_pose)
        stopped = should_stop(distance, self.safe_distance)
        message = Twist()

        if not stopped:
            now = time.monotonic()
            if now >= self.next_turn_change:
                self.turn_speed = random.choice(
                    [-0.8, -0.4, 0.0, 0.4, 0.8]
                )
                self.next_turn_change = now + 2.0
            message.linear.x = 1.0
            message.angular.z = self.turn_speed

        if stopped != self.was_stopped:
            state = '정지' if stopped else '이동'
            self.get_logger().info(
                f'turtle2 {state}: 거리={distance:.2f}'
            )
            self.was_stopped = stopped

        self.publisher.publish(message)


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = DistanceGuard()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
