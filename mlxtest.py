import time
import mlx90614
from machine import I2C
import utime
# from Maix import GPIO
# from board import board_info
# from fpioa_manager import fm

# fm.register(board_info., fm.fpioa.GPIO0, force=True)
# fm.register(board_info.LED_G, fm.fpioa.GPIOHS0, force=True)
# fm.register(board_info.LED_B, fm.fpioa.GPIO1, force=True)

# led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
# led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)
# led_b = GPIO(GPIO.GPIO1, GPIO.OUT)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=100000, scl=10, sda=11, addr_size=7)
time.sleep_ms(500)
devices = i2c.scan()
print(devices)
sensor = mlx90614.MLX90614(i2c)

while True:
	print(sensor.read_ambient_temp(), sensor.read_object_temp())
	time.sleep_ms(500)