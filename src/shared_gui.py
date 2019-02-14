"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Tristen Foisy, Tommy Hoevener, Sam Hedrick.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation", font='Arial 14 bold')
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw", font='Arial 14 bold')
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control", font='Arial 14 bold')
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


def get_drive_system_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=1, borderwidth=5, relief='ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text='Drive System', font='Arial 14 bold')

    empty_label_1 = ttk.Label(frame, text=' ')
    empty_label_2 = ttk.Label(frame, text=' ')
    empty_label_3 = ttk.Label(frame, text=' ')

    speed_label = ttk.Label(frame, text='Robot Speed')
    inches_label = ttk.Label(frame, text='Inches moved')
    seconds_label = ttk.Label(frame, text='Seconds of movement')
    intensity_label = ttk.Label(frame, text='Intensity of Light')
    color_label = ttk.Label(frame, text='Color')
    inches_label_2 = ttk.Label(frame, text='Inches moved')
    delta_label = ttk.Label(frame, text='plus or minus(in inches) : ')
    area_label = ttk.Label(frame, text='Area seen')

    speed_entry = ttk.Entry(frame, width=8)
    inches_entry = ttk.Entry(frame, width=8)
    seconds_entry = ttk.Entry(frame, width=8)
    intensity_entry = ttk.Entry(frame, width=8)
    color_entry = ttk.Entry(frame, width=8)
    inches_entry_2 = ttk.Entry(frame, width=8)
    delta_entry = ttk.Entry(frame, width=8)
    area_entry = ttk.Entry(frame, width=8)

    forward_seconds_button = ttk.Button(frame, text='Forward with Seconds')
    forward_inches_encoder_button = ttk.Button(frame, text='Forward with Inches (using Encoder)')
    forward_inches_time_button = ttk.Button(frame, text='Forward with Inches(using Time)')
    forward_until_intensity_less_button = ttk.Button(frame, text='Forward until Intensity is less than')
    forward_until_intensity_greater_button = ttk.Button(frame, text='Forward until Intensity is greater than')
    forward_until_color_is = ttk.Button(frame, text='Forward until color is')
    forward_until_color_not = ttk.Button(frame, text='Forward until is not')
    forward_until_dist_less_than = ttk.Button(frame, text='Forward until distance is less than')
    backward_until_dist_greater_than = ttk.Button(frame, text='Backward until distance is greater than')
    go_until_dist_within = ttk.Button(frame, text='Move until distance is close to')
    display_camera_button = ttk.Button(frame, text='Display camera input')
    clockwise_until_sees_object = ttk.Button(frame, text='Spin clockwise until object with area is seen')
    counterclockwise_until_sees_object = ttk.Button(frame, text='Spin counterclockwise until object with area is seen')

    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=1)
    inches_label.grid(row=2, column=0)
    inches_entry.grid(row=3, column=0)
    seconds_label.grid(row=2, column=2)
    seconds_entry.grid(row=3, column=2)
    forward_inches_encoder_button.grid(row=4, column=0)
    forward_seconds_button.grid(row=4, column=2)
    forward_inches_time_button.grid(row=5, column=0)
    empty_label_1.grid(row=6, column=0)
    intensity_label.grid(row=7, column=0)
    color_label.grid(row=7, column=2)
    intensity_entry.grid(row=8, column=0)
    color_entry.grid(row=8, column=2)
    forward_until_intensity_less_button.grid(row=9, column=0)
    forward_until_color_is.grid(row=9, column=2)
    forward_until_intensity_greater_button.grid(row=10, column=0)
    forward_until_color_not.grid(row=10, column=2)
    empty_label_2.grid(row=11, column=1)
    inches_label_2.grid(row=12, column=0)
    inches_entry_2.grid(row=13, column=0)
    go_until_dist_within.grid(row=14, column=0)
    delta_label.grid(row=14, column=1)
    delta_entry.grid(row=14, column=2)
    forward_until_dist_less_than.grid(row=15, column=0)
    backward_until_dist_greater_than.grid(row=16, column=0)
    empty_label_3.grid(row=17, column=0)
    area_label.grid(row=18, column=0)
    area_entry.grid(row=19, column=0)
    clockwise_until_sees_object.grid(row=20, column=0)
    display_camera_button.grid(row=20, column=2)
    counterclockwise_until_sees_object.grid(row=21, column=0)

    forward_inches_encoder_button["command"] = lambda: handle_forward_inches_with_encoder(mqtt_sender, inches_entry,
                                                                                          speed_entry)
    forward_inches_time_button["command"] = lambda: handle_forward_inches_with_time(mqtt_sender, inches_entry,
                                                                                    speed_entry)
    forward_seconds_button["command"] = lambda: handle_forward_seconds(mqtt_sender, seconds_entry, speed_entry)

    forward_until_intensity_less_button["command"] = lambda: handle_forward_until_intensity_less(mqtt_sender,
                                                                                                 intensity_entry,
                                                                                                 speed_entry)

    forward_until_intensity_greater_button["command"] = lambda: handle_forward_until_intensity_greater(mqtt_sender,
                                                                                                       intensity_entry,
                                                                                                       speed_entry)

    forward_until_color_is["command"] = lambda: handle_forward_until_color_is(mqtt_sender, color_entry, speed_entry)

    forward_until_color_not["command"] = lambda: handle_forward_until_color_is_not(mqtt_sender, color_entry,
                                                                                   speed_entry)
    go_until_dist_within["command"] = lambda: handle_go_until_distance_is_within(mqtt_sender, delta_entry,
                                                                                 inches_entry_2, speed_entry)

    forward_until_dist_less_than["command"] = lambda: handle_go_forward_until_distance_is_less_than(mqtt_sender,
                                                                                                    inches_entry_2,
                                                                                                    speed_entry)

    backward_until_dist_greater_than["command"] = lambda: handle_go_backward_until_distance_is_greater_than(mqtt_sender,
                                                                                                            inches_entry_2,
                                                                                                            speed_entry)

    display_camera_button["command"] = lambda: handle_display_camera(mqtt_sender)
    clockwise_until_sees_object["command"] = lambda: handle_spin_clockwise_until_area(mqtt_sender, speed_entry,
                                                                                      area_entry)
    counterclockwise_until_sees_object["command"] = lambda: handle_spin_counterclockwise_until_area(mqtt_sender,
                                                                                                    speed_entry,
                                                                                                    area_entry)

    return frame


def get_sound_system_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=1, borderwidth=5, relief='ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text='Sound System', font='Arial 14 bold')

    number_label = ttk.Label(frame, text='Number of Beeps')
    frequency_label = ttk.Label(frame, text='Frequency')
    time_label = ttk.Label(frame, text='Duration')

    frequency_entry = ttk.Entry(frame, width=8)
    number_entry = ttk.Entry(frame, width=8)
    time_entry = ttk.Entry(frame, width=8)
    phrase_entry = ttk.Entry(frame, width=20)

    beep_button = ttk.Button(frame, text='^Beep for this many times^')
    tone_button = ttk.Button(frame, text='^Play freq. for this long^')
    phrase_button = ttk.Button(frame, text='Say this phrase:')

    frame_label.grid(row=0, column=1)
    frequency_label.grid(row=1, column=1)
    time_label.grid(row=2, column=0)
    frequency_entry.grid(row=2, column=1)
    number_label.grid(row=2, column=2)
    time_entry.grid(row=3, column=0)
    number_entry.grid(row=3, column=2)
    tone_button.grid(row=4, column=0)
    phrase_button.grid(row=4, column=1)
    beep_button.grid(row=4, column=2)
    phrase_entry.grid(row=5, column=1)

    beep_button["command"] = lambda: handle_beep(mqtt_sender, number_entry)
    tone_button["command"] = lambda: handle_tone(mqtt_sender, time_entry, frequency_entry)
    phrase_button["command"] = lambda: handle_phrase(mqtt_sender, phrase_entry)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("stop")
    mqtt_sender.send_message("stop")


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Raising arm")
    mqtt_sender.send_message("raise_arm")


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Lowering arm")
    mqtt_sender.send_message("lower_arm")


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Calibrating arm")
    mqtt_sender.send_message("calibrate_arm")


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("Moving arm to", int(arm_position_entry.get()))
    mqtt_sender.send_message("move_arm_to", [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quitting')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()


###############################################################################
# Handlers for Buttons in the Drive System.
###############################################################################
def handle_forward_seconds(mqtt_sender, seconds_entry, speed_entry):
    print("Moving forward for", seconds_entry.get(), "seconds")
    mqtt_sender.send_message("go_straight_for_seconds", [seconds_entry.get(), speed_entry.get()])


def handle_forward_inches_with_time(mqtt_sender, inches_entry, speed_entry):
    print("Moving forward", inches_entry.get(), "inches using time")
    mqtt_sender.send_message("go_straight_for_inches_using_time", [inches_entry.get(), speed_entry.get()])


def handle_forward_inches_with_encoder(mqtt_sender, inches_entry, speed_entry):
    print("Moving forward", inches_entry.get(), "inches using the encoder")
    mqtt_sender.send_message("go_straight_for_inches_using_encoder", [inches_entry.get(), speed_entry.get()])


def handle_forward_until_intensity_less(mqtt_sender, intensity_entry, speed_entry):
    print("moving forward till light intensity is less than", intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_less_than", [intensity_entry.get(), speed_entry.get()])


def handle_forward_until_intensity_greater(mqtt_sender, intensity_entry, speed_entry):
    print("moving forward till light intensity is greater than", intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_greater_than", [intensity_entry.get(), speed_entry.get()])


def handle_forward_until_color_is(mqtt_sender, color_entry, speed_entry):
    print('moving forward till color is', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is', [color_entry.get(), speed_entry.get()])


def handle_forward_until_color_is_not(mqtt_sender, color_entry, speed_entry):
    print('moving forward till color is not', color_entry.get())
    mqtt_sender.send_message('go_straight_until_color_is_not', [color_entry.get(), speed_entry.get()])


def handle_go_forward_until_distance_is_less_than(mqtt_sender, inches_entry_2, speed_entry):
    print('moving forward until distance is less than', inches_entry_2.get())
    mqtt_sender.send_message('go_forward_until_distance_is_less_than', [inches_entry_2.get(), speed_entry.get()])


def handle_go_backward_until_distance_is_greater_than(mqtt_sender, inches_entry_2, speed_entry):
    print('moving backward until distance is greater than', inches_entry_2.get())
    mqtt_sender.send_message('go_backward_until_distance_is_greater_than', [inches_entry_2.get(), speed_entry.get()])


def handle_go_until_distance_is_within(mqtt_sender, delta_entry, inches_entry_2, speed_entry):
    print('moving until distance is within', delta_entry.get(), 'inches of', inches_entry_2.get())
    mqtt_sender.send_message('go_until_distance_is_within',
                             [delta_entry.get(), inches_entry_2.get(), speed_entry.get()])


def handle_display_camera(mqtt_sender):
    print('Printing camera data:')
    mqtt_sender.send_message('display_camera_data')


def handle_spin_counterclockwise_until_area(mqtt_sender, speed_entry, area_entry):
    print('Spinning counterclockwise at speed', speed_entry.get(), 'until object of area', area_entry.get, 'is seen')
    mqtt_sender.send_message('spin_counterclockwise_until_area', [speed_entry.get(), area_entry.get()])


def handle_spin_clockwise_until_area(mqtt_sender, speed_entry, area_entry):
    print('Spinning clockwise at speed', speed_entry.get(), 'until object of area', area_entry.get, 'is seen')
    mqtt_sender.send_message('spin_clockwise_until_area', [speed_entry.get(), area_entry.get()])

###############################################################################
# Handlers for Buttons in the Sound System.
###############################################################################
def handle_beep(mqtt_sender, number_entry):
    print("Beeping", number_entry.get(), "times")
    mqtt_sender.send_message("beep_n_times", [number_entry.get()])


def handle_tone(mqtt_sender, duration_entry, frequency_entry):
    print('Playing a tone at', frequency_entry.get(), 'for', duration_entry.get(), 'seconds')
    mqtt_sender.send_message("play_a_tone_at_frequency_for_duration", [duration_entry.get(), frequency_entry.get()])


def handle_phrase(mqtt_sender, phrase_entry):
    print('Saying', phrase_entry.get())
    mqtt_sender.send_message('speak_a_phrase', [phrase_entry.get()])
