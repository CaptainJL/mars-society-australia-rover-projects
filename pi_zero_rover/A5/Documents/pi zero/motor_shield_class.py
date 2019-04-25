
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


class Monster_Motor_Shield:
	
	def forward(self, speed):
		GPIO.output(self.p_en,1)
		GPIO.output(self.p0,1)
		GPIO.output(self.p1,0)	
		self.p_pwm.ChangeDutyCycle(speed)
		
	def reverse(self, speed):
		GPIO.output(self.p_en,1)
		GPIO.output(self.p0,0)
		GPIO.output(self.p1,1)	
		self.p_pwm.ChangeDutyCycle(speed)	
		
	def stop(self):
		GPIO.output(self.p_en,0)
		GPIO.output(self.p0,0)
		GPIO.output(self.p1,0)	
		self.p_pwm.stop()
		
	def __init__(self, pinpwm, pinen, pin0, pin1):
		GPIO.setup(pinpwm, GPIO.OUT)
		GPIO.setup(pinen, GPIO.OUT)
		GPIO.setup(pin0, GPIO.OUT)
		GPIO.setup(pin1, GPIO.OUT)	
		self.p_pwm = 	GPIO.PWM(pinpwm, 980)
		self.p_en = 	pinen	
		self.p0 = 	pin0
		self.p1 = 	pin1
		
