import pigpio
import time

######Camera servo Definitions######

Hpin = 25   #GPIO pin for the horizontal servo
  #GPIO pin for the vertical servo


pwm= pigpio.pi()

pwm.set_mode(Hpin, pigpio.OUTPUT)

 
pwm.set_PWM_frequency(Hpin, 50 )

pwm.set_servo_pulsewidth( Hpin, 500)
time.sleep(3)
pwm.set_servo_pulsewidth( Hpin, 2500)
time.sleep(3)
pwm.set_servo_pulsewidth( Hpin, 0)





