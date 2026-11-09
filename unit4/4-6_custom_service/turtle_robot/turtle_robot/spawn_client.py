"""/spawn 서비스를 호출해 turtle2를 만드는 Client 예제입니다."""

import rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn


class SpawnClient(Node):
    """turtle2 생성을 한 번 요청합니다."""

    def __init__(self):
        super().__init__('spawn_client')
        # 실습 2: /spawn의 Client를 만들고 Server가 준비될 때까지 기다립니다.
        self.client = self.create_client(Spawn, '/spawn')
        while not self.client.wait_for_service(1.0):
            self.get_logger().info('waiting ...')

    def spawn(self, x, y, theta, name):
        """위치와 이름을 담아 요청하고 future를 반환합니다."""
        # 실습 2: Spawn 요청에 x, y, theta, name을 채워 call_async로 보냅니다.
        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        req.name = name
        return self.client.call_async(req)


def main(args=None):
    """turtle2 생성을 요청하고 응답 이름을 출력합니다."""
    rclpy.init(args=args)
    node = SpawnClient()
    # 실습 2: 응답이 올 때까지 기다린 뒤 결과를 읽습니다.
    future = node.spawn(3.0, 3.0, 0.0, 'turtle2')
    rclpy.spin_until_future_complete(node, future)
    result = future.result()
    node.get_logger().info(f'spawned: {result.name}')
    node.destroy_node()
    rclpy.try_shutdown()


if __name__ == '__main__':
    main()
