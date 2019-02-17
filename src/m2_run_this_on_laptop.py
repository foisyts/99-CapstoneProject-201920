"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Thomas Hoevener.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


# def main():
#     """
#     This code, which must run on a LAPTOP:
#       1. Constructs a GUI for my part of the Capstone Project.
#       2. Communicates via MQTT with the code that runs on the EV3 robot.
#     """
#     # -------------------------------------------------------------------------
#     # Construct and connect the MQTT Client:
#     # -------------------------------------------------------------------------
#     mqtt_sender = com.MqttClient()
#     mqtt_sender.connect_to_ev3()
#
#     # -------------------------------------------------------------------------
#     # The root TK object for the GUI:
#     # -------------------------------------------------------------------------
#     root = tkinter.Tk()
#     root.title("CSSE 120 Capstone Project, Winter 2018-19")
#
#     # -------------------------------------------------------------------------
#     # The main frame, upon which the other frames are placed.
#     # -------------------------------------------------------------------------
#     main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
#     main_frame.grid()
#
#     # -------------------------------------------------------------------------
#     # Sub-frames for the shared GUI that the team developed:
#     # -------------------------------------------------------------------------
#     teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, increasing_tone_picker_upper_frame = get_shared_frames(
#         main_frame,
#         mqtt_sender)
#
#     # -------------------------------------------------------------------------
#     # Frames that are particular to my individual contributions to the project.
#     # -------------------------------------------------------------------------
#
#     # -------------------------------------------------------------------------
#     # Grid the frames.
#     # -------------------------------------------------------------------------
#     grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame,
#                 increasing_tone_picker_upper_frame)
#
#     # -------------------------------------------------------------------------
#     # The event loop:
#     # -------------------------------------------------------------------------
#     root.mainloop()
#
#
# def get_shared_frames(main_frame, mqtt_sender):
#     teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
#     arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
#     control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
#     drive_system_frame = shared_gui.get_drive_system_frame(main_frame, mqtt_sender)
#     sound_system_frame = shared_gui.get_sound_system_frame(main_frame, mqtt_sender)
#     increasing_tone_picker_upper_frame = get_tommys_frame(main_frame, mqtt_sender)
#
#     return teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, increasing_tone_picker_upper_frame
#
#
# def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame,
#                 increasing_tone_picker_upper_frame):
#     teleop_frame.grid(row=0, column=0)
#     arm_frame.grid(row=1, column=0)
#     control_frame.grid(row=2, column=0)
#     drive_system_frame.grid(row=0, column=1)
#     sound_system_frame.grid(row=1, column=1)
#     increasing_tone_picker_upper_frame.grid(row=0, column=2)
#
#
# def get_tommys_frame(window, mqtt_sender):
#     # Construct the frame to return:
#     frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#     frame.grid()
#
#     # Construct the widgets on the frame:
#     frame_label = ttk.Label(frame, text="Tommy's Frame", font='Arial 14 bold')
#     tone_picker_upper_button = ttk.Button(frame, text="Pick it up annoyingly")
#     initial_frequency_label = ttk.Label(frame, text='Initial frequency')
#     initial_frequency_entry = ttk.Entry(frame, width=8)
#     rate_label = ttk.Label(frame, text='Rate of increase')
#     rate_entry = ttk.Entry(frame, width=8)
#
#     # Grid the widgets:
#     frame_label.grid(row=0, column=1)
#     tone_picker_upper_button.grid(row=3, column=1)
#     initial_frequency_label.grid(row=1, column=0)
#     initial_frequency_entry.grid(row=2, column=0)
#     rate_label.grid(row=1, column=2)
#     rate_entry.grid(row=2, column=2)
#
#     # Set the Button callbacks:
#     tone_picker_upper_button["command"] = lambda: handle_tone_picker_upper(mqtt_sender, initial_frequency_entry,
#                                                                            rate_entry)
#
#     return frame
#
#     # #######################################################
#     # Write all the handlers down here
#     # #######################################################
#
#
# def handle_tone_picker_upper(mqtt_sender, initial_frequency_entry, rate_entry):
#     print("Picking up with tones.", "Starting tone at max distance:", int(initial_frequency_entry.get()),
#           "Rate of increase:",
#           int(rate_entry.get()))
#
#     mqtt_sender.send_message("tone_picker_upper", [initial_frequency_entry.get(), rate_entry.get()])


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Sprint 3 GUI created here
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def main():
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Cooking Assistant 3000")
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()
    introduction_frame = get_introduction_frame(main_frame, mqtt_sender)
    grid_frames(introduction_frame)
    root.mainloop()


def get_introduction_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Welcome to Cooking Assistant 3000!", font='Times')
    v = tkinter.IntVar()
    v.set(1)
    radiobutton1 = tkinter.Radiobutton(frame, text="button 1", variable=v, value=2)
    radiobutton2 = tkinter.Radiobutton(frame, text="button 2", variable=v, value=2)
    radiobutton1.grid(row=1)
    radiobutton2.grid(row=2)
    # radiobutton1.pack(row=1)
    # radiobutton2.pack(row=2)
    # tone_picker_upper_button = ttk.Button(frame, text="Pick it up annoyingly")
    # initial_frequency_label = ttk.Label(frame, text='Initial frequency')
    # initial_frequency_entry = ttk.Entry(frame, width=8)
    # rate_label = ttk.Label(frame, text='Rate of increase')
    # rate_entry = ttk.Entry(frame, width=8)

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    # tone_picker_upper_button.grid(row=3, column=1)
    # initial_frequency_label.grid(row=1, column=0)
    # initial_frequency_entry.grid(row=2, column=0)
    # rate_label.grid(row=1, column=2)
    # rate_entry.grid(row=2, column=2)

    # Set the Button callbacks:
    # tone_picker_upper_button["command"] = lambda: handle_tone_picker_upper(mqtt_sender, initial_frequency_entry,
    #                                                                        rate_entry)
    # radiobutton1["command"] = lambda: handle_radiobutton1(mqtt_sender, radiobutton1.get())
    # radiobutton2["command"] = print('b2 girl')

    return frame


def grid_frames(introduction_frame):
    introduction_frame.grid()


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
