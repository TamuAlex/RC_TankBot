import motors

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''


'''
Wrap class to define functions for moving the motors,
given the desired direction
It uses the motors library to iteract with the motors
at lower level
'''
class Movement:
    
    def __init__(self):
        pass

    '''
    Function that makes the robot move forward
    '''
    def forward(self):
        #First both motors are enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished 
        motors.GPIOSet(motors.IN1)
        motors.GPIOClr(motors.IN2)
        motors.GPIOSet(motors.IN3)
        motors.GPIOClr(motors.IN4)
    
    '''
    Function that makes the robot move backward
    '''
    def back(self):
        #First both motors are enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOClr(motors.IN1)
        motors.GPIOSet(motors.IN2)
        motors.GPIOClr(motors.IN3)
        motors.GPIOSet(motors.IN4)
        
    '''
    Function that makes the robot turn left
    '''
    def left(self):
        #First only the right motor is enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOSet(motors.IN1)
        motors.GPIOClr(motors.IN2)
        motors.GPIOClr(motors.IN3)
        motors.GPIOSet(motors.IN4)

    '''
    Function that makes the robot turn right
    '''
    def right(self):
        #First only the left motor is enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOClr(motors.IN1)
        motors.GPIOSet(motors.IN2)
        motors.GPIOSet(motors.IN3)
        motors.GPIOClr(motors.IN4)

    '''
    Function that makes the robot stop
    '''
    def stop(self):
        #First both motors are disabled
        motors.GPIOClr(motors.ENA)
        motors.GPIOClr(motors.ENB)
        
        #Then the direction is disabled
        motors.GPIOClr(motors.IN1)
        motors.GPIOClr(motors.IN2)
        motors.GPIOClr(motors.IN3)
        motors.GPIOClr(motors.IN4)
	
    def setSpeed(self, speed):
        motors.setSpeed(speed)
        
    def getSpeed():
        return motors.getSpeed()