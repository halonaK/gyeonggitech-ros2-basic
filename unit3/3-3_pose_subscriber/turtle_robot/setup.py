"""turtle_robot 패키지 설치 설정입니다 (3-3 완성본)."""

from setuptools import find_packages, setup

package_name = 'turtle_robot'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Instructor',
    maintainer_email='instructor@example.com',
    description='경기테크 ROS 2 Basic 3-3 완성본',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_pub = turtle_robot.hello_pub:main',
            'hello_sub = turtle_robot.hello_sub:main',
            'battery_pub = turtle_robot.battery_pub:main',
            'battery_sub = turtle_robot.battery_sub:main',
            'cmd_vel_pub = turtle_robot.cmd_vel_pub:main',
            'pose_sub = turtle_robot.pose_sub:main',
        ],
    },
)
