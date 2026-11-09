"""cmd_vel_pub와 pose_sub를 MultiThreadedExecutor로 함께 실행하는 예제입니다."""

import rclpy
from rclpy.executors import MultiThreadedExecutor

from turtle_robot.cmd_vel_pub import CmdVelPub
from turtle_robot.pose_sub import PoseSub


def main(args=None):
    """두 노드를 멀티스레드 실행기로 실행합니다."""
    rclpy.init(args=args)
    # 실습 1: CmdVelPub와 PoseSub 객체를 만듭니다.
    publisher = CmdVelPub()
    subscriber = PoseSub()
    # 실습 2: 스레드가 2개인 MultiThreadedExecutor를 만듭니다.
    executor = MultiThreadedExecutor(num_threads=2)
    # 실습 3: 두 노드를 executor에 추가하고 실행합니다.
    executor.add_node(publisher)
    executor.add_node(subscriber)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        publisher.destroy_node()
        subscriber.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
