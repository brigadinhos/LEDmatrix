import sys
import serial
import time
import socket
import string
import math

def xy_convert_vertical(x, y):

    if y % 2 != 0:
        return (y*10 + x)
    else:
        return (y*10 + 9 - x)

def xy_convert_horizontal( x, y):

     if x % 2 == 0:
         return (x*10 + y)
     else:
         return (x*10 + 9 - y)
#def vec_conv
def main():
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 9500               # Arbitrary non-privileged port
    li = []

    li.extend(range(0, 600))
    for i in range(600):
      li[i] = 0
    ser = serial.Serial('/dev/cu.usbmodemFD121',115200);
    #for i in range(10):
    #just to clean buffer and matrix
    for i in range(10):
      ser.write(bytearray(li))
      time.sleep(0.5);


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print("go listen")
        conn, addr = s.accept()
        print("accept")
        with conn:
            print('Connected by', addr)
            #orientation = conn.recv(1024)
            while True:
                input_msg = conn.recv(10000)
                #print(input_msg)
                clean_msg = input_msg.decode("UTF-8").split("|", 600)
                #print(clean_msg)
                #for i in range(600):
                #    print(clean_msg[i])
                #    UTF-8
                if (len(clean_msg)>=600):
                    for i in range(200):
                        line = int(i / 10)
                        column = int(i % 10)
                        matrix_index = int(xy_convert_vertical(column, line))
                        li[matrix_index*3] = int(clean_msg[i*3]);
                        li[matrix_index*3+1] = int(clean_msg[i*3+1]);
                        li[matrix_index*3+2] = int(clean_msg[i*3+2]);

                    ser.write(bytearray(li))

    ser.close()
# this is the standard boilerplate that calls the main() function
if __name__ == '__main__':
    # sys.exit(main(sys.argv)) # used to give a better look to exists
    main()
