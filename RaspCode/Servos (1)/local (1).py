import pika, os, logging, re
from servoCamera import *
import threading

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Script that creates the connection with the AMQP server
and listen for messages about how the camera servos have to move.
Then, implementing the movement library, performs the
camera servos movement.

This is all done withh mutithreading, to perform each movent independently,
and allow the camera to move in two directions at the same time.
'''



#A movement object is created
sc = ServoCamera()

contador=0

while True:
    
    #Checks for new messages in the queue
 
        #Eight different body mesagges possible (controlled by code on the unity project):
        # b'up'
        # b'down'
        # b'left'
        # b'right'
        # The previous ones, preceded by an s, indicating "stop" (e.g.: b'sup')
        
        #We get the string between '' to call the function with the same name
    body=input("Mete ")
    body=str(body)
    body="b'"+body+"'"

        
        #If it is a stop instruction
    if body[2]=="s":
            #A new thread is created and started, calling the stop function with the parameter of the movement
        threading.Thread(target=sc.stop, args=(body[3:-1],)).start()
            
        #If is a moving option, a thread is created and started, calling the proper moving 
    else:
        func = getattr(sc, body[2:-1])
        threading.Thread(target=func, daemon=True).start()