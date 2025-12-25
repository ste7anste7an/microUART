from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import ustruct
hub = PrimeHub()
from pybricks.iodevices import UARTDevice

# u=UARTDevice(Port.A,timeout=1000)
# u.set_baudrate(115200)

class MicroUART:
    def __init__(self,port,baudrate=115200,wait_recv=10000,uart_timeout=1000):
        self.wait_recv = wait_recv
        self.uart = UARTDevice(port,timeout=uart_timeout)
        self.uart.set_baudrate(baudrate)

    def send_bytes(self,b):
        b=bytes([len(b)])+b
        print(b)
        self.uart.write(b)

    def receive_bytes(self):
        s=StopWatch()
        while (s.time()<self.wait_recv) and self.uart.waiting()==0:
            pass
        if self.uart.waiting() > 0:
            l=self.uart.read(1)[0]
        else:
            self.uart.read_all()
            return 1,None
        print(l,"u.waiting",self.uart.waiting())
        b=self.uart.read(l)
        return b


    def encode(self, cmd, *argv):
        encoded=bytes([len(cmd)])+bytes(cmd,'utf-8')
        for arg in argv:
            if type(arg)==int:
                s=str(arg)
                encoded+=bytes([78,len(s)])+bytes(s,'utf-8')
            if type(arg)==bytes:
                encoded+=bytes([65,len(arg)])+arg
            if type(arg)==str:
                encoded+=bytes([83,len(arg)])+bytes(arg,'utf-8')
            if type(arg)==bool:
                b= 1 if arg==True else 0
                encoded+=bytes([66,1,b])
        return encoded

    def decode(self, encoded: bytes):
        len_cmd=encoded[0]
        cmd = str(encoded[1:len_cmd+1],'utf-8')
        decoded = []
        p = len_cmd+1
        while p < len(encoded):
            t = encoded[p]
            length = encoded[p + 1]
            p += 2

            payload = encoded[p:p + length]
            p += length
            if t == 78:          # N int
                decoded.append(int(str(payload,'utf-8')))
            elif t == 65:        # A bytes
                decoded.append(payload)
            elif t == 83:        # S str
                decoded.append(str(payload,'utf-8'))
            elif t == 66:        # B bool
                decoded.append(bool(payload[0]))
            else:
                raise ValueError(f"Unknown type code: {t}")

        return cmd,decoded


    def send_command(self,cmd,*data):
        b=self.encode(cmd,*data)
        print('b encoded',b)
        self.send_bytes(b)
        
    def receive_command(self):
        b=self.receive_bytes()
        if b!=None and len(b)>0:
            cmd,data=self.decode(b)
            return cmd,data
        else:
            return "!ERROR","no bytes received"



    def call(self,cmd,*data):
        self.send_command(cmd,data)
        return self.receive_command()


uu=MicroUART(Port.A)
print(uu.decode(uu.encode('cmd',2124,b'1234','hallo',True,5)))

# i=0
# s=b'\x40'+bytearray([i+65 for i in range(0x40)])
# while True:
#     send_str(i)
#     print(i)
#     i+=1
#     i%=32
#     wait(100)

uu.send_command('call',8888123,'hoi',b'1234',True)
while True:
    pass