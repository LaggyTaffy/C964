# This file contains the class for the trucks

class Trucks:
    def __init__(self, trucknumber, truckcapacity, truckspeed, truckmileage, trucklocation, truckpackages, truckdeparturetime):
        self.trucknumber = trucknumber
        self.truckcapacity = truckcapacity
        self.truckspeed = truckspeed
        self.truckmileage = truckmileage
        self.trucklocation = trucklocation
        self.truckpackages = truckpackages
        self.truckdeparturetime = truckdeparturetime
        self.trucktime = truckdeparturetime

    def __str__(self):
        return self.trucknumber, self.truckcapacity, self.truckspeed, self.truckmileage, self.trucklocation, self.truckpackages, self.truckdeparturetime