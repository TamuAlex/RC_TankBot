import RPi.GPIO as GPIO

'''
        Authors:
        Alejandro Ortega Martinez: alejandro.ormar@gmail.com
        Juan Luis Garcia Gonzalez: jgg1009@alu.ubu.es
'''

'''
Library for interacting with the motors
'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
######Motor Definition######
ENA = 13	#//L298-Enable Motor A
ENB = 20	#//L298-Enable Motor B
IN1 = 19	#//Motor Iface 1
IN2 = 16	#//Motor Iface 2
IN3 = 21	#//Motor Iface 3
IN4 = 26	#//Motor Iface 4


#ENB = 13	#//L298-Enable Motor A
#ENA = 20	#//L298-Enable Motor B
#IN3 = 19	#//Motor Iface 1
#IN4 = 16	#//Motor Iface 2
#IN1 = 21	#//Motor Iface 3
#IN2 = 26	#//Motor Iface 4

def_speed = 90 #The relative power of the motors (0-100)


#########The  both motor are initialized as LOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
ENA_pwm=GPIO.PWM(ENA,1000)
ENA_pwm.start(0)
ENA_pwm.ChangeDutyCycle(def_speed)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)

GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
ENB_pwm=GPIO.PWM(ENB,1000)
ENB_pwm.start(0)
ENB_pwm.ChangeDutyCycle(def_speed)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

"""
GPIOSet(gpio)
Function that enable the current power of the pin given

Param: the pin (BCM mode) which we want to interact

"""
def	GPIOSet(gpio):
	GPIO.output(gpio,True)
"""
GPIOClr(gpio)
Function that disable the current power of the pin given

Param: the pin (BCM mode) which we want to interact

"""
def	GPIOClr(gpio):
	GPIO.output(gpio,False)
"""
ENAset(EA_num)
Function that establish the given duty cycle in the motor A

Param: the duty cycle

"""
def ENAset(EA_num):
	ENA_pwm.ChangeDutyCycle(EA_num)
"""
ENBset(EB_num)
Function that establish the given duty cycle to the motor b

Param: the duty cycle

"""
def ENBset(EB_num):
	ENB_pwm.ChangeDutyCycle(EB_num)
"""
setSpeed(speed)
Function that change the current spped of the motors

Param: the new speed

"""
def setSpeed(speed):
    ENB_pwm.ChangeDutyCycle(speed)
    ENA_pwm.ChangeDutyCycle(speed)
    def_speed = speed

"""
getSpeed(speed)
Function that returns the current speed

Return: The current speed.

"""
def getSpeed(speed):
    return def_speed
