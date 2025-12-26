from microuart import MicroUART
from time import ticks_ms,sleep_ms
u = MicroUART()   # UART1, RX=16, TX=17


def test(a,b):
    print("test",a,b)
    return a==b,a+b,a*3

i=0
while True:
    u.process()
    i+=1
    if i> 1000:
        i=0
    
