#! /bin/sh

#Connection try
#Waits until a Internet connection is stablished before continuing with the set-up
status=1
echo "Waiting for a connection"
while [ $status -ne 0 ];do
	ping -q -c 1 8.8.8.8 > /dev/null 2>&1 
	if [ $? -eq 0 ]; then
		status=0
	fi
done 

echo "Done"
	 
#Check packages

#Checks if the pigpio package is installed (for controlling the pins) and launchs it
if dpkg -l | grep -q -w pigpio; then
	echo "Pigpio installed"
	sudo pigpiod  > /dev/null 2>&1 
	echo "Pigpio launched"
else
	echo "No Pigpio version founded"
	exit 1
fi


#Launches the rtsp-simple-server application to strat emiting the video stream
	sudo  /home/pi/RaspCode/rtsp-simple-server 2> /home/pi/server.log & 
	echo "rtsp-simple-server launched"


#Starts the python code where all the motos and servos will start up
python3 /home/pi/RaspCode/tankrobot.py
