import pigpio

######Camera servo Definitions######

Hpin = 22   #GPIO pin for the horizontal servo
Vpin = 27   #GPIO pin for the vertical servo

maxWidth=2000
minWidth=500

pwmH = pigpio.pi()
pwmV = pigpio.pi()
pwmH.set_mode(Hpin, pigpio.OUTPUT)
pwmV.set_mode(Vpin, pigpio.OUTPUT)
 
pwmH.set_PWM_frequency(Hpin, 50 )
pwmV.set_PWM_frequency(Vpin, 50 )

def set_PWidth_H (newPulseW):
    if newPulseW >= 500 and newPulseW <=2000:
        pwmH.set_servo_pulsewidth( Hpin, newPulseW )
    
def set_PWidth_V (newPulseW):
    if newPulseW >= 500 and newPulseW <=2000:
        pwmV.set_servo_pulsewidth( Vpin, newPulseW )
        
def get_PWidth_H ():
    return pwmH.get_servo_pulsewidth( Hpin)
    
def get_PWidth_V ():
    return pwmV.get_servo_pulsewidth( Vpin)


