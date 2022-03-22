#! /bin/sh
#Connection try
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


if dpkg -l | grep -q -w motion; then
	echo "motion installed"
	sudo  /home/pi/RaspCode/rtsp-simple-server 2> /home/pi/server.log & 
	echo "motion launched"
else
	echo "No Motion version founded" 
	exit 1
fi


python3 /home/pi/RaspCode/tankrobot.py
