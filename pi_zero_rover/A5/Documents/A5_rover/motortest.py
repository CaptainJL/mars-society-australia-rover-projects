from threading import Thread
import time
from datetime import datetime
from motozero_class import MotoZero



motors = 	MotoZero()




time_start = datetime.now()
time_total = 5.0

t_now = datetime.now()-time_start
t_n_f = float(t_now.seconds*1000000 + t_now.microseconds)/1000000

while (t_n_f < time_total):
	motors.forward()
	time.sleep(0.01)
	t_now = datetime.now()-time_start
	t_n_f = float(t_now.seconds*1000000 + t_now.microseconds)/1000000
	
motors.stop()
GPIO.cleanup() 
print "ended"


