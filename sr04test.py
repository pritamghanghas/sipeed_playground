import time
from pinsetup import setupPins
from hcsr04 import HCSR04
from fpioa_manager import fm
from Maix import GPIO
from board import board_info

# setupPins()
fm.register(board_info.PIN15, fm.fpioa.GPIO3, force=True) # 15 - trig_dispensor
fm.register(board_info.PIN17, fm.fpioa.GPIO4, force=True) # 17 - echo_dsipenser

dispSensor = HCSR04(GPIO.GPIO3, GPIO.GPIO4) # disp
# tempSensor = HCSR04(GPIO.GPIO5, GPIO.GPIO6) # temp

while True:
    # print("measuring disp distance")
    dispDistance = dispSensor.distance_cm()
    # print("measuring temp distance")
    # tempDistance = tempSensor.distance_cm()
    # print("done measuring temp distance")

    if dispDistance < 0: 
        print("time out occured")
    
    if dispDistance > 2: # and (dispDistance < 50):
        print('Dispensor Distance:', dispDistance, 'cm')
    
    # if tempDistance > 2: #and (tempDistance < 10):
    #     print('Temp sensor Distance:', tempDistance, 'cm')
    
    time.sleep_ms(100)

# import machine, time
# #import utime
# from Maix import GPIO
# from board import board_info
# from fpioa_manager import fm
# from modules import ultrasonic

# fm.register(board_info.PIN15, fm.fpioa.GPIOHS0, force=True)

# device = ultrasonic(fm.fpioa.GPIOHS0)

# while True:
#     distance = device.measure(unit = ultrasonic.UNIT_CM, timeout = 3000000)
#     print(distance)
#     time.sleep_ms(100)
