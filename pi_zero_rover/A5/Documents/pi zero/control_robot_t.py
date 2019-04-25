from threading import Thread
import time
from envirophat import analog
from envirophat import light
from envirophat import weather
from envirophat import motion
from motor_shield_class import Monster_Motor_Shield



cmd_val = "s"
cmd_time = 0


motor_0 = Monster_Motor_Shield(12, 22, 23, 6)


def log():
	file = open('rover.csv','w')
	file.write('time,temp_ambient,ax,ay,az,compass,motor_current\n')
	ax,ay,az = motion.accelerometer()
	time.sleep(0.1)
	for i in xrange(1,10):
    		ax,ay,az = motion.accelerometer()
    		file.write('%s,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f\n' % (time.strftime('%M:%S'),weather.temperature(),9.81*ax,9.81*ay,9.81*az,motion.heading(),analog.read(0)))
    		time.sleep(0.1)
    		
    		# break if commanded
		if cmd_val == "exit":
			break

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
			
		time.sleep(0.1)
		
		

def commander():
	global cmd_val
	global cmd_time
	print "aye from cmd"
	time.sleep(1)

	while True:
		cmd_val = raw_input('> ')
		cmd_time = 1.0*len(cmd_val)
				
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