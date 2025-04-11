from TMC_2209.TMC_2209_StepperDriver import * 
import math
import servo_control as sc

tmc1 = TMC_2209(16,20,21,250000,driver_address=1,)
tmc2 = TMC_2209(8,7,1,250000,driver_address=0)

min_steps = 0
max_steps = 5850

average_speed = 1000

driver_list = [tmc1, tmc2]

def setup():
    for tmc in driver_list:
        tmc.tmc_logger.loglevel = Loglevel.DEBUG
        tmc.movement_abs_rel = MovementAbsRel.ABSOLUTE 
        tmc.set_direction_reg(False)
        tmc.set_interpolation(True)
        tmc.set_spreadcycle(True)
        tmc.set_microstepping_resolution(8)
        tmc.set_internal_rsense(False)
        tmc.set_acceleration_fullstep(500)
        tmc.set_max_speed_fullstep(average_speed)
        tmc.set_motor_enabled(True)
        tmc.set_current_position(0)

    tmc1.set_current(900)
    tmc2.set_current(500)

def make_diamond():
    tmc1.run_to_position_steps(max_steps/2, MovementAbsRel.RELATIVE)
    time.sleep(1)

    for i in range(4):
        if i == 0:
            tmc1.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
            tmc2.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
        elif i == 1:
            tmc1.run_to_position_steps_threaded(-max_steps/2,MovementAbsRel.RELATIVE)
            tmc2.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
        elif i == 2:
            tmc1.run_to_position_steps_threaded(-max_steps/2,MovementAbsRel.RELATIVE)
            tmc2.run_to_position_steps_threaded(-max_steps/2,MovementAbsRel.RELATIVE)
        elif i == 3:
            tmc1.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
            tmc2.run_to_position_steps_threaded(-max_steps/2,MovementAbsRel.RELATIVE)
        tmc1.wait_for_movement_finished_threaded()
        tmc2.wait_for_movement_finished_threaded()

    tmc1.run_to_position_steps(-max_steps/2, MovementAbsRel.RELATIVE)

def make_circle():
    tmc1.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
    tmc2.run_to_position_steps_threaded(max_steps/2,MovementAbsRel.RELATIVE)
    tmc1.wait_for_movement_finished_threaded()
    tmc2.wait_for_movement_finished_threaded()
    last_x, last_y = 0, 0
    radius = 2000
    steps_per_circle = 360
    theta_increment = (2 * math.pi) / steps_per_circle

    for step in range(steps_per_circle):
        theta = step * theta_increment
        x_steps=int(radius*math.cos(theta))
        y_steps=int(radius*math.sin(theta))

        tmc1.run_to_position_steps_threaded(x_steps-last_x, MovementAbsRel.RELATIVE)
        tmc2.run_to_position_steps_threaded(y_steps-last_y, MovementAbsRel.RELATIVE)

        last_x = x_steps
        last_y = y_steps

        tmc1.wait_for_movement_finished_threaded()
        tmc2.wait_for_movement_finished_threaded()

def go_to_box(x_coord, y_coord):
    toggle = False
    x_step = int(max_steps / 3)
    y_step = int(max_steps / 3)

    goal_x_coord = x_step * x_coord
    goal_y_coord = y_step * y_coord

    distance_to_goal_x = int(goal_x_coord - tmc1.get_current_position())
    distance_to_goal_y = int(goal_y_coord - tmc2.get_current_position())

    print("distance x: ", distance_to_goal_x, "distance y: ", distance_to_goal_y)

    """ tmc1.run_to_position_steps(distance_to_goal_x, MovementAbsRel.RELATIVE)
    time.sleep(3)
    tmc2.run_to_position_steps(distance_to_goal_y, MovementAbsRel.RELATIVE)
    time.sleep(3) """

    tmc1.run_to_position_steps_threaded(distance_to_goal_x, MovementAbsRel.RELATIVE)
    tmc2.run_to_position_steps_threaded(distance_to_goal_y, MovementAbsRel.RELATIVE)

    tmc1.wait_for_movement_finished_threaded()
    tmc2.wait_for_movement_finished_threaded()
    
def reset():
    tmc1.set_motor_enabled(False)
    tmc2.set_motor_enabled(False)

if __name__ == "__main__":
    setup()

    for i in range(3):
        for j in range(3):
            go_to_box(j, i)
            time.sleep(1) 
    go_to_box(0,0)

    reset()

