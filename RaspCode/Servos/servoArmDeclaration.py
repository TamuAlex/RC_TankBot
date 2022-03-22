import pigpio
import time
'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''

'''
Library for interacting with the arm servos
'''

######Arm servo Definitions######

pinS1 = 7           #GPIO pin for the first servo
pinS2 = 8           #GPIO pin for the second servo
pinSR =11           #GPIO pin for the rotor servo
pinSP=25            #GPIO pin for the claw servo


pwm= pigpio.pi()

#Initializate the servo pins as Pulse-width Modulation
pwm.set_mode(pinS1, pigpio.OUTPUT)
pwm.set_mode(pinS2, pigpio.OUTPUT)
pwm.set_mode(pinSR, pigpio.OUTPUT)
pwm.set_mode(pinSP, pigpio.OUTPUT)


#Set the servos frequency
pwm.set_PWM_frequency(pinS1, 50)
pwm.set_PWM_frequency(pinS2, 50)
pwm.set_PWM_frequency(pinSR, 50)
pwm.set_PWM_frequency(pinSP, 50)


#Creates a dictionary with the servos names, and their pines
pines={"S1":7,"S2":8,"SR":11,"SP":25}

'''
Function that set a given servo a new pulsewidth.
It makes the servo move to a new position, depending the
value of the pusewidth (500-2500)

Param (pin): Pulse width to move the servo
Param (newPulseW): Pulse width to move the servo
'''
def set_PWidth (pin,newPulseW):
    if newPulseW >= 500 and newPulseW <=2500:
        pwm.set_servo_pulsewidth( pines[pin], newPulseW )
    
'''
Function that gives the current pulse width of the
given servo.


param: Servo which want to know
Return: Pulsewidth of the given Servo
'''
def get_PWidth (pin):
    return pwm.get_servo_pulsewidth( pines[pin])

'''
Function to get the list of pines used to move the servos

return: a dictionary with the pines and their names
'''
def get_Pines():
    return pines
    








