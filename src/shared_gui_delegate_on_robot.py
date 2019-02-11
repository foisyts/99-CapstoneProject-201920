"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tristen Foisy, Tommy Hoevener, Sam Hedrick.
  Winter term, 2018-2019.
"""


class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot """
        self.robot = robot

    # Teleop
    def forward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), -int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(-int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed), -int(right_wheel_speed))

    def stop(self):
        self.robot.drive_system.stop()

    # Arm and Claw
    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to(self, position):
        self.robot.arm_and_claw.move_arm_to_position(int(position))

    # Control Frame

    # DriveSystem
    def go_straight_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    # SoundSystem
    def beep_n_times(self, n):
        print('I will beep', int(n), 'times')

    def play_a_tone_at_frequency_for_duration(self, frequency, duration):
        print('I will play a tone at frequency', int(frequency), 'for duration', int(duration))

    def speak_a_phrase(self, phrase):
        print('I will now speak the phrase', phrase)
