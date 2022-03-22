from servoCamera import *
import websockets, asyncio, threading



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
    
    async with websockets.connect(uri) as websocket:
        
        while True:
            message = (await websocket.recv())
            print(message)
            
            if message[0]=="c":
                print("Entra")
                #If it is a stop instruction
                if message[2]=="s":
                    #A new thread is created and started, calling the stop function with the parameter of the movement
                    threading.Thread(target=sc.stop, args=(message[3:-1],)).start()
                    
                #If is a moving option, a thread is created and started, calling the proper moving 
                else:
                    func = getattr(sc, message[2:-1])
                    print(str(func))
                    threading.Thread(target=func, daemon=True).start()
                
if __name__ == "__main__":
    sc = ServoCamera()
    asyncio.run(receive())

       