import pigpio

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''

'''
Library for interacting with the camera servos
'''

######Camera servo Definitions######

Hpin = 22   #GPIO pin for the horizontal servo
Vpin = 27   #GPIO pin for the vertical servo

maxWidth=2000
minWidth=500

#Initializate the servo pins as Pulse-width Modulation
pwmH = pigpio.pi()
pwmV = pigpio.pi()
pwmH.set_mode(Hpin, pigpio.OUTPUT)
pwmV.set_mode(Vpin, pigpio.OUTPUT)

#Set the servos frequency
pwmH.set_PWM_frequency(Hpin, 50 )
pwmV.set_PWM_frequency(Vpin, 50 )


'''
Function that set the Horizontal servo a new pulsewidth.
It makes the servo move to a new position, depending the
value of the pusewidth (500-2000)

Param: Pulse width to move the servo
'''
def set_PWidth_H (newPulseW):
    if newPulseW >= 500 and newPulseW <=2000:
        pwmH.set_servo_pulsewidth( Hpin, newPulseW )


'''
Function that set the Vertical servo a new pulsewidth.
It makes the servo move to a new position, depending the
value of the pusewidth (500-2000)

Param: Pulse width to move the servo
'''
def set_PWidth_V (newPulseW):
    if newPulseW >= 500 and newPulseW <=2000:
        pwmV.set_servo_pulsewidth( Vpin, newPulseW )


'''
Function that gives the current pulse width of the
Horizontal servo.

Return: Pulsewidth of the Horizontal Servo
'''
def get_PWidth_H ():
    return pwmH.get_servo_pulsewidth( Hpin)


'''
Function that gives the current pulse width of the
Vertical servo.

Return: Pulsewidth of the Vertical Servo
'''
def get_PWidth_V ():
    return pwmV.get_servo_pulsewidth( Vpin)


