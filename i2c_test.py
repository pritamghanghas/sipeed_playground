from machine import I2C
from Maix import GPIO
from board import board_info
from fpioa_manager import fm
import time

# i2c = I2C(I2C.I2C0, freq=100000, scl=28, sda=29)

fm.register(board_info.PIN10, fm.fpioa.I2C0_SCLK) # pin 10
fm.register(board_info.PIN11, fm.fpioa.I2C0_SDA) # pin 11
Fpioa = FPIOA()
Fpioa.set_function(board_info.PIN10, fm.fpioa.I2C0_SCLK) # pin 10
Fpioa.set_function(board_info.PIN11, fm.fpioa.I2C0_SDA) # pin 11

# i2c = I2C(I2C.I2C2, mode=I2C.MODE_MASTER, freq=1000000, scl=board_info.SPI0_MOSI, sda=board_info.SPI0_CS0)

i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=100000, scl=board_info.PIN10, sda=board_info.PIN11)
time.sleep_ms(500)
devices = i2c.scan()
print(devices)

i2c.deinit()
i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=10000, scl=28, sda=29)
time.sleep_ms(500)
devices = i2c.scan()
print(devices)

i2c.deinit()
i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=20000, scl=28, sda=29)
time.sleep_ms(500)
devices = i2c.scan()
print(devices)

i2c.deinit()
i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=50000, scl=28, sda=29)
time.sleep_ms(500)
devices = i2c.scan()
print(devices)

# i2c.deinit()
# i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=100000, scl=29, sda=28)
# time.sleep_ms(500)
# devices = i2c.scan()
# print(devices)


# i2c.deinit()
# i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=100000, scl=29, sda=28)
# time.sleep_ms(500)
# devices = i2c.scan()
# print(devices)