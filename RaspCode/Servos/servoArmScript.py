from servoArm import *
import websockets, asyncio
import threading

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Script that creates the connection with the WebSocket server
and listen for messages about how the robot has to move.
Then, implementing the servoArm library, performs the
arm movements.

(See Github for how the messages format should be)
'''
async def receive():

    #First of all, the IP of the WebSocket server to which the script connects is declared
    uri = "ws://172.24.50.15:8765"
    
    async with websockets.connect(uri) as websocket:
        while True:

            #First of all, it waits until a message is recieved
            message = (await websocket.recv())
            
            #Checks if the message is meant for the arm movement (It starts with an "a")
            if message[0]=="a":

                #Checks if is an stop message
                if message[2]=="s":
                    threading.Thread(target=sa.stop, args=(message[3:-1],)).start()

                #If not, checks if is an "up" message    
                elif message[2]=="u":

                    threading.Thread(target=sa.up, args=(message[3:-1],)).start()
                else:

                    #If not, it should be a "down" message
                    threading.Thread(target=sa.down, args=(message[3:-1],)).start()
                
if __name__ == "__main__":
    sa = ServoArmMovement()
    asyncio.run(receive())

