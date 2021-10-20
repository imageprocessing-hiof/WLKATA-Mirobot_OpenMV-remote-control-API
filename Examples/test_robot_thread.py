# Execute Mirobot Homing parallelly using Threading

import r2 as rem
import time
import threading

bot1 = rem.remote_control()
bot2 = rem.remote_control()

Flag_robot_one_finished = False
Flag_robot_two_finished = False

def moveRobot_one():
    Flag_robot_one_finished = False
    print("starting Robot 1")
    move_status = bot1.init_robot(bot1.MIROBOT_ONE_PORT)
    print(move_status)
    Flag_robot_one_finished = True
    
def moveRobot_two():
    Flag_robot_two_finished = False
    print("starting Robot 2")
    move_status = bot2.init_robot(bot2.MIROBOT_TWO_PORT)
    print(move_status)
    Flag_robot_two_finished = True
    

# the main function
thread_1 = threading.Thread(target=moveRobot_one)
thread_2 = threading.Thread(target=moveRobot_two)
thread_1.start()
thread_2.start()



