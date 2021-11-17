import pika, os, logging, re
from servoArmMov import *
import threading

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
        #Four different body mesagges possible (controlled by code on the unity project):
        # b'up'
        # b'down'
        # b'left'
        # b'right'
        # b'sup'
        #We get the string between '' to call the function with the same name
        body=str(body)
        #print(body)
        if body[2]=="s":
            threading.Thread(target=sa.stop, args=(body[3:-1],)).start()
        elif body[2]=="u":
            threading.Thread(target=sa.up, args=(body[3:-1],)).start()
        else:
            threading.Thread(target=sa.down, args=(body[3:-1],)).start()
            
            