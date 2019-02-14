import rosebot
import time
import m3_extra as m3


def drive_and_beep_with_ir(initial, rate_of_increase):
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.beep()
        sleep = m3.get_sleep(initial, rate_of_increase)
        time.sleep(sleep)
        if distance <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
