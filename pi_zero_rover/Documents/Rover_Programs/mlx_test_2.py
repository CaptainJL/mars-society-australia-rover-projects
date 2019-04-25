# MAIN Test 1




from mlx90614 import MLX90614
from monster_ms import MONSTER_MS 

mlx90614_address = 0x5a

motor = MONSTER_MS()
mlxsensor = MLX90614(mlx90614_address)

print "ambient_temp: ", mlxsensor.get_amb_temp()
print "object_temp:  ", mlxsensor.get_obj_temp() 

motorsel = raw_input("motor 0 or 1?  ")
print motorsel

motor.forward(motorsel,50)
motor.forward(motorsel,50)
motor.stop()
