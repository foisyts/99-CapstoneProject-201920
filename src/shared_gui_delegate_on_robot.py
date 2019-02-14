"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Tristen Foisy, Tommy Hoevener, Sam Hedrick.
  Winter term, 2018-2019.
"""
import time
import m1_extra
import m2_run_this_on_robot as m2


class DelegateThatReceives(object):
    def __init__(self, robot):
        """:type robot: rosebot.RoseBot """
        self.robot = robot
        self.is_time_to_stop = False

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
    def quit(self):
        print('got quit')
        self.is_time_to_stop = True

    def exit(self):
        print('got exit')
        self.quit()
        self.exit()

    # DriveSystem
    def go_straight_for_seconds(self, seconds, speed):
        self.robot.drive_system.go_straight_for_seconds(int(seconds), int(speed))

    def go_straight_for_inches_using_time(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(speed))

    def go_straight_for_inches_using_encoder(self, inches, speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def go_straight_until_intensity_is_less_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def go_straight_until_intensity_is_greater_than(self, intensity, speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_straight_until_color_is(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is(color, int(speed))

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color, int(speed))

    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(float(inches), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(float(inches), int(speed))

    def go_until_distance_is_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(float(delta), float(inches), int(speed))

    def display_camera_data(self):
        self.robot.drive_system.display_camera_data()

    # SoundSystem
    def beep_n_times(self, n):
        # print('I will beep', int(n), 'times at', frequency)
        print('beeping')
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep().wait()

    def play_a_tone_at_frequency_for_duration(self, duration, frequency):
        # print('I will play a tone at frequency', int(frequency), 'for duration', int(duration))
        self.robot.sound_system.tone(int(frequency), int(duration))

    def speak_a_phrase(self, phrase):
        print('I will now speak the phrase', phrase)
        self.robot.sound_system.speak(phrase)

    # Tommy's functions
    def tone_picker_upper(self, initial_frequency, rate):
        print('Running tone_picker_upper')
        m2.run_test_pick_up_with_tones(int(initial_frequency), int(rate))
