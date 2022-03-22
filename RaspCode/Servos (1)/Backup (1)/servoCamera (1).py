import servoDeclaration as sD

class ServoCamera:
    def __init__(self):
        sD.set_PWidth_H(1250)
        sD.set_PWidth_V(1250)
        
        self.vSpeed=1
        self.hSpeed=10
        
        self.up_con=False
        self.down_con=False
        self.left_con=False
        self.right_con=False
    def up(self):
        up_con=True
        while up_con:
            print(sD.get_PWidth_V())
            sD.set_PWidth_V(sD.get_PWidth_V()+self.vSpeed)
    def down(self):
        down_con=True
        while down_con:
            sD.set_PWidth_V(sD.get_PWidth_V()-self.vSpeed)
    def left(self):
        left_con=True
        while left_con:
            sD.set_PWidth_H(sD.get_PWidth_H()-self.hSpeed)
    def right(self):
        right_con=True
        while right_con:
            sD.set_PWidth_H(sD.get_PWidth_H()+self.hSpeed)
    def stop(self,movement):
        if movement=="up":
            self.up_control=False
        elif movement=="down":
            self.down_control=False
        elif movement=="left":
            self.left_control=False
        else:
            right_control=False
    def set_SpeedV(self,newSpeed):
        self.vSpeed=newSpeed
    def get_speedV(self):
        return vSpeed
    def set_SpeedH(self,newSpeed):
        self.hSpeed=newSpeed
    def get_speedH(self):
        return self.hSpeed
    
        
        