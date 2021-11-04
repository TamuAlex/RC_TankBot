import motors

    
class Movement:
    
    def __init__(self):
        pass
	
    def forward(self):
        #First both motors are enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished 
        motors.GPIOSet(motors.IN1)
        motors.GPIOClr(motors.IN2)
        motors.GPIOSet(motors.IN3)
        motors.GPIOClr(motors.IN4)
    
    def back(self):
        #First both motors are enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOClr(motors.IN1)
        motors.GPIOSet(motors.IN2)
        motors.GPIOClr(motors.IN3)
        motors.GPIOSet(motors.IN4)
	
    def left(self):
        #First only the right motor is enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOSet(motors.IN1)
        motors.GPIOClr(motors.IN2)
        motors.GPIOClr(motors.IN3)
        motors.GPIOSet(motors.IN4)
	
    def right(self):
        #First only the left motor is enabled
        motors.GPIOSet(motors.ENA)
        motors.GPIOSet(motors.ENB)
        
        #Then the direction is stablished
        motors.GPIOClr(motors.IN1)
        motors.GPIOSet(motors.IN2)
        motors.GPIOSet(motors.IN3)
        motors.GPIOClr(motors.IN4)
	
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