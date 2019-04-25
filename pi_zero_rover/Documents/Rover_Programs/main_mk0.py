# MAIN MK0
import time

# MLX Temp Sensor Setup
from mlx90614 import MLX90614
mlx90614_address = 0x5a
mlxsensor = MLX90614(mlx90614_address)

# Monster Motor Shield Setup
from monster_ms import MONSTER_MS
motor = MONSTER_MS()

# EnviroPHAT Setup
from envirophat import weather
from envirophat import light
from envirophat import leds
from envirophat import motion
from envirophat import analog





# FUNCTIONS
def forward():
    print "f"
    motor.forward(0,90)
    motor.forward(1,90)

def reverse():
    print "r"
    motor.reverse(0,90)
    motor.reverse(1,90)

def left():
    print "l"
    motor.reverse(0,50)
    motor.forward(1,50)

def right():
    print "r"
    motor.forward(0,50)
    motor.reverse(1,50)

def stop():
    print "s"
    motor.stop()

def log():
    ctr = 0
    logfile = open('log.txt','w')
    print "mlx_obj_temp,envphat_temp,envphat_light"
    logfile.write("mlx_obj_temp,envphat_temp,envphat_light\n")
    while ctr<50:
        mt = mlxsensor.get_obj_temp()
        et = weather.temperature()
        el = light.light()
        print mt,",",et,",",el
        logfile.write("%s,%s,%s\n"%(mt,et,el))
        ctr+=1
        time.sleep(0.02)
        












# MAIN

# Variables
count_dt = 1
counter = 0

# Setup Commands
print "Type commands"
print "W: FORWARD"
print "S: REVERSE"
print "A: LEFT (45o)"
print "D: RIGHT (45o)"
print "Z: HOLD/STOP"
print "L: LOG (50 samples, 20ms steps)"

# main loop
while 1:
    
    counter=0
    # get command
    modesel = raw_input("Designate Input:   ")
    modelen = len(modesel)
    mode    = modesel[0]

    # Process Loop
    while counter<modelen:
        
        if mode=="W":
            forward()
        elif mode=="S":
            reverse()
        elif mode=="A":
            left()    
        elif mode=="D":
            right()
        elif mode=="Z":
            stop()
            break
        elif mode=="L":
            log()
            break
        else:
            print "incorrect command!"
            break
            
        counter+=1

        time.sleep(count_dt)
        












    
