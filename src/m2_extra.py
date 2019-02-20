import rosebot
import time
import m2_another_file as m2a


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
    speed = 70
    robot.drive_system.go_straight_until_color_is(color, speed)
    turn_90_degrees_counterclockwise(robot)


def go_and_pick_up_the_ingredient(robot):
    # Goes to pile of ingredients and grabs it
    # Sensors: encoder, touch, IR
    robot.drive_system.go_until_distance_is_within(0.5, 2, 60)
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go_straight_for_inches_using_encoder(7, -30)
    turn_90_degrees_counterclockwise(robot)


def go_and_place_ingredient_in_bowl(robot, ingredient_distance):
    # Goes to bowl and drops ingredient
    # Sensors: encoder
    robot.drive_system.go_straight_for_inches_using_encoder(ingredient_distance, 50)
    robot.arm_and_claw.lower_arm()
    turn_90_degrees_counterclockwise(robot)


def return_to_origin(robot):
    # Returns the robot to the original starting spot
    # Sensors: IR
    robot.drive_system.go_until_distance_is_within(0.1, 4, 70)
    turn_90_degrees_counterclockwise(robot)


##############################################
# Mini-functions used in movement functions
##############################################

def determine_ingredient_distance(color):
    # Determines distance needed for encoder
    #   in go_and_place_ingredient_in_bowl function
    ingredient_distance = 10
    if color is 'pink':
        ingredient_distance = 10
    elif color is 'yellow':
        ingredient_distance = 20
    elif color is 'blue':
        ingredient_distance = 30
    return ingredient_distance


def turn_90_degrees_counterclockwise(robot):
    # Turns the robot by 90 degrees counterclockwise
    robot.drive_system.go(-30, 30)
    time.sleep(1)
    # need to figure out accurate time sleep based on speed given
    robot.drive_system.stop()


def check_if_done(bowl):
    if bowl.yeast_count == 1 and bowl.flour_count == 1 and bowl.water_count == 1:
        return 'bread'
    elif bowl.yeast_count == 0 and bowl.flour_count == 0 and bowl.water_count == 3:
        return 'water'
    elif bowl.yeast_count == 1 and bowl.flour_count == 0 and bowl.water_count == 0:
        return 'fake sugar'
    elif bowl.yeast_count > 3 or bowl.flour_count > 3 or bowl.water_count > 3:
        return 'failure'
    else:
        return False


###############################################
# Main function
###############################################

def lets_get_this_bread(color, yeast_count, water_count, flour_count):
    robot = rosebot.RoseBot()
    bowl = m2a.Bowl
    bowl.yeast_count = int(yeast_count)
    bowl.water_count = int(water_count)
    bowl.flour_count = int(flour_count)
    bowl.add_to_the_bowl(color)
    ingredient_distance = determine_ingredient_distance(color)
    robot.sound_system.speak('Coming right up! Just let me calibrate my arm first!')
    robot.arm_and_claw.calibrate_arm()
    robot.sound_system.speak('All done')
    go_to_floor_color_and_turn(robot, color)
    go_and_place_ingredient_in_bowl(robot, ingredient_distance)
    return_to_origin(robot)
    check_if_done(bowl)
