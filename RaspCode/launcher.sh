#! /bin/sh
#Connection try

#Waits until a connection to internet is stablished
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

if dpkg -l | grep -q -w pigpio; then
	echo "Pigpio installed"
	sudo pigpiod  > /dev/null 2>&1 
	echo "Pigpio launched"
else
	echo "No Pigpio version founded"
	exit 1
fi


#	sudo  /home/pi/RaspCode/rtsp-simple-server &> /home/pi/server.log &



python3 /home/pi/RaspCode/tankrobot.py
