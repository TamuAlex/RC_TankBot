import servoArm as sA

class ServoArmMovement:
    
    movN={"S1":"s","S2":"s","SR":"s","SP":"s"}
    speed=1
    
    def __init__(self):
        
        sA.set_PWidth ("S1",2500)
        sA.set_PWidth ("S2",1000)
        sA.set_PWidth ("SR",1500)
        sA.set_PWidth ("SP",900)
        
        movN={"S1":"s","S2":"s","SR":"s","SP":"s"}
        speed=1

    def up(self,pin):
        self.movN[pin]="u"
        while self.movN[pin]=="u":
            sA.set_PWidth(pin,sA.get_PWidth(pin)+self.speed)
    def down(self,pin):
        self.movN[pin]="d"
        while self.movN[pin]=="d":
            sA.set_PWidth(pin,sA.get_PWidth(pin)-self.speed)
    def stop(self,pin):
        self.movN[pin]="s"
        if pin=="SP":
            sA.set_PWidth(pin,0)
            
    