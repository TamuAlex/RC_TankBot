import pigpio
import time

######Camera servo Definitions######

pinS1 = 7   #GPIO pin for the horizontal servo
pinS2 = 8
pinSR =11
pinSP=25            #GPIO pin for the vertical servo


pwm= pigpio.pi()


pwm.set_mode(pinS1, pigpio.OUTPUT)
pwm.set_mode(pinS2, pigpio.OUTPUT)
pwm.set_mode(pinSR, pigpio.OUTPUT)
pwm.set_mode(pinSP, pigpio.OUTPUT)

pwm.set_PWM_frequency(pinS1, 50)
pwm.set_PWM_frequency(pinS2, 50)
pwm.set_PWM_frequency(pinSR, 50)
pwm.set_PWM_frequency(pinSP, 50)

pines={"S1":7,"S2":8,"SR":11,"SP":25}


def set_PWidth (pin,newPulseW):
    if newPulseW >= 500 and newPulseW <=2500:
        pwm.set_servo_pulsewidth( pines[pin], newPulseW )
        
def get_PWidth (pin):
    return pwm.get_servo_pulsewidth( pines[pin])

def get_Pines():
    return pines
    








