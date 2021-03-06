import sys
import serial
import socket
import time
from const import *

BLACK = (0, 0, 0)
RED = (0xff, 0, 0)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'socket':
        setattr(socket.socket, 'write', socket.socket.sendall)
        matrix = socket.socket()
        matrix.connect(('localhost', PORT))
    else:
        matrix = serial.Serial(PATH, BAUD)
        time.sleep(5)

    leds = [[BLACK]*WIDTH for _ in range(HEIGHT)]
    while True:
        for x in range(HEIGHT):
            for y in range(WIDTH):
                b = b''
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        if (i, j) == (x, y):
                            b += bytes(RED)
                        else:
                            b += bytes(BLACK)
                matrix.write(b)
                time.sleep(0.1)


if __name__ == '__main__':
    main()
