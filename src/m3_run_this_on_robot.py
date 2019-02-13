"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Sam Hedrick.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # real_thing()
    # run_test_arm()
    # run_test_calibrate_arm()
    # run_test_move_arm_to_position(100)
    # run_test_lower_arm()
    # run_test_go_straight_for_seconds()
    # time.sleep(2)
    # run_test_go_straight_for_inches_using_time()
    # time.sleep(1)
    # run_test_go_straight_using_encoder()
    # run_test_intensity_less_than()
    # run_test_intensity_greater_than()
    # run_test_color_is()
    # run_test_color_is_not()
    # run_test_distance_is_less_than()
    # run_test_distance_is_further_than()
    # run_test_distance_within()
    # ir_tester()
    # led_tester()
    led_blinker(2, 5)


def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break


def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()


def run_test_calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()


def run_test_move_arm_to_position(given_pos):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(given_pos)


def run_test_lower_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()


def run_test_go_straight_for_seconds():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(5, 100)


def run_test_go_straight_for_inches_using_time():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(24, 50)


def run_test_go_straight_using_encoder():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(24, 50)


def run_test_intensity_less_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(30, 100)


def run_test_intensity_greater_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_greater_than(30, 100)


def run_test_color_is():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is(6, 100)


def run_test_color_is_not():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is_not('White', 100)


def run_test_distance_is_less_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(8, 100)


def run_test_distance_is_further_than():
    robot = rosebot.RoseBot()
    robot.drive_system.go_backward_until_distance_is_greater_than(30, 100)


def run_test_distance_within():
    robot = rosebot.RoseBot()
    robot.drive_system.go_until_distance_is_within(.5, 7, 100)


def ir_tester():
    robot = rosebot.RoseBot()
    print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())


def led_tester():
    robot = rosebot.RoseBot()
    while True:
        robot.led_system.left_led.set_color_by_fractions(.33, .67)
        robot.led_system.right_led.turn_on()
        time.sleep(2)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        time.sleep(2)


def led_blinker(initial, rate):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(25, 25)
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.led_system.left_led.turn_on()
        time.sleep(initial * (1 - ((122-d) / 122 + rate)))
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(initial * (1 - ((122-d) / 122 + rate)))
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.led_system.left_led.turn_on()
        time.sleep(initial * (1 - ((122-d) / 122 + rate)))
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        time.sleep(initial * (1 - ((122-d) / 122 + rate)))
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

        if d <= 6:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.led_system.right_led.turn_off()
            robot.led_system.left_led.turn_off()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
