from microuart import MicroUART
from time import ticks_ms,sleep_ms
u = MicroUART()   # UART1, RX=16, TX=17


s=ticks_ms()
i=0
for j in range(100):
    #uu.send_command('test',i,i+2)
    #cmd,data=uu.receive_command()
    cmd,data = u.call('test',i,i+2)
    #print(cmd,data)
    #sleep_ms(20)
    #wait(1)
    i+=1
    if i> 255:
        i=0

print(ticks_ms()-s)
