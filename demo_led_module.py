import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

# register pin to gpiohs0, 
# arg force means force register no matter we have registered before or not
# if arg force=False(by default), register func will return a tuple that registered info,
#                                                           or return number 1
fm.register(20, fm.fpioa.GPIO4, force=True)
fm.register(21, fm.fpioa.GPIO5, force=True)

led_r = GPIO(GPIO.GPIO4, GPIO.OUT)
led_g = GPIO(GPIO.GPIO5, GPIO.OUT)

i = 0
status = 0
while i<2000:
    color = i%3
    if color == 0:
        led_r.value(0)
    else:
        led_r.value(1)
    if color == 1:
        led_g.value(0)
    else:
        led_g.value(1)
    if color == 2:
        led_g.value(0)
    else:
        led_g.value(1)
    i+=1
    utime.sleep_ms(500)

fm.unregister(20, fm.fpioa.GPIO4)
fm.unregister(21, fm.fpioa.GPIO5)

