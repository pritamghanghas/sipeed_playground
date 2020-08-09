import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

# register pin to gpiohs0, 
# arg force means force register no matter we have registered before or not
# if arg force=False(by default), register func will return a tuple that registered info,
#                                                           or return number 1
fm.register(board_info.LED_R, fm.fpioa.GPIO0, force=True)
fm.register(board_info.LED_G, fm.fpioa.GPIOHS0, force=True)
fm.register(board_info.LED_B, fm.fpioa.GPIO1, force=True)

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_g = GPIO(GPIO.GPIOHS0, GPIO.OUT)
led_b = GPIO(GPIO.GPIO1, GPIO.OUT)

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

fm.unregister(board_info.LED_R, fm.fpioa.GPIO0)
fm.unregister(board_info.LED_G, fm.fpioa.GPIOHS0)
fm.unregister(board_info.BOOT_KEY, fm.fpioa.GPIO1)

