import subprocess
import os
import signal

mv=subprocess.Popen(['python3', 'motors/movementScript.py'])
sc=subprocess.Popen(['python3', 'Servos/servoCameraScript.py'])
sa=subprocess.Popen(['python3', 'Servos/servoArmScript.py'])

key=input("")
if key=="k":
   mv.kill()
   sc.kill()
   sa.kill()
