import smbus
import time
bus = smbus.SMBus(1)
address = 0x4c


data = bus.read_byte_data(address, 1)
print data
data = bus.read_byte_data(address, 2)
print data
