import time
import serial
from math import pi
import numpy
import socket

import serial
import time
import waypoints as wp
import kg_robot as kgr


def main():
    print("------------Configuring Burt-------------\r\n")
    burt = kgr.kg_robot(port=30010,db_host="169.254.23.126")
    #burt = kgr.kg_robot(port=30010,ee_port="COM32",db_host="192.168.1.51")
    print("----------------Hi Burt!-----------------\r\n\r\n")

    ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
    # pos = 45

    # ser.write(str(pos).encode())
    # read = str(ser.readline())     
    # time.sleep(1)
    # print(read)

    
    burt.translatejl_rel([0.0,-0.055,-0.02,0,0.0,-0.11], acc=0.5, vel=0.2)
    # burt.translatejl_rel([0.0,0.0,-0.0
    # 5,0,0.0,0], acc=0.5, vel=0.2)
    burt.translatejl_rel([0.0,0.0,-0.188,0,0.0,0], acc=0.5, vel=0.2)


    pos = 75

    ser.write(str(pos).encode())
    read = str(ser.readline())     
    time.sleep(1)
    print(read)
    burt.translatel_rel([0.0,0,0.07], acc=0.2, vel=0.2)
    burt.translatel_rel([0.0,-0.1,0], acc=0.2, vel=0.2)

    
    burt.translatel_rel([0.0,0.0,-0.054], acc=0.2, vel=0.2)

    time.sleep(3)

    pos = 50
    ser.write(str(pos).encode())
    read = str(ser.readline())     
    time.sleep(1)
    print(read)

    burt.translatel_rel([0.0,0.0,0.05], acc=0.2, vel=0.2)



        
    burt.close()
if __name__ == '__main__': main()

# 