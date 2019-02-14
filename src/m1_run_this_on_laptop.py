"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Tristen Foisy.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import rosebot


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    sender2 = com.MqttClient()
    sender2.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame = get_shared_frames(
        main_frame,
        mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)


    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
    sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
    feature_9_frame = feature_9_window(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=0, column=1)
    sound_system_frame.grid(row=1, column=1)
    feature_9_frame.grid(row=0, column=2)


def feature_9_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    title_label = ttk.Label(frame, text="Tristen's Feature 9 Control Panel", font='Arial 13 bold')

    # testing_label = ttk.Label(main_frame, text="Hi! I'm working!")
    initial_label = ttk.Label(frame, text="Initial Rate:")
    rate_of_increase_label = ttk.Label(frame, text="Rate of Increase:")

    initial_entry = ttk.Entry(frame, width=8)
    rate_of_increase_entry = ttk.Entry(frame, width=8)

    forward_with_beeps_button = ttk.Button(frame, text='Go forward while beeping with the below rates')

    title_label.grid(row=0, column=1)
    # testing_label.grid()
    forward_with_beeps_button.grid(row=1, column=1)
    initial_label.grid(row=2, column=0)
    initial_entry.grid(row=2, column=2)
    rate_of_increase_label.grid(row=3, column=0)
    rate_of_increase_entry.grid(row=3, column=2)

    forward_with_beeps_button["command"] = lambda: feature_9_movement(mqtt_sender, initial_entry,
                                                                      rate_of_increase_entry)

    return frame


def feature_9_movement(mqtt_sender, initial_entry, rate_of_increase_entry):
    print("test")
    mqtt_sender.send_message("beeper_picker_upper", [initial_entry.get(), rate_of_increase_entry.get()])


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
