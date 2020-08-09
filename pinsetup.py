from board import board_info
from fpioa_manager import fm

# register pin to gpiohs0, 
# arg force means force register no matter we have registered before or not
# if arg force=False(by default), register func will return a tuple that registered info,
#                                                           or return number 1
def setupPins():
    # lighting pin setup
    fm.register(board_info.LED_B, fm.fpioa.GPIO0, force=True) # 12 - blue led
    fm.register(board_info.LED_G, fm.fpioa.GPIO1, force=True) # 13 - green led
    fm.register(board_info.LED_R, fm.fpioa.GPIO2, force=True) # 14 - red led

    #buzzer pin setup
    fm.register(board_info.PIN9, fm.fpioa.GPIO7, force=True) # 8 - buzzer

    # back panel gpio setup
    fm.register(board_info.MIC_ARRAY_DATA3, fm.fpioa.GPIOHS0, force=True) # 20 - back panel 1
    fm.register(board_info.MIC_ARRAY_DATA2, fm.fpioa.GPIOHS1, force=True) # 21 - back panel 2
    fm.register(board_info.MIC_ARRAY_DATA1, fm.fpioa.GPIOHS2, force=True) # 22 - back panel 3

    # pump and laser control
    fm.register(board_info.MIC_ARRAY_DATA0, fm.fpioa.GPIOHS3, force=True) # 23 - solenoid control
    fm.register(board_info.MIC_ARRAY_LED, fm.fpioa.GPIOHS4, force=True) # 24 - laser led control

    # gesture sonic pins
    fm.register(board_info.PIN15, fm.fpioa.GPIO3, force=True) # 15 - trig for gesture
    fm.register(board_info.PIN17, fm.fpioa.GPIO4, force=True) # 17 - echo for gesture
    
    #temp sonic pins
    fm.register(board_info.MIC_ARRAY_BCK, fm.fpioa.GPIO5, force=True) # 18 - trig temp
    fm.register(board_info.MIC_ARRAY_WS, fm.fpioa.GPIO6, force=True) # 19 - echo temp

