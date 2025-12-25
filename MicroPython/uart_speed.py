from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
from pybricks.iodevices import UARTDevice
u=UARTDevice(Port.A)
u.set_baudrate(115200)

i=0
while True:
    wait(10)
    i+=1
    if i>255:
        i=0
    b=bytes([i])+b'abcdefghijklmnopqrstuvwxyz'
    u.write(b)
    if u.waiting()>0:
        r=u.read_all()
        print(r[0])
    
