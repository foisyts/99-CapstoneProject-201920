import rosebot
import time


def run_test_pick_up_with_tones(initial_frequency, rate):
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    speed = 50
    robot.drive_system.go(speed, speed)
    max_freq = (initial_frequency + 19 * rate) * 2
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.tone(100, max_freq - 2 * d * rate)
        print(max_freq - d * rate)
        time.sleep(0.2)
        if d <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


##################################################
# Sprint 3 personal project
##################################################

def go_to_floor_color_and_turn(robot, color):
    speed = 70
    robot.drive_system.go_straight_until_color_is(color, speed)
    turn_90_degrees_counterclockwise(robot)


def turn_90_degrees_counterclockwise(robot):
    robot.drive_system.go(-30, 30)
    time.sleep(1)
    # need to figure out accurate time sleep based on speed given
    robot.drive_system.stop()


def go_and_pick_up_the_ingredient(robot):


def lets_get_this_bread(color, other):
    robot = rosebot.RoseBot()
    go_to_floor_color_and_turn(robot, color)
