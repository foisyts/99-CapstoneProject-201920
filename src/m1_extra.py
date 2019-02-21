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
    # calls the functions that will move the robot through the rainbow track
    robot = rosebot.RoseBot()
    speed = 50
    starting_beeps(robot)
    rainbow_course(robot, speed)
    robot.arm_and_claw.lower_arm()


def drive_koopa():
    # calls the functions that will move the robot through the koopa track (unimplimented)
    robot = rosebot.RoseBot()
    speed = 50
    robot.drive_system.go_straight_for_inches_using_encoder(6, speed)
    robot.drive_system.go(10, speed)
    time.sleep(2.11)
    robot.drive_system.go(speed * 2, speed)


def drive_bowser():
    # calls the functions that will move the robot through the bowser track
    robot = rosebot.RoseBot()
    speed = 50
    starting_beeps(robot)
    bowser_course(robot, speed)
    robot.arm_and_claw.lower_arm()


def hard_90_right(robot, speed):
    # custom function to turn a sharp 90 degrees to the left
    robot.drive_system.go(speed, -speed)
    time.sleep(1.42)


def hard_90_left(robot, speed):
    # custom function to turn a sharp 90 degrees to the left
    robot.drive_system.go(-speed, speed)
    time.sleep(1.42)


def drive_loop(robot, speed):
    # custom function to drive in a loop
    robot.drive_system.go(20, 2 * speed)
    time.sleep(5.08)
    robot.drive_system.stop()


def curved_right(robot, speed):
    # custom function to turn a 'round' 90 degrees to the right
    robot.drive_system.go(speed, 10)
    time.sleep(4.25)


def curved_left(robot, speed):
    # custom function to turn a 'round' 90 degrees to the left
    robot.drive_system.go(10, speed)
    time.sleep(4.25)


def rainbow_course(robot, speed):
    # sequence for driving through the rainbow road course
    my_go_straight_inches(robot, 24, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 15, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 6, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 6, speed)
    curved_left(robot, speed)
    my_go_straight_inches(robot, 4, speed)
    curved_left(robot, speed)
    my_go_straight_inches(robot, 18, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 4, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 30, speed)
    curved_right(robot, speed)
    my_go_straight_inches(robot, 32, speed)


def bowser_course(robot, speed):
    # sequence for driving through the bowser's castle course
    my_go_straight_inches(robot, 12, speed)
    robot.drive_system.go(speed, -speed)
    time.sleep(0.725)
    my_go_straight_inches(robot, 3, speed)
    robot.drive_system.go(speed, -speed)
    time.sleep(0.725)
    my_go_straight_inches(robot, 8, speed)
    hard_90_left(robot, speed)
    my_go_straight_inches(robot, 5, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 7, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 5, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 3, speed)
    hard_90_left(robot, speed)
    my_go_straight_inches(robot, 5, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 5, speed)
    hard_90_left(robot, speed)
    my_go_straight_inches(robot, 3, speed)
    hard_90_left(robot, speed)
    my_go_straight_inches(robot, 5, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 10, speed)
    drive_loop(robot, speed)
    my_go_straight_inches(robot, 24, speed)
    hard_90_right(robot, speed)
    my_go_straight_inches(robot, 6, speed)


def my_go_straight_inches(robot, inches, speed):
    # goes straight for inches while simultaneously searching (using the camera) for a 'powerup' block, which is then
    # picked up using data from the IR sensor
    inches_per_degree = robot.drive_system.left_motor.WheelCircumference / 360
    desired_degrees = inches / inches_per_degree
    robot.drive_system.left_motor.reset_position()
    robot.drive_system.go(speed, speed)
    while True:
        angular_position = abs(robot.drive_system.left_motor.get_position())
        if desired_degrees <= angular_position:
            robot.drive_system.stop()
            break
        if robot.sensor_system.camera.get_biggest_blob().width >= 30:
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2:
                robot.drive_system.stop()
                robot.arm_and_claw.raise_arm()
                robot.sound_system.speak("Let's uh go!")
                robot.drive_system.go(speed, speed)


def starting_beeps(robot):
    # beeps in the manner of "3, 2, 1, GO!"
    for k in range(4):
        if k < 3:
            robot.sound_system.tone(400, 1000)
            time.sleep(0.4)
        else:
            robot.sound_system.tone(900, 2200)
