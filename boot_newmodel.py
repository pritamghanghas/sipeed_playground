# refer to http://blog.sipeed.com/p/680.html
import sensor, image, lcd, time
import KPU as kpu
import gc as pgc

lcd.init()
lcd.clear()
try:
    img = image.Image("/sd/startup.jpg")
    lcd.display(img)
except:
    lcd.draw_string(lcd.width()//2-100,lcd.height()//2-4, "Error: Cannot find startup.jpg", lcd.WHITE, lcd.RED)

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
#sensor.set_windowing((224, 224))
#sensor.set_vflip(1)
#sensor.set_hmirror(1)
sensor.run(1)
#f=open('/sd/labels.txt','r')
#labels=f.readlines()
#f.close()
#task = kpu.load('/sd/facedetect_6672f87d1d082bee045e3150c59ba9da.smodel') 
task = kpu.load('/sd/new_model_float.kmodel')
#kpu.set_outputs(task, 0, None, None, 7)
lcd.clear(0xFFFF)
clock = time.clock()
while(True):
    print("staring new loop for processing image, beginnging with gc collect")
    pgc.collect()
    img = sensor.snapshot()
    img.rotation_corr(z_rotation=-90)
    clock.tick()
    print("before fmap")
    pgc.collect()
    fmap = kpu.forward(task, img)
    print(fmap)
    fps=clock.fps()
    #plist=fmap[:]
    #pmax=max(plist) 
    #max_index=plist.index(pmax) 
    a = lcd.display(img)
    #lcd.draw_string(48, 224, "%.2f:%s                            "%(pmax, labels[max_index].strip()))
    print(fps)
a = kpu.deinit(task)
