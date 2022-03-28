import subprocess
import os
import signal

mv=subprocess.Popen(['python3', '/home/pi/RaspCode/motors/movementScript.py'])
sc=subprocess.Popen(['python3', '/home/pi/RaspCode/Servos/servoCameraScript.py'])
sa=subprocess.Popen(['python3', '/home/pi/RaspCode/Servos/servoArmScript.py'])
streaming=subprocess.Popen(['python3','/home/pi/RaspCode/CameraStream/streaming.py'])

key=input("")
if key=="k":
   mv.kill()
   sc.kill()
   sa.kill()
   streaming.kill()
   
