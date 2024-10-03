# This file contains the implementation of the csvreader function that reads all of the csv files and pushes it to the hash table.

import csv

from packages import Packages

# Time complexity = O(n)
# Reads the packages.csv file and stores it in a list
with open('CSVs/packages.csv', newline='') as csvfile:
    packagescsv = csv.reader(csvfile)
    packagescsv = list(packagescsv)

# Reads the distances.csv file and stores it in a list
with open('CSVs/distances.csv', newline='') as csvfile:
    distancescsv = csv.reader(csvfile)
    distancescsv = list(distancescsv)

# Reads the addresses.csv file and stores it in a list
with open('CSVs/addresses.csv', newline='') as csvfile:
    addressescsv = csv.reader(csvfile)
    addressescsv = list(addressescsv)

# Inserts the packages into the hash table when called
def packagesinsert(myHashTable):
    with open('CSVs/packages.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)  # Skip header row
        for packages in reader:
            packagesID = int(packages[0])
            packagesaddress = packages[1]
            packagescity = packages[2]
            packagesstate = packages[3]
            packageszip = packages[4]
            packagesweight = packages[5]
            packagesdeadline = packages[6]
            packagestatus = 'Loading package into truck'

            # Creates a package object
            package = Packages(packagesID, packagesaddress, packagescity, packagesstate, packageszip, packagesdeadline,
                               packagesweight, packagestatus)
            # Inserts the package into the hash table
            myHashTable.insert(packagesID, package)