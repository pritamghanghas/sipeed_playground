from machine import Pin, I2C
import time
import mlx90614

i2c = I2C(scl=Pin(5), sda=Pin(4))

sensor = mlx90614.MLX90614(i2c)

while True:
	print(sensor.read_ambient_temp(), sensor.read_object_temp())
	time.sleep_ms(500)