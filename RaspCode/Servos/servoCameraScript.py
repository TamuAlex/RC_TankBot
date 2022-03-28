from servoCamera import *
import websockets, asyncio, threading

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
Script that creates the connection with the AMQP server
and listen for messages about how the robot has to move.
Then, implementing the movement library, performs the
robot movement.

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
                
                # If the message is intended for this script (it starts with c)
                if message[0]=="c":
                    print("Entra")
                    #If it is a stop instruction
                    if message[2]=="s":
                        #A new thread is created and started, calling the stop function with the parameter of the movement
                        threading.Thread(target=sc.stop, args=(message[3:-1],)).start()
                        
                    #If is a moving option, a thread is created and started, calling the proper moving 
                    else:
                        func = getattr(sc, message[2:-1])
                        threading.Thread(target=func, daemon=True).start()

                
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
    sc = ServoCamera()
    asyncio.run(receive())

       