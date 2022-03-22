import subprocess
import os
import signal


#Launches all three motors and servos scripts in three different threads, for them to work concurrently
mv=subprocess.Popen(['python3', '/home/pi/RaspCode/motors/movementScript.py'])
sc=subprocess.Popen(['python3', '/home/pi/RaspCode/Servos/servoCameraScript.py'])
sa=subprocess.Popen(['python3', '/home/pi/RaspCode/Servos/servoArmScript.py'])

#Press "k" if we want to stop the script
key=input("")
if key=="k":
   mv.kill()
   sc.kill()
   sa.kill()
