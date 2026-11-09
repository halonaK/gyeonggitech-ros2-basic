"""거북이를 지정한 위치로 순간이동시키는 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute


class TeleportClient(Node):
    """순간이동 서비스를 한 번 호출합니다."""

    def __init__(self):
        super().__init__('teleport_client')
        # 실습 1: /turtle1/teleport_absolute의 Client를 만듭니다.
        self.client = self.create_client(
            TeleportAbsolute, '/turtle1/teleport_absolute'
        )

    def send_request(self):
        """고정된 위치로 이동하는 요청을 보냅니다."""
        # 실습 2: x=2.0, y=2.0, theta=0.0인 요청 메시지를 만듭니다.
        request = TeleportAbsolute.Request()
        request.x = 2.0
        request.y = 2.0
        request.theta = 0.0
        # 실습 3: call_async로 요청을 보내고 Future를 반환합니다.
        return self.client.call_async(request)


def main(args=None):
    """서비스를 호출하고 응답을 기다립니다."""
    rclpy.init(args=args)
    node = TeleportClient()
    # 실습 4: 서비스가 준비될 때까지 기다립니다.
    node.client.wait_for_service()
    # 실습 5: 요청을 보내고 완료될 때까지 spin합니다.
    future = node.send_request()
    rclpy.spin_until_future_complete(node, future)
    future.result()
    node.get_logger().info('순간이동 완료')
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
