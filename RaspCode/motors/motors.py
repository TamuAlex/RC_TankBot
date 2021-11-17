import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
######Motor Definition######
ENA = 13	#//L298-Enable Motor A
ENB = 20	#//L298-Enable Motor B
IN1 = 19	#//Motor Iface 1
IN2 = 16	#//Motor Iface 2
IN3 = 21	#//Motor Iface 3
IN4 = 26	#//Motor Iface 4

def_speed = 50


#########The motor is initialized as LOW##########
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

def	GPIOSet(gpio):
	GPIO.output(gpio,True)

def	GPIOClr(gpio):
	GPIO.output(gpio,False)

def ENAset(EA_num):
	ENA_pwm.ChangeDutyCycle(EA_num)
def ENBset(EB_num):
	ENB_pwm.ChangeDutyCycle(EB_num)
	
def setSpeed(speed):
    ENB_pwm.ChangeDutyCycle(speed)
    ENA_pwm.ChangeDutyCycle(speed)
    def_speed = speed
    
def getSpeed(speed):
    return def_speed
