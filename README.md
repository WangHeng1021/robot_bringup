# robot_bringup
# 查看手柄连接状态
rockchip@ubuntu:~$ docker exec -it lingchu_nav bash
root@ubuntu:~/ws# source install/setup.bash 
root@ubuntu:~/ws# ros2 run  joy joy_enumerate_devices
ID : GUID                             : GamePad : Mapped : Joystick Device Name
-------------------------------------------------------------------------------
 0 : 030000006d04000019c2000011010000 :    true :   true : Logitech F710 Gamepad (DInput)

# 运行手柄驱动
rockchip@ubuntu:~$ docker exec -it lingchu_nav bash
root@ubuntu:~/ws# source install/setup.bash 
root@ubuntu:~/ws# ros2 launch robot_bringup teleop_f710.launch.py
