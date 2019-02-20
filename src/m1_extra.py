import rosebot
import time
import m3_extra as m3


def drive_and_beep_with_ir(initial, rate_of_increase):
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    id = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.beep()
        sleep = m3.get_sleep(robot, initial, rate_of_increase, id)
        time.sleep(sleep)
        if distance <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


def drive_rainbow():
    robot = rosebot.RoseBot()
    speed = 50
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(15, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)
    curved_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(4, speed)
    curved_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(18, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(4, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(30, speed)
    curved_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(32, speed)


def drive_koopa():
    robot = rosebot.RoseBot()
    speed = 50
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)
    robot.drive_system.go(10, speed)
    time.sleep(2.11)
    robot.drive_system.go(speed * 2, speed)


def drive_bowser():
    robot = rosebot.RoseBot()
    speed = 50
    robot.drive_system.go_straight_for_inches_using_encoder(12, speed)
    robot.drive_system.go(speed, -speed)
    time.sleep(0.725)
    robot.drive_system.go_straight_for_inches_using_encoder(3, speed)
    robot.drive_system.go(speed, -speed)
    time.sleep(0.725)
    robot.drive_system.go_straight_for_inches_using_encoder(8, speed)
    hard_90_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(5, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(7, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(5, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(3, speed)
    hard_90_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(5, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(5, speed)
    hard_90_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(3, speed)
    hard_90_left(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(5, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(10, speed)
    drive_loop(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(24, speed)
    hard_90_right(robot, speed)
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)


def hard_90_right(robot, speed):
    robot.drive_system.go(speed, -speed)
    time.sleep(1.42)


def hard_90_left(robot, speed):
    robot.drive_system.go(-speed, speed)
    time.sleep(1.42)


def drive_loop(robot, speed):
    robot.drive_system.go(20, 2 * speed)
    time.sleep(5.08)
    robot.drive_system.stop()


def curved_right(robot, speed):
    robot.drive_system.go(speed, 10)
    time.sleep(4.25)


def curved_left(robot, speed):
    robot.drive_system.go(10, speed)
    time.sleep(4.25)
