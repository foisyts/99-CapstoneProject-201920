import time
import rosebot


def led_blinker(initial, rate):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(25, 25)
    while True:
        robot.led_system.left_led.turn_on()
        time.sleep(get_sleep(initial, rate))

        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(get_sleep(initial, rate))

        robot.led_system.left_led.turn_on()
        time.sleep(get_sleep(initial, rate))

        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        time.sleep(get_sleep(initial, rate))

        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d <= 3:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.led_system.right_led.turn_off()
            robot.led_system.left_led.turn_off()
            break


def get_sleep(initial, rate):
    robot = rosebot.RoseBot()
    d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    y = ((-1 / rate) * (19 - d) + initial) / 5
    if y <= .001:
        return 0.01
    else:
        return y
    print(y)