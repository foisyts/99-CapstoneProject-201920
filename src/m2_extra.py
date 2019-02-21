import rosebot
import time
import m2_another_file as m2a
import mqtt_remote_method_calls as com


def run_test_pick_up_with_tones(initial_frequency, rate):
    robot = rosebot.RoseBot()
    # robot.arm_and_claw.calibrate_arm()
    speed = 50
    robot.drive_system.go(speed, speed)
    max_freq = (initial_frequency + 19 * rate) * 2
    while True:
        d = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        robot.sound_system.tone(100, max_freq - 2 * d * rate)
        print(max_freq - d * rate)
        time.sleep(0.2)
        if d <= 2:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


############################################################
############################################################
# Sprint 3 personal project
############################################################
############################################################


##############################################
# Movement functions
##############################################

def go_to_floor_color_and_turn(robot, color):
    # Robot goes to the correct "ingredient" color mat
    #   located on the floor using the color sensor
    #   then turns 90 degrees counterclockwise to position
    #   itself toward the correct pile of ingredients.
    # Sensors: color sensor
    speed = 60
    robot.drive_system.go_straight_until_color_is(color, speed)
    # go_until_color(robot, color)
    turn_90_degrees_counterclockwise(robot)


def go_and_pick_up_the_ingredient(robot):
    # Goes to pile of ingredients and grabs it
    # Sensors: encoder, touch, IR
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go_until_distance_is_within(0.5, 1, 50)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(3, -30)
    turn_90_degrees_counterclockwise(robot)


def go_and_place_ingredient_in_bowl(robot, ingredient_distance):
    # Goes to bowl and drops ingredient
    # Sensors: encoder
    robot.drive_system.go_straight_for_inches_using_encoder(ingredient_distance, 50)
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(3, -30)
    turn_90_degrees_counterclockwise(robot)


def return_to_origin(robot):
    # Returns the robot to the original starting spot
    # Sensors: encoder
    robot.drive_system.go_straight_for_inches_using_encoder(10, 50)
    turn_90_degrees_counterclockwise(robot)
    robot.drive_system.go_straight_for_inches_using_encoder(3, -30)


##############################################
# Mini-functions used in movement functions
##############################################

def determine_ingredient_distance(color):
    # Determines distance needed for encoder
    #   in go_and_place_ingredient_in_bowl function
    ingredient_distance = 5
    if color == 'Red':
        ingredient_distance = 10
    elif color == 'Blue':
        ingredient_distance = 15
    elif color == 'White':
        ingredient_distance = 20
    return ingredient_distance


def turn_90_degrees_counterclockwise(robot):
    # Turns the robot by 90 degrees counterclockwise
    robot.drive_system.go(-50, 50)
    time.sleep(1.6)
    robot.drive_system.stop()


###############################################
# Other
###############################################

def return_information(r, bowl):
    print("sending info back to the laptop now")
    r.send_message("get_bowl", [bowl.water_count, bowl.flour_count, bowl.yeast_count])


###############################################
# Main function
###############################################

def lets_get_this_bread(color, yeast_count, water_count, flour_count, r):
    # this is the main function that runs the whole movement and checking values
    robot = rosebot.RoseBot()
    bowl = m2a.Bowl()
    bowl.yeast_count = int(yeast_count)
    bowl.water_count = int(water_count)
    bowl.flour_count = int(flour_count)
    bowl.add_to_the_bowl(color)
    ingredient_distance = determine_ingredient_distance(color)
    robot.sound_system.speak('Coming right up!')
    go_to_floor_color_and_turn(robot, color)
    go_and_pick_up_the_ingredient(robot)
    go_and_place_ingredient_in_bowl(robot, ingredient_distance)
    return_to_origin(robot)
    return_information(r, bowl)
