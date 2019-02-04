import numpy as np
from time import sleep
from stepper import Stepper, RotateStepper  # This is LoisLab's stepper library
from steppers import Steppers
import RPi.GPIO as GPIO

class Rover():

    def __init__(self):
        self.tuning_coeff = 1.555  #adjustment to tune motors being a little off
        GPIO.setmode(GPIO.BOARD)
        self.right_wheel = RotateStepper((7,11,13,15),orientation=Stepper.CCW)
        self.left_wheel = RotateStepper((31,33,35,37),orientation=Stepper.CW)
        self.wheels = Steppers((self.right_wheel, self.left_wheel))

    def move(self, action):
        rotation_degrees = 90 * self.tuning_coeff  # turns are 90 degrees, arbitrarily
        travel_duration = 180                       # forward moves are a 90 degree rotation of both wheels
        if action == 0:
            #go forward
            self.right_wheel.set_target(travel_duration)
            self.left_wheel.set_target(travel_duration)
        elif action == 1:
            #turn left
            self.right_wheel.set_target(rotation_degrees)
            self.left_wheel.set_target(-rotation_degrees)
        elif action == 2:
            #turn right
            self.right_wheel.set_target(-rotation_degrees)
            self.left_wheel.set_target(rotation_degrees)
        self.wheels.move()




#################################################################
# Script to do a basic trip                                     #
#################################################################

rover = Rover()     # Create a new instance of rover 
for x in range(4):  # Loop 4 times
    rover.move(0)   # move forward
    rover.move(1)   # turn


