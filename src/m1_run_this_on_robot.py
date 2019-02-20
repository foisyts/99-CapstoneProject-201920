"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Tristen Foisy.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
import m1_extra as m1

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # camera_tester()
    real_thing()

def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    # m1.drive_and_beep_with_ir(2, 5)

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            # if robot...:
            #     mqtt_receiver.send_message('function_name')
            break


def camera_tester():
    robot = rosebot.RoseBot()
    robot.drive_system.display_camera_data()


def m2_feature_9():
    robot = rosebot.RoseBot()





# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()