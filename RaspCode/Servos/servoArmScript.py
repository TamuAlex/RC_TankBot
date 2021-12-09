import pika, os, logging, re
from servoArm import *
import threading


'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Script that creates the connection with the AMQP server
and listen for messages about how the arm servos have to move.
Then, implementing the movement library, performs the
arm servos movement.

This is all done withh mutithreading, to perform each movent independently,
and allow for the arm to move more than one servo at a time.
'''


#Connects to the AMQP broker
url = os.environ.get('CLOUDAMQP_URL', 'amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel

#A movement object is created
sa = ServoArmMovement()

while True:
    
    for method_frame, properties, body in channel.consume("ClawServos"):
        #The message is any combination of the following letters, indicating the movvement:
        # u -> for moving up
        # d -> for moving down
        # s -> for stopping
        # An the following, indicating the servos:
        # S1 -> The first servo, the one closer to the robot chasis
        # S2 -> The second servo
        # SR -> The robot servo
        # SP -> The claw servo
        
        #For example: b'uS1'
        #The string is parsed to know which function and which parameters are needed
        body=str(body)
        #print(body)
        if body[2]=="s":
            threading.Thread(target=sa.stop, args=(body[3:-1],)).start()
        elif body[2]=="u":
            threading.Thread(target=sa.up, args=(body[3:-1],)).start()
        else:
            threading.Thread(target=sa.down, args=(body[3:-1],)).start()
            
            