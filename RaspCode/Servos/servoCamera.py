import servoCameraDeclaration as sC
import time

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''

'''
Wrap class to define functions for moving the camera servos,
given the desired direction
It uses the servoCameraDeclaration library to iteract with
the motors at lower level
'''
class ServoCamera:
    up_con=False
    down_con=False
    left_con=False
    right_con=False
    vSpeed=float(1)
    hSpeed=float(1)
    
    def __init__(self):
        sC.set_PWidth_H(float(1500))
        sC.set_PWidth_V(float(700))
    
    '''
    Function that makes the camera start looking up
    '''
    def up(self):
   
        #The flag indicates that the camera is moving in this direction
        self.up_con=True
        while self.up_con:
            # While the flag is true (until the stop(up) function is called)
            # The servo keeps moving
            sC.set_PWidth_V(sC.get_PWidth_V()+self.vSpeed)
            time.sleep(0.005)

    
    '''
    Function that makes the camera start looking down
    '''
    def down(self):
        self.down_con=True
        while self.down_con:
            sC.set_PWidth_V(sC.get_PWidth_V()-self.vSpeed)
            time.sleep(0.005)
            #print("down:" + str(sC.get_PWidth_V()))
    
    '''
    Function that makes the camera start looking left
    '''
    def left(self):
        self.left_con=True
        while self.left_con:
            sC.set_PWidth_H(sC.get_PWidth_H()+self.hSpeed)
            time.sleep(0.005)
            #print("left:" + str(sC.get_PWidth_H()))
            
    '''
    Function that makes the camera start looking right
    '''
    def right(self):
        self.right_con=True
        while self.right_con:
            sC.set_PWidth_H(sC.get_PWidth_H()-self.hSpeed)
            time.sleep(0.005)
            #print("right:" + str(sC.get_PWidth_H()))
    
    
    '''
    Function that, given a movement, stops the movement in that
    direction.
    For example, if the camera is moving up, and stop(up) is called,
    the camera will stop moving up
    
    Param: Movement it is wnated to stop {up, down, left, rigth}
    '''
    def stop(self,movement):
        if movement=="up":
            self.up_con=False
        elif movement=="down":
            self.down_con=False
        elif movement=="left":
            self.left_con=False
        else:
            self.right_con=False
    
    
    
    '''
    Function to set the speed of the vertical movement
    Param: New speed
    '''
    def set_SpeedV(self,newSpeed):
        self.vSpeed=newSpeed
        
    '''
    Function to get the speed of the vertical movement
    Return: Current speed
    '''
    def get_speedV(self):
        return self.vSpeed
    
    '''
    Function to set the speed of the horizontal movement
    Param: New speed
    '''
    def set_SpeedH(self,newSpeed):
        self.hSpeed=newSpeed
        
    '''
    Function to get the speed of the horizontal movement
    Return: Current speed
    '''   
    def get_speedH(self):
        return self.hSpeed
    
    
    def __str__(self):
        return " up: " + str(self.up_con) + " down: " + str(self.down_con) + " left: " + str(self.left_con) + " right: " + str(self.right_con) + "speed V: " + str(self.speedV) +"speed H: " + str(self.speedH)
    
        