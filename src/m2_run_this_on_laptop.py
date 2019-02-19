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
import m2_another_file as m2a
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
    bowl = m2a.Bowl
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()
    root = tkinter.Tk()
    root.title("Cooking Assistant 3000")
    main_frame1 = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame1.grid()
    get_introduction_frame(main_frame1, mqtt_sender, bowl)
    root.mainloop()


def get_introduction_frame(window, mqtt_sender, bowl):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Welcome to Cooking Assistant 3000!", font='Times 20')
    directions_label0 = ttk.Label(frame,
                                  text='Directions:')
    directions_label1 = ttk.Label(frame,
                                  text='Click the "Next Customer" button to get the next order.')
    directions_label2 = ttk.Label(frame,
                                  text='Then, you will see the ingredients you need to have the robot get.')
    directions_label3 = ttk.Label(frame,
                                  text='Next, click on the correct ingredient and the robot will get it.')
    directions_label4 = ttk.Label(frame,
                                  text='You have 3 minutes to complete the order!')
    directions_label5 = ttk.Label(frame,
                                  text='Or else, the customer will get angry and leave your shop!')
    directions_label6 = ttk.Label(frame,
                                  text='If you click the wrong ingredient, the robot will tell you so.')
    directions_label7 = ttk.Label(frame,
                                  text=' ')
    directions_label8 = ttk.Label(frame,
                                  text='...Click NEXT to continue...')
    next_button = ttk.Button(frame, text='NEXT')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    directions_label0.grid(row=1, column=0)
    directions_label1.grid(row=1, column=1)
    directions_label2.grid(row=2, column=1)
    directions_label3.grid(row=3, column=1)
    directions_label4.grid(row=4, column=1)
    directions_label5.grid(row=5, column=1)
    directions_label6.grid(row=6, column=1)
    directions_label7.grid(row=7, column=1)
    directions_label8.grid(row=4, column=2)
    next_button.grid(row=8, column=2)

    # Callback functions for the widgets
    next_button["command"] = lambda: get_game_frame(window, mqtt_sender, frame, bowl)

    frame.grid()


def get_game_frame(window, mqtt_sender, prev_frame, bowl):
    # Construct the frame to return:
    prev_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Ingredients", font='Times')
    quit_button = ttk.Button(frame, text='QUIT')
    v = tkinter.IntVar()
    v.set(1)
    flour_button = tkinter.Radiobutton(frame, text="Flour", variable=v, value=1, indicatoron=False, background='white')
    water_button = tkinter.Radiobutton(frame, text="Water", variable=v, value=2, indicatoron=False,
                                       background='light blue')
    yeast_button = tkinter.Radiobutton(frame, text="Yeast", variable=v, value=3, indicatoron=False,
                                       background='yellow')
    space_label1 = tkinter.ttk.Label(frame, text=' ')
    space_label2 = tkinter.ttk.Label(frame, text=' ')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_button.grid(row=4, column=1)
    flour_button.grid(row=2, column=0)
    water_button.grid(row=2, column=1)
    yeast_button.grid(row=2, column=2)
    space_label1.grid(row=1, column=1)
    space_label2.grid(row=3, column=1)

    # Set the Button callbacks:
    flour_button["command"] = lambda: handle_flour(mqtt_sender, 'white', bowl)
    water_button["command"] = lambda: handle_water(mqtt_sender, 'blue', bowl)
    yeast_button["command"] = lambda: handle_yeast(mqtt_sender, 'yellow', bowl)
    quit_button["command"] = lambda: window.quit()

    frame.grid()


# def get_recipe_frame(window, mqtt_sender, prev_frame):
#     # Construct the frame to return:
#     prev_frame.destroy()
#     frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
#     frame.grid()
#
#     # Construct the widgets on the frame:
#     frame_label = ttk.Label(frame, text="Ingredients", font='Times')
#     quit_button = ttk.Button(frame, text='QUIT')
#     v = tkinter.IntVar()
#     v.set(1)
#     flour_button = tkinter.Radiobutton(frame, text="Flour", variable=v, value=1, indicatoron=False, background='white')
#     water_button = tkinter.Radiobutton(frame, text="Water", variable=v, value=2, indicatoron=False,
#                                        background='light blue')
#     yeast_button = tkinter.Radiobutton(frame, text="Yeast", variable=v, value=3, indicatoron=False,
#                                        background='yellow')
#     space_label1 = tkinter.ttk.Label(frame, text=' ')
#     space_label2 = tkinter.ttk.Label(frame, text=' ')
#
#     # Grid the widgets:
#     frame_label.grid(row=0, column=1)
#     quit_button.grid(row=4, column=1)
#     flour_button.grid(row=2, column=0)
#     water_button.grid(row=2, column=1)
#     yeast_button.grid(row=2, column=2)
#     space_label1.grid(row=1, column=1)
#     space_label2.grid(row=3, column=1)
#
#     # Set the Button callbacks:
#     flour_button["command"] = lambda: handle_flour(mqtt_sender, 'white')
#     water_button["command"] = lambda: handle_water(mqtt_sender, 'blue')
#     yeast_button["command"] = lambda: handle_yeast(mqtt_sender, 'yellow')
#     quit_button["command"] = lambda: window.quit()
#
#     frame.grid()


########################################
# Handlers
########################################
def handle_flour(mqtt_sender, color, bowl):
    print('Getting flour now')
    mqtt_sender.send_message("grab_ingredient", [color, bowl])


def handle_water(mqtt_sender, color, bowl):
    print('Getting water now')
    mqtt_sender.send_message("grab_ingredient", [color, bowl])


def handle_yeast(mqtt_sender, color, bowl):
    print('Getting yeast now')
    mqtt_sender.send_message("grab_ingredient", [color, bowl])



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
