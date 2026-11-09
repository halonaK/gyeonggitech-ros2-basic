# 경기테크 ROS 2 Basic — 차시별 완성 코드

Ubuntu 24.04 · ROS 2 Jazzy · Python

차시 폴더마다 **그 차시가 끝난 시점의 `turtle_robot` 패키지 전체**가 들어 있습니다. 듣고 있는 차시 폴더 하나만 보면 됩니다.

## 받는 방법

**방법 1. git clone**

```bash
git clone https://github.com/halonaK/gyeonggitech-ros2-basic.git
```

**방법 2. ZIP 다운로드**

GitHub 페이지에서 **Code → Download ZIP**을 눌러 받은 뒤 압축을 풉니다.

## 사용법

내 코드와 비교하는 용도입니다. `~/ros2_ws/src`에 이미 `turtle_robot`이 있으면 **덮어쓰기 전에 백업**하세요.

```bash
# 1. 내 패키지 백업
mv ~/ros2_ws/src/turtle_robot ~/ros2_ws/src/turtle_robot_backup

# 2. 차시 폴더 안의 패키지를 복사 (예: 3-5)
cp -r gyeonggitech-ros2-basic/unit3/3-5_zigzag_cleaner/turtle_robot ~/ros2_ws/src/

# 3. 빌드
cd ~/ros2_ws
colcon build
source install/setup.bash

# 4. 실행 (다른 터미널에서 ros2 run turtlesim turtlesim_node 먼저 실행)
ros2 run turtle_robot cleaner
```

4-6 폴더는 `turtle_interfaces`도 함께 복사합니다.

```bash
cp -r gyeonggitech-ros2-basic/unit4/4-6_custom_service/* ~/ros2_ws/src/
```

## 차시별 폴더

| 차시 | 제목 | 폴더 | 이 차시에서 추가·변경된 실행 파일 | 비고 |
| --- | --- | --- | --- | --- |
| 1-1 | ROS 2 소개 | — | — | 코드 없음 |
| 1-2 | Ubuntu 개발환경 | — | — | 코드 없음 |
| 1-3 | 리눅스 CLI 기초 | — | — | 코드 없음 |
| 1-4 | ROS 2 설치·환경설정 | — | — | 코드 없음 |
| 2-1 | 노드와 토픽 개요 | — | — | 코드 없음 |
| 2-2 | CLI로 노드와 토픽 | — | — | 코드 없음 |
| 2-3 | 토픽으로 메시지 보내기 | — | — | 코드 없음 |
| 2-4 | 메시지 타입과 인터페이스 | — | — | 코드 없음 |
| 2-5 | Hello Publisher | `unit2/2-5_hello_publisher` | `hello_pub` | |
| 2-6 | Hello Subscriber | `unit2/2-6_hello_subscriber` | `hello_sub` | |
| 2-7 | Battery 토픽 | `unit2/2-7_battery_topic` | `battery_pub`, `battery_sub` | |
| 3-1 | 결과물 소개·cmd_vel | — | — | 코드 없음 |
| 3-2 | Twist Publisher | `unit3/3-2_twist_publisher` | `cmd_vel_pub` | 더 해보기: `growing_circle` |
| 3-3 | Pose Subscriber | `unit3/3-3_pose_subscriber` | `pose_sub` | |
| 3-4 | Pose·Color 구독 | `unit3/3-4_pose_color_subscriber` | `pose_color_sub` | 더 해보기: `color_sub`, `pose_color_vel_sub` |
| 3-5 | 지그재그 청소기 | `unit3/3-5_zigzag_cleaner` | `cleaner` | 더 해보기: `wall_turn` |
| 3-6 | 토픽 통합 점검 | `unit3/3-6_topic_check` | — | 더 해보기: `multi_thread` |
| 4-1 | Service 개념·CLI | — | — | 코드 없음 |
| 4-2 | Service Client 거북이 생성 | `unit4/4-2_spawn_client` | `spawn_client` | 더 해보기: `teleport_client` |
| 4-3 | Pose·set_pen 선 색 | `unit4/4-3_pen_color` | `pen_color` | |
| 4-4 | Service Server 청소 시작·중지 | `unit4/4-4_cleaner_server` | `cleaner` (SetBool 서버) | |
| 4-5 | 청소 요청 Client | `unit4/4-5_cleaner_client` | `cleaner_client`, `cleaner` (거북이 선택) | |
| 4-6 | 사용자정의 서비스 | `unit4/4-6_custom_service` | `turtle_interfaces` (Clean.srv), `cleaner`, `cleaner_client` | 더 해보기: `distance_guard` |
| 5-1 ~ 5-6 | Parameter·Launch | — | — | 추가 예정 |
| 6-1 ~ 6-6 | Manipulator URDF | — | — | 추가 예정 |
| 7-1 ~ 7-7 | Mobile Robot Nav2 | — | — | 추가 예정 |

"더 해보기" 파일은 그 차시 폴더에만 있습니다. 다음 차시 폴더에는 수업 본 내용 파일만 이어집니다.
