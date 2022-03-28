import websockets, asyncio
import subprocess
import unittest
import sys 
sys.path.append("/home/pi/RaspCode/utils") 

from CustomizedExceptions import * 


async def receive():
    uri = "ws://172.24.50.15:8765"
    flag = False
    async for websocket in websockets.connect(uri):
        try:

            while True:
                    message = (await websocket.recv())
                    if message[0]=="s":
                        if message[2:7]=="start" and not flag:
                            flag = True
                            stream=subprocess.Popen(["./rtsp-simple-server"])
                        if message[2:6]=="stop" and flag:
                            stream.kill()
                            flag = False
                    if message == "close":
                        raise CustomizedExceptions.ClosingNoticeError()

        except websockets.ConnectionClosed:
            continue
        
        except CustomizedExceptions.ClosingNoticeError:
            if flag:
                stream.kill()
            break
if __name__ == "__main__":
    asyncio.run(receive())
