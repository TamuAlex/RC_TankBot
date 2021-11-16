import pika, os, logging, re
from servoCamera import *
import threading

sc = ServoCamera()
while True:
    
    body=input("Mete")
    body="b'"+str(body)+"'"
    print(body)
    if body[2]=="s":
        
        hilo=threading.Thread(target=sc.stop, args=(body[3:-1],))
        hilo.start()
        print("Recibido el stop")
    else:
        func = getattr(sc, body[2:-1])
        hilo=threading.Thread(target=func, daemon=True)
        hilo.start()
        
        print("Recibido la funcion")
        
    print(sc)
