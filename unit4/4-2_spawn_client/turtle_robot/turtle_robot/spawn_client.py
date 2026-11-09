"""/spawn 서비스를 호출해 turtle2를 만드는 Client 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class SpawnClient(Node):
    """turtle2 생성을 한 번 요청합니다."""

    def __init__(self):
        super().__init__('spawn_client')
        # 실습 1: /spawn의 Client를 만들고 서버가 준비될 때까지 기다립니다.
        self.client = self.create_client(Spawn, 'spawn')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn ...')

    def send_request(self):
        """위치와 이름을 담아 요청하고 응답을 반환합니다."""
        # 실습 2: Spawn 요청에 x, y, theta, name을 채웁니다.
        req = Spawn.Request()
        req.x = 5.0
        req.y = 5.0
        req.theta = 0.0
        req.name = 'turtle2'
        # 실습 3: call_async로 보내고 응답이 올 때까지 기다립니다.
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    """요청을 보내고 생성된 이름을 출력합니다."""
    rclpy.init(args=args)
    node = SpawnClient()
    result = node.send_request()
    node.get_logger().info(f'Spawned: {result.name}')
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
