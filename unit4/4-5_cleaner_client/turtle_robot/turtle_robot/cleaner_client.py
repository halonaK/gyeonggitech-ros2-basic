"""청소기 서버에 시작·중지를 요청하는 Client 예제입니다."""

import sys
import time

import rclpy
from rclpy.node import Node
# 실습 1: SetBool 서비스 타입을 가져옵니다.
from std_srvs.srv import SetBool


class CleanerClient(Node):
    """청소를 5초 동안 시작했다가 멈춥니다."""

    def __init__(self, turtle):
        super().__init__('cleaner_client')
        # 실습 2: /<거북이>/cleaner/enable의 Client를 만들고 서버를 기다립니다.
        self.client = self.create_client(
            SetBool, f'/{turtle}/cleaner/enable'
        )
        self.client.wait_for_service()

    def send(self, start):
        """시작(True) 또는 중지(False)를 요청하고 응답을 반환합니다."""
        # 실습 3: 요청에 start 값을 담아 보내고 응답을 기다립니다.
        req = SetBool.Request()
        req.data = start
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    """시작 요청 → 5초 대기 → 중지 요청 순서로 실행합니다."""
    rclpy.init(args=args)
    turtle = sys.argv[1] if len(sys.argv) > 1 else 'turtle1'
    node = CleanerClient(turtle)
    res = node.send(True)
    node.get_logger().info(res.message)
    # 실습 4: 5초 동안 청소하도록 기다립니다.
    time.sleep(5.0)
    res = node.send(False)
    node.get_logger().info(res.message)
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
