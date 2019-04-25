from threading import Thread
import time
from datetime import datetime
from envirophat import weather
from envirophat import motion
from motozero_class import MotoZero
from ADCPi import ADCPi
from mlx90614 import MLX90614
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

cmd_val = "s"
cmd_time = 0
global start_time


motors = 	MotoZero()
adc =		ADCPi(0x68, 0x69, 12)
mlx90614_address = 0x5a
mlxsensor = MLX90614(mlx90614_address)


def log():
	global cmd_val
	global cmd_time
	global start_time
	file = open('rover.csv','w')
	file.write('time,command,temp_ambient,ax,ay,az,compass,mlx_amb,mlx_obj,motor_current_m1,motor_current_m2\n')
	ax,ay,az = motion.accelerometer()
	time.sleep(0.1)
	while True:
    		ax,ay,az = motion.accelerometer()
    		time_now = datetime.now()-start_time    # OLD = (time.strftime('%M:%S')
    		time_print = float(time_now.seconds*1000000 + time_now.microseconds)/1000000.0
    		file.write('%0.6f,%s,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f\n' % (time_print,cmd_val[0],weather.temperature(),9.81*ax,9.81*ay,9.81*az,motion.heading(),mlxsensor.get_amb_temp(),mlxsensor.get_obj_temp(),adc.read_voltage(0),adc.read_voltage(7)))
    		time.sleep(0.1)
    		
    		# break if commanded
		if cmd_val == "exit":
			file.close()
			break



def cmd_act(time_ctrl,cmd):

	time_s = time.time()
	while True:
		if (time.time()-time_s >= time_ctrl):
			motors.stop()
			break
		elif (cmd == 'w'):
			motors.forward()
		elif (cmd == 'z'):
			motors.reverse()
		elif (cmd == 'a'):
			motors.left()
		elif (cmd == 'd'):
			motors.right()
		elif (cmd == 's'):
			motors.stop()
			break
		else:
			print 'null cmd'
			break
		
		time.sleep(0.1)




def controller():
	global cmd_val
	global cmd_time
	time.sleep(2)
	val = cmd_val
	while True:
		if val != cmd_val:
			print str(cmd_val[0])
			print str(cmd_time)
			val = cmd_val
			
			# break if commanded
			if cmd_val == "exit":
				break
				
			print 'start'
			cmd_act(cmd_time,cmd_val[0])
			print 'end'
						
		time.sleep(0.1)
		
		

def commander():
	global cmd_val
	global cmd_time
	print "aye from cmd"
	time.sleep(1)

	while True:
		cmd_val = raw_input('> ')
		cmd_time = 0.25*len(cmd_val)
				
		# break if commanded
		if cmd_val == "exit":
			break
		
		time.sleep(0.5)
	
	time.sleep(1.0)
	GPIO.cleanup() 		


def main():
	global cmd_val
	global cmd_time
	global start_time
	start_time = datetime.now()

	log_thread = 	Thread(target=log)
	cmd_thread = 	Thread(target=commander)
	ctrl_thread = 	Thread(target=controller)
	log_thread.start()
	cmd_thread.start()
	ctrl_thread.start()


if __name__ == "__main__":
   	main()
