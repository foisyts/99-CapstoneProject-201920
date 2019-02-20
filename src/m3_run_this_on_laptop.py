"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Sam Hedrick.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


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

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project, Winter 2018-19")
    root.config(bg='green')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    # teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, led_frame = get_shared_frames(main_frame,
    # mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, led_frame)
    football = football_frame(main_frame, mqtt_sender)
    football.grid(row=2, column=2)

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
    led_frame = get_sams_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, led_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, led_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=0, column=1)
    sound_system_frame.grid(row=1, column=1)
    led_frame.grid(row=0, column=3)


def get_sams_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge", bg='#00ff00')
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sam's Frame", font='Arial 14 bold')
    led_picker_upper_button = ttk.Button(frame, text="Pick it up")
    initial_label = ttk.Label(frame, text='Initial')
    initial_entry = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text='Rate of increase')
    rate_entry = ttk.Entry(frame, width=8)

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    led_picker_upper_button.grid(row=3, column=1)
    initial_label.grid(row=1, column=0)
    initial_entry.grid(row=2, column=0)
    rate_label.grid(row=1, column=2)
    rate_entry.grid(row=2, column=2)

    # Set the Button callbacks:
    led_picker_upper_button["command"] = lambda: handle_led_picker_upper(mqtt_sender, initial_entry,
                                                                         rate_entry)

    return frame


def handle_led_picker_upper(mqtt_sender, initial_entry, rate_entry):
    print("Picking up with LED.")
    mqtt_sender.send_message("led_picker_upper", [initial_entry.get(), rate_entry.get()])


def football_frame(window, mqtt_sender):
    frame = tkinter.Frame(window, borderwidth=100, bg='green')
    frame.grid()

    frame_label = ttk.Label(frame, text='Football Bot', font='Arial 18 bold', background='green')
    fumble_button = ttk.Button(frame, text='Recover the fumble!')
    juke_button = ttk.Button(frame, text='Juke Defender')
    celebrate_button = ttk.Button(frame, text='Celebrate the Touchdown')
    shake_button = ttk.Button(frame, text='Good game')

    frame_label.grid(row=0, column=1)
    fumble_button.grid(row=3, column=1)
    juke_button.grid(row=4, column=1)
    celebrate_button.grid(row=5, column=1)
    shake_button.grid(row=6, column=1)

    fumble_button["command"] = lambda: handle_fumble(mqtt_sender)
    juke_button["command"] = lambda: handle_juke(mqtt_sender)
    celebrate_button["command"] = lambda: handle_celebrate(mqtt_sender)
    shake_button["command"] = lambda: handle_shake(mqtt_sender)

    return frame


def handle_fumble(mqtt_sender):
    print("FUMBLE!")
    mqtt_sender.send_message('fumble')


def handle_juke(mqtt_sender):
    print('Get juked!')
    mqtt_sender.send_message('juke')


def handle_celebrate(mqtt_sender):
    print('Touchdown!!')
    mqtt_sender.send_message('celebration')


def handle_shake(mqtt_sender):
    print('Good game.')
    mqtt_sender.send_message('shake')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
