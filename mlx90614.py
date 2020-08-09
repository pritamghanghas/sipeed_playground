"""
MicroPython MLX90614 IR temperature sensor driver
https://github.com/mcauser/micropython-mlx90614

MIT License
Copyright (c) 2016 Mike Causer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import ustruct

_REGISTER_TA = const(0x06)     # ambient
_REGISTER_TOBJ1 = const(0x07)  # object
_REGISTER_TOBJ2 = const(0x08)  # object2

_TEMP_HUMAN_MIN = const(96)
_TEMP_HUMAN_MAX = const(105)

class TempratureUnit:
	KELVIN = 0
	CELCIUS = 1
	FAHRENHEIT = 2
	
class MLX90614:
	def __init__(self, i2c, address=0x5a, unit=TempratureUnit.FAHRENHEIT, correction_factor_fahrenheit=6.5): 
		self.temp_unit = unit
		self.i2c = i2c
		self.address = address
		self.correctio_factor_fahrenheit = correction_factor_fahrenheit
		_config1 = i2c.readfrom_mem(address, 0x25, 2)
		_dz = ustruct.unpack('<H', _config1)[0] & (1<<6)
		self.dual_zone = True if _dz else False

	def set_unit(self, unit):
		self.temp_unit = unit

	def read16(self, register):
		data = self.i2c.readfrom_mem(self.address, register, 2)
		return ustruct.unpack('<H', data)[0]

	def read_temp(self, register):
		temp = self.read16(register);
		# apply measurement resolution (0.02 degrees per LSB)
		temp *= .02;
		# appropirate conversion from kelvin
		if self.temp_unit == TempratureUnit.FAHRENHEIT:
			return (temp - 273.15) * 9/5 + 32 + self.correctio_factor_fahrenheit
		elif self.temp_unit == TempratureUnit.CELCIUS:
			return (temp - 273.15)
		else: # if kelvin or something else
			return temp

	def read_ambient_temp(self):
		return self.read_temp(_REGISTER_TA)

	def read_object_temp(self):
		return self.read_temp(_REGISTER_TOBJ1)

	def read_object2_temp(self):
		if self.dual_zone:
			return self.read_temp(_REGISTER_TOBJ2)
		else:
			raise RuntimeError("Device only has one thermopile")
	
	def isHumanTemp(self, recTemp):
		return (recTemp > _TEMP_HUMAN_MIN) and (recTemp < _TEMP_HUMAN_MAX)
	
	@property
	def ambient_temp(self):
		return self.read_ambient_temp()

	@property
	def object_temp(self):
		return self.read_object_temp()

	@property
	def object2_temp(self):
		return self.read_object2_temp()
