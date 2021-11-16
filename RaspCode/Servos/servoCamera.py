import servoDeclaration as sD
import time

class ServoCamera:
    up_con=False
    down_con=False
    left_con=False
    right_con=False
    vSpeed=float(1)
    hSpeed=float(1)
    
    def __init__(self):
        sD.set_PWidth_H(float(1250))
        sD.set_PWidth_V(float(1250))
                
    def up(self):
        self.up_con=True
        while self.up_con:
            sD.set_PWidth_V(sD.get_PWidth_V()+self.vSpeed)
            time.sleep(0.005)
            #sD.set_PWidth_V(2000)
            #print("up:" + str(sD.get_PWidth_V()))
            
    def down(self):
        self.down_con=True
        while self.down_con:
            sD.set_PWidth_V(sD.get_PWidth_V()-self.vSpeed)
            time.sleep(0.005)
            #print("down:" + str(sD.get_PWidth_V()))
            
    def left(self):
        self.left_con=True
        while self.left_con:
            sD.set_PWidth_H(sD.get_PWidth_H()+self.hSpeed)
            time.sleep(0.005)
            #print("left:" + str(sD.get_PWidth_H()))
            
    def right(self):
        self.right_con=True
        while self.right_con:
            sD.set_PWidth_H(sD.get_PWidth_H()-self.hSpeed)
            time.sleep(0.005)
            #print("right:" + str(sD.get_PWidth_H()))
            
    def stop(self,movement):
        if movement=="up":
            self.up_con=False
        elif movement=="down":
            self.down_con=False
        elif movement=="left":
            self.left_con=False
        else:
            self.right_con=False
            
    def set_SpeedV(self,newSpeed):
        self.vSpeed=newSpeed
    def get_speedV(self):
        return self.vSpeed
    def set_SpeedH(self,newSpeed):
        self.hSpeed=newSpeed
    def get_speedH(self):
        return self.hSpeed
    def __str__(self):
        return " up: " + str(self.up_con) + " down: " + str(self.down_con) + " left: " + str(self.left_con) + " right: " + str(self.right_con) + "speed V: " + str(self.speedV) +"speed H: " + str(self.speedH)
    
        
        