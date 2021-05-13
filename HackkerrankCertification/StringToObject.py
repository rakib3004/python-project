#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self,max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit



class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for i in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
            vehicle_type="Car"
            print("{} with the maximum speed of {} {}".format(vehicle_type,vehicle.max_speed,vehicle.speed_unit))
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
            vehicle_type = "Boat"
            print("{} with the maximum speed of {} knots".format(vehicle_type,vehicle.max_speed))
        else:
            raise ValueError("invalid vehicle type")
        #fptr.write("%s\n" % vehicle)

