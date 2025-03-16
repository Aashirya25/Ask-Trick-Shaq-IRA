import serial
import time
  


arduino = serial.Serial("COM11", 9600)
time.sleep(2)

while True:
    if arduino.in_waiting > 0:
        message = arduino.readline().decode('utf-8').strip()
        print(message)
    
    user_input = input("Enter a number: ")

    arduino.write((user_input + "\n").encode())