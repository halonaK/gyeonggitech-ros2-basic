"""Clean 서비스로 시작·중지와 속도 배율을 요청하는 Client 예제입니다."""

import sys
import time

import rclpy
from rclpy.node import Node
# 실습 1: 직접 만든 Clean 서비스 타입을 가져옵니다.
from turtle_interfaces.srv import Clean


class CleanerClient(Node):
    """2배 속도로 5초 동안 청소했다가 멈춥니다."""

    def __init__(self, turtle):
        super().__init__('cleaner_client')
        # 실습 2: SetBool 대신 Clean 타입으로 Client를 만듭니다.
        self.client = self.create_client(
            Clean, f'/{turtle}/cleaner/enable'
        )
        self.client.wait_for_service()

    def send(self, start, scale):
        """시작 여부와 속도 배율을 요청하고 응답을 반환합니다."""
        # 실습 3: 요청에 start와 scale 두 값을 담습니다.
        req = Clean.Request()
        req.start = start
        req.scale = scale
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    """2배 속도로 시작 → 5초 대기 → 중지 순서로 실행합니다."""
    rclpy.init(args=args)
    turtle = sys.argv[1] if len(sys.argv) > 1 else 'turtle1'
    node = CleanerClient(turtle)
    # 실습 4: 시작은 scale 2.0, 중지는 scale 1.0으로 요청합니다.
    res = node.send(True, 2.0)
    node.get_logger().info(res.message)
    time.sleep(5.0)
    res = node.send(False, 1.0)
    node.get_logger().info(res.message)
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
