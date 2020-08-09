import utime
from Maix import GPIO
from board import board_info
from fpioa_manager import fm

# register pin to gpiohs0, 
# arg force means force register no matter we have registered before or not
# if arg force=False(by default), register func will return a tuple that registered info,
#                                                           or return number 1
fm.register(board_info.LED_B, fm.fpioa.GPIO0, force=True) # 12 - blue led
fm.register(board_info.LED_G, fm.fpioa.GPIO1, force=True) # 13 - green led
fm.register(board_info.LED_R, fm.fpioa.GPIO2, force=True) # 14 - red led

fm.register(board_info.PIN9, fm.fpioa.GPIO7, force=True) # 8 - buzzer

fm.register(board_info.MIC_ARRAY_DATA3, fm.fpioa.GPIOHS0, force=True) # 20 - back panel 1
fm.register(board_info.MIC_ARRAY_DATA2, fm.fpioa.GPIOHS1, force=True) # 21 - back panel 2
fm.register(board_info.MIC_ARRAY_DATA1, fm.fpioa.GPIOHS2, force=True) # 22 - back panel 3

fm.register(board_info.MIC_ARRAY_DATA0, fm.fpioa.GPIOHS3, force=True) # 23 - pump/sv
fm.register(board_info.MIC_ARRAY_LED, fm.fpioa.GPIOHS4, force=True) # 24 - laser


fm.register(board_info.PIN15, fm.fpioa.GPIO3, force=True) # 15 - trig_dispensor
fm.register(board_info.PIN17, fm.fpioa.GPIO4, force=True) # 17 - echo_dsipenser
fm.register(board_info.MIC_ARRAY_BCK, fm.fpioa.GPIO5, force=True) # 18 - trig temp
fm.register(board_info.MIC_ARRAY_WS, fm.fpioa.GPIO6, force=True) # 19 - echo temp


led_b = GPIO(GPIO.GPIO0, GPIO.OUT)
led_r = GPIO(GPIO.GPIO1, GPIO.OUT)
led_g = GPIO(GPIO.GPIO2, GPIO.OUT)


trig_desp = GPIO(GPIO.GPIO3, GPIO.OUT)
echo_desp = GPIO(GPIO.GPIO4, GPIO.OUT)
trig_temp = GPIO(GPIO.GPIO5, GPIO.OUT)
echo_temp = GPIO(GPIO.GPIO6, GPIO.OUT)

buzzer = GPIO(GPIO.GPIO7, GPIO.OUT)

panel1 = GPIO(GPIO.GPIOHS0, GPIO.OUT)
panel2 = GPIO(GPIO.GPIOHS1, GPIO.OUT)
panel3 = GPIO(GPIO.GPIOHS2, GPIO.OUT)

pump = GPIO(GPIO.GPIOHS3, GPIO.OUT)
laser = GPIO(GPIO.GPIOHS4, GPIO.OUT)

DISABLE=0
ENABLE=1

while True:
    buzzer.value(DISABLE)
    utime.sleep_ms(200)
    buzzer.value(ENABLE)

    led_r.value(DISABLE)
    utime.sleep_ms(200)
    led_r.value(ENABLE)
    
    led_b.value(DISABLE)
    utime.sleep_ms(200)
    led_b.value(ENABLE)

    led_g.value(DISABLE)
    utime.sleep_ms(200)
    led_g.value(ENABLE)
    
    trig_desp.value(DISABLE)
    utime.sleep_ms(200)
    trig_desp.value(ENABLE)
    
    echo_desp.value(DISABLE)
    utime.sleep_ms(200)
    echo_desp.value(ENABLE)
    
    trig_temp.value(DISABLE)
    utime.sleep_ms(200)
    trig_temp.value(ENABLE)
    
    echo_temp.value(DISABLE)
    utime.sleep_ms(200)
    echo_temp.value(ENABLE)
    
    panel1.value(DISABLE)
    utime.sleep_ms(200)
    panel1.value(ENABLE)
    
    panel2.value(DISABLE)
    utime.sleep_ms(200)
    panel2.value(ENABLE)
    
    panel3.value(DISABLE)
    utime.sleep_ms(200)
    panel3.value(ENABLE)
    
    pump.value(DISABLE)
    utime.sleep_ms(200)
    pump.value(ENABLE)
    
    laser.value(DISABLE)
    utime.sleep_ms(200)
    laser.value(ENABLE)
    
    utime.sleep_ms(200)
    
