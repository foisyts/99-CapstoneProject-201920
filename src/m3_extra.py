import time
import rosebot


def led_blinker(initial, rate):
    robot = rosebot.RoseBot()
    robot.drive_system.go(50, 50)
    id = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        robot.led_system.left_led.turn_on()
        time.sleep(get_sleep(robot, initial, rate, id))

        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(get_sleep(robot, initial, rate, id))

        robot.led_system.left_led.turn_on()
        time.sleep(get_sleep(robot, initial, rate, id))

        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        time.sleep(.5)

        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d <= 3:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            robot.led_system.right_led.turn_off()
            robot.led_system.left_led.turn_off()
            break


def get_sleep(robot, initial, rate, id):
    d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    # y = (((-1 / rate) * (19 - d) + initial))
    # k1 = initial + rate * id
    # y = k1 - rate * id + (rate * d)
    y = 1 / (initial + rate * (id - d))

    print('y=', y)
    if y <= .01:
        return 0.01
    else:
        return y
