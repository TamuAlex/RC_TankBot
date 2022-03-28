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
                print(message)
                if message[0]=="m":
                    func = getattr(mv, str(message)[2:-1])
                    func()
                if message == "close":
                        raise CustomizedExceptions.ClosingNoticeError()  
        except websockets.ConnectionClosed:
            continue
        
        except CustomizedExceptions.ClosingNoticeError:
            break                 
if __name__ == "__main__":
    mv = Movement()
    asyncio.run(receive())

        