from movement import *
import websockets, asyncio

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

(See Github for how the messages format should be)
'''
async def receive():

    #First of all, the IP of the WebSocket server to which the script connects is declared
    uri = "ws://172.24.50.15:8765"
    
    async with websockets.connect(uri) as websocket:
        while True:
            #First of all, it waits until a message is recieved
            message = (await websocket.recv())

            #Checks if the message is meant for the robot movement (It starts with an "m")
            if message[0]=="m":

                #If is a moving option, a thread is created and started, calling the proper moving 
                func = getattr(mv, str(message)[2:-1])
                func()
            
if __name__ == "__main__":
    mv = Movement()
    asyncio.run(receive())

        