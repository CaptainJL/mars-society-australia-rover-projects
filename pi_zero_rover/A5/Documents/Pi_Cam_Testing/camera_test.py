# PYTHON RPI CAMERA CAPTURE
# based on GPIO high/low input


# imports
import time                 
import picamera
import RPi.GPIO as GPIO

# setup classes and modes
camera = picamera.PiCamera()

# GPIO setup
sig_pin = 16    # BCM pin for input
GPIO.setmode(GPIO.BCM)
GPIO.setup(sig_pin, GPIO.IN)

# counter for image + timing components
time_p = time.time()
time_d = 0

# image and counters
ctr = 0
end = ".jpg"
img = str(ctr) + end

# main loop for image capture
while 1:

    if GPIO.input(sig_pin):
        print "request recognised"
        
        img = str(ctr) + end
        camera.capture(img)
        ctr = ctr+1     # raise image counter to stop overwriting of images

        time_d = 1 - (time.time()-time_p)
        time.sleep(time_d)  # 1s intervals if image recieved
        # Note: images take 0.55s to save (at default resolution)
        
    else:
        print "no request"
        time.sleep(0.001)   # 1ms intervals if not recieved, to respond asap to request

    time_p = time.time()

    




#camera.capture('aye.jpg')


