import time
from datetime import datetime
from threading import Thread
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)



## TIME TESTING - prints in float (microsecond accuracy)
#t_s = datetime.now()
#time.sleep(3.14)
#t_n = datetime.now()-t_s
#print (float(t_n.seconds*1000000 + t_n.microseconds)/1000000)


motorspeed_pin = 26
test_pin = 20
GPIO.setup(motorspeed_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(test_pin, GPIO.OUT)


global last_time
global cnt


def trigger(channel):
    global last_time
    global cnt
    since_last = datetime.now()-last_time
    since_lf = float(since_last.seconds*1000000 + since_last.microseconds)/1000000.0
    
    if (since_lf > 0.25):
    	print "triggered with dt: " + str(since_lf)
    	last_time = datetime.now()
    	cnt = cnt+1
    
    



def main():
    global last_time
    global cnt
    cnt = 0
    time_start = datetime.now()
    last_time = time_start
    
    
    GPIO.add_event_detect(motorspeed_pin,GPIO.FALLING, callback=trigger, bouncetime=1)
 	#, bouncetime=3

    while(1):
        time.sleep(0.01)

        GPIO.output(test_pin,1)
        time.sleep(0.01)
        GPIO.output(test_pin,0)
        
       
        
       











if __name__ == "__main__":
    main()
