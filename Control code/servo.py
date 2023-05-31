
import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
while True:
    pos = input("Position: ")
    ser.write(str(pos).encode())
    read = str(ser.readline())     
    time.sleep(1)
    print(read)
