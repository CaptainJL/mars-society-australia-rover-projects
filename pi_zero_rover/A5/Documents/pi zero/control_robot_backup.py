from threading import Thread
import time
from envirophat import analog
from envirophat import light
from envirophat import weather
from envirophat import motion
from monster_ms import MONSTER_MS



cmd_val = "s"
cmd_time = 0


motors = MONSTER_MS()


def log():
	global cmd_val
	global cmd_time
	file = open('rover.csv','w')
	file.write('time,command,temp_ambient,ax,ay,az,compass,motor_current_m1,motor_current_m2\n')
	ax,ay,az = motion.accelerometer()
	time.sleep(0.1)
	while True:
    		ax,ay,az = motion.accelerometer()
    		file.write('%s,%s,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f\n' % (time.strftime('%M:%S'),cmd_val[0],weather.temperature(),9.81*ax,9.81*ay,9.81*az,motion.heading(),analog.read(0),analog.read(1)))
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
			motors.forward(0,80)
			motors.forward(1,80)
		elif (cmd == 'z'):
			motors.reverse(0,80)
			motors.reverse(1,80)
		elif (cmd == 'a'):
			motors.forward(0,80)
			motors.reverse(1,80)
		elif (cmd == 'd'):
			motors.reverse(0,80)
			motors.forward(1,80)
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
			


def main():
	global cmd_val
	global cmd_time

	log_thread = 	Thread(target=log)
	cmd_thread = 	Thread(target=commander)
	ctrl_thread = 	Thread(target=controller)
	log_thread.start()
	cmd_thread.start()
	ctrl_thread.start()


if __name__ == "__main__":
   	main()