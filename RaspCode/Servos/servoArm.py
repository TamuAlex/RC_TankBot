import servoArmDeclaration as sA
import time


'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''

'''
Wrap class to define functions for moving the arm servos,
given the desired direction
It uses the servoArmDeclaration library to interact with
the motors at lower level
'''
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

    '''
    Function that makes the given servo starst moving up.
    In the rotor servo it start rotating right
    In the claw servo it start opening
    
    param: servo pin it is wanted to move
    '''
    def up(self,pin):
        self.movN[pin]="u"
        while self.movN[pin]=="u":
            sA.set_PWidth(pin,sA.get_PWidth(pin)+self.speed)
            #sA.set_PWidth ("S1",2000)
            time.sleep(0.002)
            
            
    '''
    Function that makes the given servo starst moving down.
    In the rotor servo it start rotating left
    In the claw servo it start closing
    
    param: servo pin it is wanted to move
    '''
    def down(self,pin):
        self.movN[pin]="d"
        while self.movN[pin]=="d":
            sA.set_PWidth(pin,sA.get_PWidth(pin)-self.speed)
            time.sleep(0.002)
            
            
    '''
    Function that stops the movement of the given servo
    '''
    def stop(self,pin):
        self.movN[pin]="s"
        if pin=="SP":
            sA.set_PWidth(pin,0)
            

        
            
    
