from servoArm import *
import websockets, asyncio
import threading

import unittest
import sys 
sys.path.append("/home/pi/RaspCode/utils") 

from CustomizedExceptions import * 
#from ...utils import CustomizedExceptions
'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Script that creates the connection with the AMQP server
and listen for messages about how the robot has to move.
Then, implementing the movement library, performs the
robot movement.
'''
async def receive():
    uri = "ws://172.24.50.15:8765"
    
    async for websocket in websockets.connect(uri):
        try:
            while True:
                    message = (await websocket.recv())
                    
                    if message[0]=="a":
                        if message[2]=="s":
                            threading.Thread(target=sa.stop, args=(message[3:-1],)).start()
                        elif message[2]=="u":

                            threading.Thread(target=sa.up, args=(message[3:-1],)).start()
                        else:
                            threading.Thread(target=sa.down, args=(message[3:-1],)).start()
                    if message == "close":
                        raise CustomizedExceptions.ClosingNoticeError()        
        except websockets.ConnectionClosed:
            continue
        
        except CustomizedExceptions.ClosingNoticeError:
            break
                        
if __name__ == "__main__":
    sa = ServoArmMovement()
    asyncio.run(receive())

