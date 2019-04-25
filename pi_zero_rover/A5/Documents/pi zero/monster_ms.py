"""
Monster Motor Shield Driver
Raspberry Pi - Python
Add the foler this is located to PYTHONPATH variable
"""

import RPi.GPIO as GPIO


# Monster_Motor_Shield class
class MONSTER_MS():

    gpio_list = [17,27,22,23,5,6] 
    pwm_list = [12,13]
        
    # MOTOR Params
    # motor 0
    m0_i0 = 22
    m0_i1 = 23
    m0_en = 5

    # motor 1
    m1_i0 = 17
    m1_i1 = 27
    m1_en = 6


    def __init__(self):
        print "init motor shield"
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.gpio_list, GPIO.OUT)
        GPIO.setup(self.pwm_list, GPIO.OUT)

        self.m0_PWM = GPIO.PWM(12, 980)
        GPIO.output(self.m0_i0,0)
        GPIO.output(self.m0_i1,0)
        GPIO.output(self.m0_en,0)

        self.m1_PWM = GPIO.PWM(13, 980)
        GPIO.output(self.m1_i0,0)
        GPIO.output(self.m1_i1,0)
        GPIO.output(self.m1_en,0)

        self.m0_PWM.start(0)
        self.m1_PWM.start(0)
        self.m0_PWM.ChangeDutyCycle(0)
        self.m1_PWM.ChangeDutyCycle(0)

    def forward(self, motor, speed):
        if (motor==0):
            GPIO.output(self.m0_en,1)
            GPIO.output(self.m0_i0,1)
            GPIO.output(self.m0_i1,0)
            self.m0_PWM.ChangeDutyCycle(speed)
        elif (motor==1):
            GPIO.output(self.m1_en,1)
            GPIO.output(self.m1_i0,1)
            GPIO.output(self.m1_i1,0)
            self.m1_PWM.ChangeDutyCycle(speed)
        else:
            print "Motors 0-1 only!"

    def reverse(self, motor, speed):
        if (motor==0):
            GPIO.output(self.m0_en,1)
            GPIO.output(self.m0_i0,0)
            GPIO.output(self.m0_i1,1)
            self.m0_PWM.ChangeDutyCycle(speed)
        elif (motor==1):
            GPIO.output(self.m1_en,1)
            GPIO.output(self.m1_i0,0)
            GPIO.output(self.m1_i1,1)
            self.m1_PWM.ChangeDutyCycle(speed)
        else:
            print "Motors 0-1 only!"
     
    def stop(self):
            GPIO.output(self.m0_en,1)
            GPIO.output(self.m0_i0,0)
            GPIO.output(self.m0_i1,0)
            self.m0_PWM.ChangeDutyCycle(0)
            GPIO.output(self.m1_en,1)
            GPIO.output(self.m1_i0,0)
            GPIO.output(self.m1_i1,0)
            self.m1_PWM.ChangeDutyCycle(0)
            print "Motors stopping!"




if __name__ == "__main__":
    print "dont know why this is here!"



















