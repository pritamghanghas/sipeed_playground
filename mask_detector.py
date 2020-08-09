#tested with frimware 5-0.22
import sensor,image,lcd,time
from machine import I2C
import KPU as kpu
import mlx90614

textScale = 2
rectThickness = 10

lcd.init()
lcd.clear(0xFFFF)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_brightness(2)
# sensor.set_auto_gain(1)
# sensor.set_saturation(2)
sensor.set_contrast(2)
sensor.set_vflip(1)
# sensor.set_hmirror(1)
sensor.run(1)
classes = ["Mask", "No Mask"]
colors = [(0,255,0), (255,0,0)]
#task = kpu.load(0x200000) #change to "/sd/name_of_the_model_file.kmodel" if loading from SD card
task = kpu.load('/sd/mask20.kmodel')
a = kpu.set_outputs(task, 0, 7,7,35)   #the actual shape needs to match the last layer shape of your model(before Reshape)
anchor = (0.57273, 0.677385, 1.87446, 2.06253, 3.33843, 5.47434, 7.88282, 3.52778, 9.77052, 9.16828)
a = kpu.init_yolo2(task, 0.6, 0.05, 5, anchor) #tweak the second parameter if you're getting too many false positives
clock = time.clock()
lcd.direction(lcd.YX_RLDU)


i2c = I2C(I2C.I2C0, mode=I2C.MODE_MASTER, freq=100000, scl=10, sda=11, addr_size=7)
temp_sensor = mlx90614.MLX90614(i2c)

while(True):
    #img = sensor.snapshot().rotation_corr(z_rotation=-90.0)
    img = sensor.snapshot()
    a = img.pix_to_ai()
    clock.tick()
    code = kpu.run_yolo2(task, img)
    fps=clock.fps()
    # print(fps)
    # code = None
    if code:
        # print("network found something")
        for i in code:
            selectedColor = colors[i.classid()]
            label = classes[i.classid()]
            class_length = len(label)
            labelPosX = int((224-(class_length*textScale*4))/2)
            labelPosY = 10
            # print(i.rect(), labelPosX, labelPosY)
            a = img.draw_rectangle(i.rect(), thickness=rectThickness, color=selectedColor)
            a = img.draw_string(labelPosX, labelPosY, label, color=selectedColor, scale=textScale)
    else:
        # print("network found nothing")
        pass
    objTemp = temp_sensor.read_object_temp()
    if temp_sensor.isHumanTemp(objTemp):
        temp_str = "{:.2f}".format(objTemp)
        print(temp_str)
        img.draw_string(80, 200, temp_str, colors[1], scale=textScale)
    else:
        print("non human temp")
    
    a = lcd.display(img)
a = kpu.deinit(task)
