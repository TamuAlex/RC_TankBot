import pika, os, logging, re
from servoCamera import *

#Connects to the AMQP broker
url = os.environ.get('CLOUDAMQP_URL', 'amqps://zvaqximc:I2_yD3JdVLcdqBIdH__EUToUUdEVSsWf@fish.rmq.cloudamqp.com/zvaqximc')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel

#A movement object is created
sc = ServoCamera()

while True:
    
    for method_frame, properties, body in channel.consume("CameraServos"):
        #Four different body mesagges possible (controlled by code on the unity project):
        # b'forward'
        # b'back'
        # b'left'
        # b'right'
        # b'stop'
        #We get the string between '' to call the function with the same name
        body=str(body)
        print(body)
        if body[2]=="s":
            sc.stop(body[3:-1])
        else:
            func = getattr(sc, body[2:-1])
            func()
        