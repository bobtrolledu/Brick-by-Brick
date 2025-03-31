import curses
#from RPi.GPIO import Motor, PWMOutputDevice
from gpiozero import Motor, PWMOutputDevice
import time

class Vehicle:
    def __init__(self):
        self.left_motor = Motor(forward = 3,backward = 4)
        self.left_pwm = PWMOutputDevice(18)
        self.left_pwm.value = 0

    def forward(self):
        self.left_motor.forward()
        self.left_pwm.value = 0.85

    def backward(self):
        self.left_motor.backward()
        self.left_pwm.value = 0.5

def pulse(num_pulses):
    rpi_vehicle = Vehicle()

    for i in range(num_pulses):
        rpi_vehicle.forward()
        time.sleep(0.5)
        rpi_vehicle.left_pwm.value = 0
        time.sleep(1)

    
if __name__ == "__main__":
    pulse(120)


    rpi_vehicle.left_pwm.value = 0
    time.sleep(2)