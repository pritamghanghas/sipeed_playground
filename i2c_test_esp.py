from machine import Pin, I2C
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
time.sleep_ms(500)
devices = i2c.scan()
print(devices)
