# Import EnvirPhat components
from envirophat import weather
from envirophat import light
from envirophat import leds
from envirophat import motion
from envirophat import analog
import time


# Import ADC Pi Zero components
#from ABE_ADCPi import ADCPi
#from ABE_helpers import ABEHelpers
 
# Envirophat tests
print light.light()
print light.rgb()
leds.on()
time.sleep(3)
leds.off()
print weather.temperature()


  

# Init I2C for ADC Pi Zero + read
#i2c_helper = ABEHelpers()
#bus = i2c_helper.get_smbus()
#adc = ADCPi(bus, 0x68, 0x69, 18)
#adc.read_voltage(1)
