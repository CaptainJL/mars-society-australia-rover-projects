
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


# This class is for the MotoZero motor controller board
# Motors 1 & 2 are for the left side of the vehicle
# Motors 3 & 4 are for the right side of the vehicle

class MotoZero:

	def forward(self):
		#GPIO.output(self.m1[0], 1)
		#GPIO.output(self.m1[1], 1)
		#GPIO.output(self.m1[2], 0)
		GPIO.output(5, 1)
		GPIO.output(24, 1)
		GPIO.output(27, 0)
				
		GPIO.output(self.m2[0], 1)
		GPIO.output(self.m2[1], 1)
		GPIO.output(self.m2[2], 0)
			
		GPIO.output(self.m3[0], 1)
		GPIO.output(self.m3[1], 1)
		GPIO.output(self.m3[2], 0)
			
		GPIO.output(self.m4[0], 1)
		GPIO.output(self.m4[1], 1)
		GPIO.output(self.m4[2], 0)


	def reverse(self):
		GPIO.output(self.m1[0], 1)
		GPIO.output(self.m1[1], 0)
		GPIO.output(self.m1[2], 1)
			
		GPIO.output(self.m2[0], 1)
		GPIO.output(self.m2[1], 0)
		GPIO.output(self.m2[2], 1)
			
		GPIO.output(self.m3[0], 1)
		GPIO.output(self.m3[1], 0)
		GPIO.output(self.m3[2], 1)
			
		GPIO.output(self.m4[0], 1)
		GPIO.output(self.m4[1], 0)
		GPIO.output(self.m4[2], 1)


	def left(self):
		GPIO.output(self.m1[0], 1)
		GPIO.output(self.m1[1], 0)
		GPIO.output(self.m1[2], 1)
			
		GPIO.output(self.m2[0], 1)
		GPIO.output(self.m2[1], 0)
		GPIO.output(self.m2[2], 1)
			
		GPIO.output(self.m3[0], 1)
		GPIO.output(self.m3[1], 1)
		GPIO.output(self.m3[2], 0)
			
		GPIO.output(self.m4[0], 1)
		GPIO.output(self.m4[1], 1)
		GPIO.output(self.m4[2], 0)	
	
	
	def right(self):
		GPIO.output(self.m1[0], 1)
		GPIO.output(self.m1[1], 1)
		GPIO.output(self.m1[2], 0)
			
		GPIO.output(self.m2[0], 1)
		GPIO.output(self.m2[1], 1)
		GPIO.output(self.m2[2], 0)
			
		GPIO.output(self.m3[0], 1)
		GPIO.output(self.m3[1], 0)
		GPIO.output(self.m3[2], 1)
			
		GPIO.output(self.m4[0], 1)
		GPIO.output(self.m4[1], 0)
		GPIO.output(self.m4[2], 1)	

	def stop(self):
		GPIO.output(self.m1[0], 0)
		GPIO.output(self.m1[1], 0)
		GPIO.output(self.m1[2], 0)
			
		GPIO.output(self.m2[0], 0)
		GPIO.output(self.m2[1], 0)
		GPIO.output(self.m2[2], 0)
			
		GPIO.output(self.m3[0], 0)
		GPIO.output(self.m3[1], 0)
		GPIO.output(self.m3[2], 0)
			
		GPIO.output(self.m4[0], 0)
		GPIO.output(self.m4[1], 0)
		GPIO.output(self.m4[2], 0)



	
	
	# Setup and Init
	def __init__(self):
		self.m1 = [5, 24, 27]	# en, pos, neg
		self.m2 = [17, 6, 22]
		self.m3 = [12, 23, 16]
		self.m4 = [25, 13, 18]
		
		GPIO.setup(self.m1[0], GPIO.OUT)
		GPIO.setup(self.m1[1], GPIO.OUT)
		GPIO.setup(self.m1[2], GPIO.OUT)
		GPIO.output(self.m1[0], 0)
		GPIO.output(self.m1[1], 0)
		GPIO.output(self.m1[2], 0)

		GPIO.setup(self.m2[0], GPIO.OUT)
		GPIO.setup(self.m2[1], GPIO.OUT)
		GPIO.setup(self.m2[2], GPIO.OUT)
		GPIO.output(self.m2[0], 0)
		GPIO.output(self.m2[1], 0)
		GPIO.output(self.m2[2], 0)
		
		GPIO.setup(self.m3[0], GPIO.OUT)
		GPIO.setup(self.m3[1], GPIO.OUT)
		GPIO.setup(self.m3[2], GPIO.OUT)
		GPIO.output(self.m3[0], 0)
		GPIO.output(self.m3[1], 0)
		GPIO.output(self.m3[2], 0)
		
		GPIO.setup(self.m4[0], GPIO.OUT)
		GPIO.setup(self.m4[1], GPIO.OUT)
		GPIO.setup(self.m4[2], GPIO.OUT)
		GPIO.output(self.m4[0], 0)
		GPIO.output(self.m4[1], 0)
		GPIO.output(self.m4[2], 0)
		
		print "MotoZero Shield initialised!"