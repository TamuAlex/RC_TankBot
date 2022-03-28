from movement import *
import websockets, asyncio
import unittest
import sys 
sys.path.append("/home/pi/RaspCode/utils") 

from CustomizedExceptions import * 
'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Script that creates the connection with the WebSocket server
and listen for messages about how the robot has to move.
Then, implementing the movement library, performs the
robot movement.

More information about what kind of messages does this script recieve in the github project
'''
async def receive():

    # Url of the WebSocket server
    uri = "ws://172.24.50.15:8765"
    
    async for websocket in websockets.connect(uri):
        try:
            while True:
                
                # Receive a message
                message = (await websocket.recv())
                
                # If the message is intended for this script (it starts with m)
                if message[0]=="m":

                    # Checks which function does it need to execute, and execute it
                    func = getattr(mv, str(message)[2:-1])
                    func()

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
    mv = Movement()
    asyncio.run(receive())

        