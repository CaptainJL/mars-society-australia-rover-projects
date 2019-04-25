# MOTORS TESTING

# import general
import time

# import and set IO components
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

gpio_list = [11,13,15,16] 
pwm_list = [32,33]
GPIO.setup(gpio_list, GPIO.OUT)
GPIO.setup(pwm_list, GPIO.OUT)


# MOTOR SETUP
# motor 0
m0_i0 = 11
m0_i1 = 13
m0_enPWM = GPIO.PWM(32, 980)
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,0)

# motor 1
m1_i0 = 15
m1_i1 = 16
m1_enPWM = GPIO.PWM(33, 980)
GPIO.output(m1_i0,0)
GPIO.output(m1_i1,0)


# RUN MOTOR (0)
m0_enPWM.start(0)
# motor forward
print "forward fast"
m0_enPWM.ChangeDutyCycle(90)
GPIO.output(m0_i0,1)
GPIO.output(m0_i1,0)
time.sleep(5)

# motor slow
print "forward slow"
m0_enPWM.ChangeDutyCycle(30)
GPIO.output(m0_i0,1)
GPIO.output(m0_i1,0)
time.sleep(5)

# motor reverse
print "reverse fast"
m0_enPWM.ChangeDutyCycle(90)
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,1)
time.sleep(5)


# end
print "end"
m0_enPWM.stop()
GPIO.output(m0_i0,0)
GPIO.output(m0_i1,0)
GPIO.output(m1_i0,0)
GPIO.output(m1_i1,0)

time.sleep(1)
GPIO.cleanup()
