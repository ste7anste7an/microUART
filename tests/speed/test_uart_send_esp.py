from microremote import MicroRemote
from time import ticks_ms,sleep_ms
ur=MicroRemote()

s=ticks_ms()
i=0
for j in range(100):
    #ur.send_command('test',i,i+2)
    #cmd,data = ur.receive_command()
    cmd,data = ur.call('test',i,i+2)
    #print(cmd,data)
    #sleep_ms(20)
    #wait(1)
    i+=1
    if i> 255:
        i=0

print(ticks_ms()-s)
