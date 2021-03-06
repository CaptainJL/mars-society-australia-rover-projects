# MOTORS TESTING

# import general
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from envirophat import analog

# import and set IO components

GPIO.setwarnings(False)

# All pins in GPIO.BCM setup
# Following guide at https://pinout.xyz/#
gpio_list = [22,23,5,17,27,6] 
pwm_list = [12,13]
GPIO.setup(gpio_list, GPIO.OUT)
GPIO.setup(pwm_list, GPIO.OUT)






# MOTOR SETUP
# motor 0
m0_i0 = 22
m0_i1 = 23
m0_en = 5
m0_PWM = GPIO.PWM(12, 980)
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,0)
GPIO.output(m0_en,0)
 
# motor 1 
m1_i0 = 17
m1_i1 = 27
m1_en = 6
m1_PWM = GPIO.PWM(13, 980)
GPIO.output(m1_i0,0)
GPIO.output(m1_i1,0)






# Run Motor 0 only - Motor 1 not programmed but similar setup                                                                           
GPIO.output(m0_en,1)
m0_PWM.start(0)

# motor forward
print "forward fast"
m0_PWM.ChangeDutyCycle(90)	# Duty cycle = 0-100
GPIO.output(m0_i0,1)
GPIO.output(m0_i1,0)
time.sleep(2)
print(analog.read_all())	# display all adc values from envirophat
time.sleep(3)

# motor slow
print "forward slow"
m0_PWM.ChangeDutyCycle(30)
GPIO.output(m0_i0,1)
GPIO.output(m0_i1,0)
time.sleep(2)
print(analog.read_all())
time.sleep(3)


# motor reverse
# flip pins i0 and i1 from 1,0 to 0,1 for reverse
print "reverse fast"
m0_PWM.ChangeDutyCycle(90)
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,1)
time.sleep(5)






# end
print "end"
m0_PWM.stop()
m1_PWM.stop()
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,0)
GPIO.output(m0_en,0)
GPIO.output(m1_i0,0)
GPIO.output(m1_i1,0)
GPIO.output(m1_en,0)
time.sleep(1)
GPIO.cleanup()
