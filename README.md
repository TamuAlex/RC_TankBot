# RC_TankRobot
Code to make the tank robot at Turku GameLab work 
<br>
<br>
## Table Of Contents
* [General info](#general-info)
  + [Anatomy of the robot](#anatomy-of-the-robot)
    - [The brain](#the-brain-the-controller)
    - [The muscles](#the-muscles-the-actuators)
    - [The eyes](#the-eyes-a-camera)
    - [The energy](#the-energy)
  + [The Scripts](#the-scripts)

* [Robot SetUp](#robot-setup)
  + [First Steps](#first-steps)
  + [WiFi Connection](#wifi-connection)
  + [Install Pigpio package](#install-pigpio-package)
  + [launcher.sh](#launchersh)
  + [tankrobot.py](#tankrobotpy)
  + [Editing the cron file](#editing-the-cron-file)
  + [Camera troubleshooting](#camera-troubleshooting)

<br>
<br>

## General info
This project consists on all the code neccessary to get a tank robot working, up and going headless from start, as well as some examples on how to implement the communications from a server to send the movement instructions.
<br>
<br>
<br>
### *Anatomy of the robot*

#### The brain (The controller)
The main controller of this tank robot is a [Raspberry pi 3b](https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/), attacheed  to a PWR.A53 A Power and motor driver board:
![PWR.A53 A board](https://github.com/TamuAlex/RC_TankBot/blob/main/images/Screenshot%202022-04-06%20112405.png?raw=true "PWR a.53 A")
<br>
<br>
#### The muscles (The actuators)
We can divide them into two categories, motors and servos.
##### Motors
The actuators that perrform the robot movement are two simple motors.
##### Servos
They permit the movement of the arm and the camera
* The camera has two servos, one for moving up and down, and another one for looking sideways. They have 180 degrees of freedom
* The arm has four servos:
  + Two servos for moving the arm up and down, with 180 degrees of freedom
  + One servo that lets the claw turn left and right, with 180 degrees of freedom
  + One servo that performs the opening-closing of the claw

#### The eyes (A camera)
The robot also has a simple USB camera attached to the raspberry Pi to receive the video feed for it to be streamed.  
  
  

#### The energy
This tank robot is powered with an 11.1V 2200mAh 8A protection board lithium battery pack


### *The Scripts*
See the [Project Wiki](../../wiki) to see how the scripts works

<br>
<br>
<br>
<br>

## Robot Setup
Before having the robot up and running (and more important, having it working headless), a little set up is needed to be done in order to get the robot working. 
<p>To simplify it, there are a couple of scripts that makes most of the work, but we will have to connect with a keyboard, mouse, and screen for the first time.</p>
<br>

### First steps
<p>First of all, install an ubuntu distro in the raspberry (This tutorial is made for the raspbian distro, if you are not using this, you may need to change some lines in a couple of scripts), and then *copy the [RaspCode](https://github.com/TamuAlex/RC_TankBot/tree/main/RaspCode) folder in the home directory of the pi user (/home/pi)*</p>
<br>

### WiFi Connection
FThe next thing to do is to set up a WiFi connection to have the robot connected to. Remember the SSID and the password of the WiFi you connect the robot to the first time, and use allways that same SSID and password, so the robot will be able to connect automaticaly once it is working headless.
<br>

### Install pigpio package
<p>This is the package used to control the General Pins for Input/Output (GPIO) on the raspberry, so install it by typping:</p>

``
$ sudo apt-get install pigpio
``
<br>
### launcher.sh
[This script](https://github.com/TamuAlex/RC_TankBot/blob/main/RaspCode/launcher.sh) is the one that checks that everything is working fine, and then launch the rest of the scripts.

The first thing it does is check for internet connection, and once it is connected, starts with the rest of steps:
https://github.com/TamuAlex/RC_TankBot/blob/db08880b34885b051e20bbbc93cfe5aaeb37782f/RaspCode/launcher.sh#L5-L12

Then, it checks if the pigpio package is installed, and if so, it launches it:
https://github.com/TamuAlex/RC_TankBot/blob/db08880b34885b051e20bbbc93cfe5aaeb37782f/RaspCode/launcher.sh#L18-L25

Finally, it launches the [tankrobot.py](https://github.com/TamuAlex/RC_TankBot/blob/main/RaspCode/tankrobot.py) script:
https://github.com/TamuAlex/RC_TankBot/blob/db08880b34885b051e20bbbc93cfe5aaeb37782f/RaspCode/launcher.sh#L32
**Note:** If your project is in other folder, you should change this line of code
<br>

### tankrobot.py
Its mission is to launch each individual script for each functionality (movement, camera servos, arm servos, and video streaming):
https://github.com/TamuAlex/RC_TankBot/blob/db08880b34885b051e20bbbc93cfe5aaeb37782f/RaspCode/tankrobot.py#L7-L10

### Editing the Cron file
<p>The cron daemon's work is to automatize jobs. As we want that everithing start on startup, we need to tell the cron daemon to do so.</p>
<p>To do so, we will need to edit the crontab file, with:</p>

``
$ crontab -e
``

Now, we want the cron daemos to execute the launcher.sh script everytime the raspberry boots. To do so, we need to add the following line at the end of the crontab file:

``
@reboot /home/pi/RaspCode/launcher.sh > /home/pi/launcher.log
``

**Note:** If your project is in other folder, you should change this line of code


### Camera Troubleshooting
If you see that the camera does not start, try coping the rtsp-simple-server.yml archive to the user folder (/home/pi)

## *Unity project*
https://tuas365-my.sharepoint.com/:u:/g/personal/alejandro_ortegamartinez_edu_turkuamk_fi/EV5GIJV7zztJlzsSsNKfIsEBEG40_-QvP37fTVBgqF3KPA?e=YVPkDS

(If there is any kind of problem with the link please contact alejandro.ormar@gmail.com)


