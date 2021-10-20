# Execute Mirobot Homing using ASYNCIO, executes one at a time

import r2 as rem
import time
import asyncio

bot1 = rem.remote_control()
bot2 = rem.remote_control()

Flag_robot_one_finished = False
Flag_robot_two_finished = False

async def move_robot(mirobot_id):
    if(mirobot_id == 1):
        print("starting Robot 1")
        move_status = bot1.init_robot(bot1.MIROBOT_ONE_PORT)
    elif(mirobot_id == 2):
        print("starting Robot 2")
        move_status = bot2.init_robot(bot2.MIROBOT_TWO_PORT)
    return move_status

async def moveRobot_one():
    Flag_robot_one_finished = False
    print("moveRobot_one")
    move_status = await move_robot(1)
    print(move_status)
    Flag_robot_one_finished = True
    
async def moveRobot_two():
    Flag_robot_two_finished = False
    print("moveRobot_two")
    move_status = await move_robot(2)
    print(move_status)
    Flag_robot_two_finished = True
    

async def runBoth():
    task_1 = asyncio.create_task(moveRobot_one())
    task_2 = asyncio.create_task(moveRobot_two())
    await task_1
    await task_2

asyncio.run(runBoth())


