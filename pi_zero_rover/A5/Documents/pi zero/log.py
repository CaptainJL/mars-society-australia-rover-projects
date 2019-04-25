# LOGGING DATA of the ROVER

# Imports
import time
from envirophat import analog
from envirophat import light
from envirophat import weather
from envirophat import motion


# Setup data file
file = open('rover.csv','w')
file.write('time,temp_ambient,ax,ay,az,compass,motor_current\n')



ax,ay,az = motion.accelerometer()
time.sleep(0.1)


for i in xrange(1,10):
    ax,ay,az = motion.accelerometer()
    file.write('%s,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f\n' % (time.strftime('%M:%S'),weather.temperature(),9.81*ax,9.81*ay,9.81*az,motion.heading(),analog.read(0)))
    time.sleep(0.1)

