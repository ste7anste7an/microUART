from microuart import MicroUART
from neopixel import NeoPixel
from machine import Pin

lednr=0

def led(updown):
    global lednr
    lednr=(lednr+updown)%9
    np.fill((0,0,0))
    np[lednr]=(10,0,0)
    np.write()

u = MicroUART()   # UART1, RX=16, TX=17

np=NeoPixel(Pin(21),9)

while True:
    u.process()
