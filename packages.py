# This file contains the class for the packages

class Packages:
    def __init__(self, packageID, packageaddress, packagecity, packagestate, packagezip, packageweight, packagedeadline, packagestatus):
        self.packageID = packageID
        self.packageaddress = packageaddress
        self.packagecity = packagecity
        self.packagestate = packagestate
        self.packagezip = packagezip
        self.packageweight = packageweight
        self.packagedeadline = packagedeadline
        self.packagestatus = packagestatus
        self.packagedeparturelocation = None
        self.packagedeliveredlocation = None

    def __str__(self):
        return F'ID: {self.packageID}\n' \
               F'Address: {self.packageaddress}\n' \
               F'Delivery Deadline: {self.packagedeadline}\n' \
               F'State: {self.packagestate}\n' \
               F'City: {self.packagecity}\n' \
               F'Zip: {self.packagezip}\n' \
               F'Weight (Kilos): {self.packageweight}\n' \
               F'Status: {self.packagestatus}\n' \
               F'Departure Location: {self.packagedeparturelocation}\n' \

    # Method to update the package status
    def updatestatus(self, timedelta):
        if self.packagedeliveredlocation > timedelta:
            statusupdate = 'HUB'
        elif self.packagedeparturelocation < timedelta:
            statusupdate = 'Delivered'
        else:
            statusupdate = 'Out for delivery'
        return F'ID: {self.packageID}\n' \
               F'Address: {self.packageaddress}\n' \
               F'Delivery Deadline: {self.packagedeadline}\n' \
               F'State: {self.packagestate}\n' \
               F'City: {self.packagecity}\n' \
               F'Zip: {self.packagezip}\n' \
               F'Weight (Kilos): {self.packageweight}\n' \
               F'Delivery Time: {self.packagedeparturelocation}\n' \
               F'Status: {statusupdate}\n'