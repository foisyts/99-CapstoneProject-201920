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


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    delegate = delegate_on_laptop()
    mqtt_sender = com.MqttClient(delegate)
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
    # teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame = get_shared_frames(
    #     main_frame,
    #     mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    mario_kart = mario_kart_120_window(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_system_frame, feature_9_frame)

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


def mario_kart_120_window(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    title_label = ttk.Label(frame, text="---------- Mario Kart 120 ----------", font='Arial 13 bold')
    title_image = title_picture(frame)
    start_button = ttk.Button(frame, text='Start Game!')
    blank_label = ttk.Label(frame, text='')

    title_label.grid(row=0, column=0)
    title_image.grid(row=1, column=0)
    blank_label.grid(row=2, column=0)
    start_button.grid(row=3, column=0)

    start_button["command"] = lambda: course_selection(frame, window, mqtt_sender)
    return frame


def title_picture(window):
    path = 'mario_kart_title.gif'
    img = tkinter.PhotoImage(file=path)
    panel = ttk.Label(window, image=img)
    panel.image = img

    return panel


def course_selection(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    title_label = ttk.Label(frame, text="--- Choose a Racetrack ---", font='Arial 13 bold')

    title_label.grid(row=0, column=1)
    get_course_displays(frame)
    get_radiobuttons(frame, window, mqtt_sender)

    return frame


def get_course_displays(window):
    path_rainbow = 'rainbowroad_display.gif'
    path_koopa = 'koopatroopa_display.gif'
    path_bowser = 'Bowserscastlen64_display.gif'
    img_rainbow = tkinter.PhotoImage(file=path_rainbow)
    panel_rainbow = ttk.Label(window, image=img_rainbow)
    panel_rainbow.image = img_rainbow
    img_koopa = tkinter.PhotoImage(file=path_koopa)
    panel_koopa = ttk.Label(window, image=img_koopa)
    panel_koopa.image = img_koopa
    img_bowser = tkinter.PhotoImage(file=path_bowser)
    panel_bowser = ttk.Label(window, image=img_bowser)
    panel_bowser.image = img_bowser
    grid_courses(panel_koopa, panel_bowser, panel_rainbow)


def grid_courses(course1, course2, course3):
    course1.grid(row=1, column=0)
    course2.grid(row=1, column=1)
    course3.grid(row=1, column=2)


def get_radiobuttons(window, big_window, mqtt_sender):
    radio_observer = tkinter.StringVar()
    radio_1 = ttk.Radiobutton(window, value='koopa')
    radio_2 = ttk.Radiobutton(window, value='bowser')
    radio_3 = ttk.Radiobutton(window, value='rainbow')
    race_button = ttk.Button(window, text="Let's Race!")
    create_course_labels(window)
    grid_radiobuttons(radio_1, radio_2, radio_3)
    empty_label(window)

    for radio in [radio_1, radio_2, radio_3]:
        radio['variable'] = radio_observer

    race_button.grid(row=5, column=1)

    race_button["command"] = lambda: race_time(window, big_window, radio_observer.get(), mqtt_sender)


def grid_radiobuttons(radio_1, radio_2, radio_3):
    radio_1.grid(row=3, column=0)
    radio_2.grid(row=3, column=1)
    radio_3.grid(row=3, column=2)


def create_course_labels(window):
    koopa_label = ttk.Label(window, text='Koopa Troopa Beach')
    bowser_label = ttk.Label(window, text="Bowser's Castle")
    rainbow_label = ttk.Label(window, text='Rainbow Road')
    koopa_label.grid(row=2, column=0)
    bowser_label.grid(row=2, column=1)
    rainbow_label.grid(row=2, column=2)


def empty_label(window):
    empty_label = ttk.Label(window, text='')
    empty_label.grid(row=4, column=1)


def feature_9_movement(mqtt_sender, initial_entry, rate_of_increase_entry):
    print("test")
    mqtt_sender.send_message("beeper_picker_upper", [initial_entry.get(), rate_of_increase_entry.get()])


def race_time(window, big_window, radio_observer, mqtt_sender):
    observer = radio_observer
    if observer == 'koopa':
        create_koopa_track(window, big_window, mqtt_sender)
    elif observer == 'bowser':
        create_bowser_track(window, big_window, mqtt_sender)
    elif observer == 'rainbow':
        create_rainbow_track(window, big_window, mqtt_sender)
    else:
        print('Choose a racetrack!')


def create_bowser_track(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    img_track = tkinter.PhotoImage(file='bowserscastle_track.gif')
    panel_track = ttk.Label(window, image=img_track)
    panel_track.image = img_track

    bowser_label = ttk.Label(window, text="----Bowser's Castle----", font='Arial 13 bold')
    go_button = ttk.Button(window, text='GO!')
    bowser_label.grid(row=0, column=0)
    panel_track.grid(row=1, column=0)
    go_button.grid(row=2, column=0)
    go_button["command"] = lambda: start_driving('bowser', mqtt_sender)


def create_rainbow_track(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    img_track = tkinter.PhotoImage(file='rainbowroad_track.gif')
    panel_track = ttk.Label(window, image=img_track)
    panel_track.image = img_track

    rainbow_label = ttk.Label(window, text="----Rainbow Road----", font='Arial 13 bold')
    go_button = ttk.Button(window, text='GO!')
    rainbow_label.grid(row=0, column=0)
    panel_track.grid(row=1, column=0)
    go_button.grid(row=2, column=0)
    go_button["command"] = lambda: start_driving('rainbow', mqtt_sender)


def create_koopa_track(last_frame, window, mqtt_sender):
    last_frame.destroy()
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    img_track = tkinter.PhotoImage(file='koopatroopa_track.gif')
    panel_track = ttk.Label(window, image=img_track)
    panel_track.image = img_track

    koopa_label = ttk.Label(window, text="----Koopa Troopa Beach----")
    go_button = ttk.Button(window, text='GO!')
    koopa_label.grid(row=0, column=0)
    panel_track.grid(row=1, column=0)
    go_button.grid(row=2, column=0)
    go_button["command"] = lambda: start_driving('koopa', mqtt_sender)


def start_driving(sent_value, mqtt_sender):
    if sent_value == 'koopa':
        # print(sent_value)
        mqtt_sender.send_message("drive_koopa")
    if sent_value == 'bowser':
        # print(sent_value)
        mqtt_sender.send_message("drive_bowser")
    if sent_value == 'rainbow':
        # print(sent_value)
        mqtt_sender.send_message("drive_rainbow")


class delegate_on_laptop(object):
    def function_name(self):
        print('a')

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
