"""문자열을 1초마다 발행하는 Hello Publisher 예제입니다."""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPublisher(Node):
    """/hello 토픽으로 인사말을 발행합니다."""

    def __init__(self):
        super().__init__('hello_pub')
        # 실습 1: /hello에 String을 발행하는 Publisher를 만듭니다.
        self.pub = self.create_publisher(String, 'hello', 10)
        # 실습 2: publish_hello를 1초마다 실행하는 Timer를 만듭니다.
        self.timer = self.create_timer(1.0, self.publish_hello)
        self.count = 0

    def publish_hello(self):
        """인사말을 발행하고 숫자를 1 늘립니다."""
        # 실습 3: String 메시지를 만들어 발행합니다.
        msg = String()
        msg.data = f'Hello Turtle {self.count}'
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        # 실습 4: 다음 발행을 위해 count를 1 늘립니다.
        self.count += 1


def main(args=None):
    """노드를 실행합니다."""
    rclpy.init(args=args)
    node = HelloPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
