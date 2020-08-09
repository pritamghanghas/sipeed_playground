import enum

class TempUnit(enum.Enum):
    KELVIN = 0
    CELCIUS = 1
    FARNHEIGHT = 2

class mlx90614:
    def __init__(self):
        self.unit = TempUnit.CELCIUS
        self.temp = 320
    
    def read_temp(self):
        if self.unit == TempUnit.FARNHEIGHT:
            return (self.temp - 273.15) * 9/5 + 32
        elif self.unit == TempUnit.CELCIUS:
            return (self.temp - 273.15)
        else: # if kelvin or something else
            return self.temp
    
    def set_unit(self, unit):
        self.unit = unit
    

if __name__ == '__main__':
    sensor = mlx90614()
    print("sensor temp in celcius {:.2f}".format(sensor.read_temp()))
    sensor.set_unit(TempUnit.FARNHEIGHT)
    print("sensor temp in farnheight {}".format(sensor.read_temp()))
    sensor.set_unit(TempUnit.CELCIUS)
    print("sensor temp in celcius {}".format(sensor.read_temp()))
    sensor.set_unit(TempUnit.KELVIN)
    print("sensor temp in kelvin {}".format(sensor.read_temp()))