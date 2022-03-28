import websockets, asyncio
import subprocess
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
that waits for a connection, and keeps listening to know when 
to start or stop the video streaming service
'''


async def receive():

    # Url of the WebSocket server
    uri = "ws://172.24.50.15:8765"
    flag = False
    async for websocket in websockets.connect(uri):
        try:

            while True:
                    # Receive a message
                    message = (await websocket.recv())

                    # If the message is intended for this script (It starts with s)
                    if message[0]=="s":

                        # Checks if it has to start or stop the camera stream, and creates or kills a subprocess with that job
                        if message[2:7]=="start" and not flag:
                            flag = True
                            stream=subprocess.Popen(["./rtsp-simple-server"])
                        if message[2:6]=="stop" and flag:
                            stream.kill()
                            flag = False
                    
                    # If the message ask for the connection to close, it raises a custom exception
                    if message == "close":
                        raise CustomizedExceptions.ClosingNoticeError()

        except websockets.ConnectionClosed:
            # If the server is down, waits until it can connect again
            continue
        
        except CustomizedExceptions.ClosingNoticeError:
            # If we ask for the script to finish, it closes the subprocess and exit
            if flag:
                stream.kill()
            break
if __name__ == "__main__":
    asyncio.run(receive())
