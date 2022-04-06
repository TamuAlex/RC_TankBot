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
## *Unity project*
https://tuas365-my.sharepoint.com/:u:/g/personal/alejandro_ortegamartinez_edu_turkuamk_fi/EV5GIJV7zztJlzsSsNKfIsEBEG40_-QvP37fTVBgqF3KPA?e=YVPkDS

(If there is any kind of problem with the link please contact alejandro.ormar@gmail.com)


