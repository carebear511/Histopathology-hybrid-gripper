import time
import serial
from math import pi
import numpy as np
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

    # ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
    # pos = 45

    # ser.write(str(pos).encode())
    # read = str(ser.readline())     
    # time.sleep(1)
    # print(read)

    burt.translatel_rel([0.0,0.0,-0.17,0,0.0,0], acc=0.5, vel=0.2)
    burt.translatel_rel([-0.2,0.0,0,0,0.0,0], acc=0.5, vel=0.2)
    burt.translatel_rel([0,0.4,0,0,0.0,0], acc=0.5, vel=0.2)
    burt.translatel_rel([0.0,0.0,-0.205,0,0.0,0], acc=0.5, vel=0.2)
    burt.translatel_rel([-0.15,0.0,0,0,0.0,0], acc=0.5, vel=0.2)

    i = 0

    while True:
        burt.translatel_rel([0.0001,0.0,0,0,0.0,0], acc=0.01, vel=0.01)
        time.sleep(0.5)
        i+= 1
        print(i/10)

    burt.close()
if __name__ == '__main__': main()

