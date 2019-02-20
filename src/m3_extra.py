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


def fumble():
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    robot.drive_system.spin_counterclockwise_until_sees_object(25, 100)
    robot.drive_system.go(50, 50)
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if d < 2:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def juke():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is('White', 100)
    robot.drive_system.go(100, -100)
    time.sleep(2.6)
    robot.drive_system.stop()
    robot.drive_system.go(100, 100)
    time.sleep(3)
    robot.drive_system.stop()


def celebrate():
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speech_maker.speak('Touchdown')
    robot.arm_and_claw.move_arm_to_position(1500)
    time.sleep(.2)
    robot.arm_and_claw.move_arm_to_position(500)
    time.sleep(.2)
    robot.arm_and_claw.move_arm_to_position(1500)
    time.sleep(.2)
    robot.arm_and_claw.move_arm_to_position(500)
    time.sleep(.2)
    robot.arm_and_claw.move_arm_to_position(1500)
    time.sleep(.2)
    robot.arm_and_claw.move_arm_to_position(0)


def shake():
    robot = rosebot.RoseBot()
    robot.sound_system.speech_maker.speak('Good game')
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.arm_and_claw.move_arm_to_position(3500)
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.arm_and_claw.move_arm_to_position(3500)
    robot.arm_and_claw.move_arm_to_position(4000)
    robot.arm_and_claw.move_arm_to_position(3500)
    robot.arm_and_claw.lower_arm()
