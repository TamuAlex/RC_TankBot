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
Script that creates the connection with the WebSocket server
and listen for messages about how the robot arm servos have to move.
Then, implementing the servoArm library, performs the
arm servos' movement.

More information about what kind of messages does this script recieve in the github project

'''
async def receive():
    # It connects to the WebSocket server url
    uri = "ws://172.24.50.15:8765"
    
    async for websocket in websockets.connect(uri):
        try:
            while True:
                    # Receive a message
                    message = (await websocket.recv())
                    
                    # If the message is intended for this script (it starts with a)
                    if message[0]=="a":

                        # Checks if it is intended to go up, down, or stop. Then it creates a subprocess for that movement
                        if message[2]=="s":
                            threading.Thread(target=sa.stop, args=(message[3:-1],)).start()
                        elif message[2]=="u":

                            threading.Thread(target=sa.up, args=(message[3:-1],)).start()
                        else:
                            threading.Thread(target=sa.down, args=(message[3:-1],)).start()

                    # If the message ask for the connection to close, it raises a custom exception
                    if message == "close":
                        raise CustomizedExceptions.ClosingNoticeError()     

        except websockets.ConnectionClosed:
            # If the server is down, waits until it can connect again
            continue
        
        except CustomizedExceptions.ClosingNoticeError:
            # If we ask for the script to finish, it closes the subprocess and exit
            break
                        
if __name__ == "__main__":
    sa = ServoArmMovement()
    asyncio.run(receive())

