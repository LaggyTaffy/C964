# Student ID: 001065048
# Richard La Frentz

# main.py houses bulk of the process. First, we import the CSV files, hash table, and truck classes.
# Then, we create the hash table and insert the packages.
# Next, we create the three trucks and assign the packages to them.
# We then define functions to find the distance between two addresses and to find the address ID from the address.
# We also define a function to load the truck with packages using the nearest neighbor algorithm.
# We then load the trucks with packages. We then define a function to print the package manifest for each truck.
# We then define the main function that prints the mileage for the route and prompts the user for a time to see the package status.
# We then update package 9 if the time is after truck 3's departure time.
# We then prompt the user for a choice to lookup a package and its truck, list all packages and information, or exit the program.
# If the user chooses to lookup a package and its truck, the user is prompted to enter a package ID and the package status is printed.
# If the user chooses to list all packages and information, the package manifest is printed and the package status is printed for each package.
# If the user chooses to exit the program, the program exits.
# If the user enters an invalid choice, the user is prompted to enter a valid choice.

import datetime

# Import the CSV files, hash table, and truck classes
from csvreader import packagesinsert, addressescsv, distancescsv
from hashtable import ChainingHashTable
from trucks import Trucks

# Creates the hash table and inserts the packages
myHashTable = ChainingHashTable()
packagesinsert(myHashTable)

# Create the three trucks and assign the packages to them
truck1 = Trucks(1, 16, 18, 0.0, '4001 South 700 East', [1, 4, 7, 8, 13, 14, 15, 16, 20, 21, 29, 30, 34, 37, 39, 40], datetime.timedelta(hours=8))
truck2 = Trucks(2, 16, 18, 0.0, '4001 South 700 East', [3, 5, 6, 18, 19, 25, 26, 28, 31, 32, 36, 38], datetime.timedelta(hours=9, minutes=5))
truck3 = Trucks(3, 16, 18, 0.0, '4001 South 700 East', [2, 9, 10, 11, 12, 17, 22, 23, 24, 27, 33, 35], datetime.timedelta(hours=10, minutes=20))
truck3starttime = truck3.truckdeparturetime

# Function to find the distance between two addresses
def finddistance(a, b):
    distance = distancescsv[a][b]
    if a < b:
        distance = distancescsv[b][a]
    return float(distance)

# Function to find the address ID from the address
def findaddress(address):
    for row in addressescsv:
        if address in row[2]:
            return int(row[0])

# Citation: C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor, https://srm--c.vf.force.com/apex/coursearticle?Id=kA03x000001DbBGCA0
# Function to load the truck with packages using the nearest neighbor algorithm.
# Time complexity = O(n^2)
def loadtruck(truck):
    undelivered = []
    for packagesID in truck.truckpackages:
        package = myHashTable.lookup(packagesID)
        undelivered.append(package)
    truck.truckpackages.clear()
    while len(undelivered) > 0:
        closestaddress = 2000
        closestpackage = None
        for package in undelivered:
            if closestaddress >= finddistance(findaddress(truck.trucklocation), findaddress(package.packageaddress)):
                closestaddress = finddistance(findaddress(truck.trucklocation), findaddress(package.packageaddress))
                closestpackage = package
        # Adds the closest package to the truck
        truck.truckpackages.append(closestpackage.packageID)
        # Removes the package from the undelivered list
        undelivered.remove(closestpackage)
        # Adds the distance to the truck mileage
        truck.truckmileage += closestaddress
        # Updates the truck location and time
        truck.trucklocation = closestpackage.packageaddress
        truck.truckdeparturetime += datetime.timedelta(hours=(closestaddress / truck.truckspeed))
        closestpackage.packagedeliveredlocation = truck.trucktime
        closestpackage.packagedeparturelocation = truck.truckdeparturetime

# Loads trucks with packages
loadtruck(truck1)
loadtruck(truck2)
loadtruck(truck3)

# Function that prints the package manifest for each truck
def truckmanifest():
    for truck in [truck1, truck2, truck3]:
        # Sort the package IDs in ascending order
        sortedpackageIDs = sorted(truck.truckpackages)
        # Convert Package IDs to strings
        packageIDs = [str(packageID) for packageID in sortedpackageIDs]
        print(f'Packages on truck {truck.trucknumber}: {", ".join(packageIDs)}')

def main():
    print('------------------------------')
    print('--- WGUPS Routing Program ----')
    print('------ Date:', datetime.datetime.now().strftime('%m/%d/%Y'), '------')
    print('----- Richard La Frentz ------')
    print('--- Student ID: 001065048 ----')
    print('------------------------------')
    print('')
    print("The mileage for the route is:")
    print(truck1.truckmileage + truck2.truckmileage + truck3.truckmileage)
    print('')
    time = input('Enter a time to see the package status. (HH:MM format, 24HR format only): ')
    print('')
    (h, m) = time.split(':')
    timedelta = datetime.timedelta(hours=int(h), minutes=int(m))

    if timedelta >= truck3starttime:
        package = myHashTable.lookup(9)
        package.packageaddress = '410 S State St'
        package.packagedeadline = 'EOD'
        package.packagestate = 'UT'
        package.packagecity = 'Salt Lake City'
        package.packagezip = '84111'
        package.packageweight = '2'
        myHashTable.insert(9, package)

    while True:
        print('What would you like to do?')
        print('1 - Lookup a package and its truck')
        print('2 - List all packages and information')
        print('3 - Exit the program')
        choice = input('Enter your choice: ')
        print('')

        if choice == '1':
            packageIDsingle = input("Please enter the package ID: ")
            singlefound = False
            for truck in [truck1, truck2, truck3]:
                if int(packageIDsingle) in truck.truckpackages:
                    print(f'On truck {truck.trucknumber}')
                    package = myHashTable.lookup(int(packageIDsingle))
                    package.updatestatus(timedelta)
                    print(package.updatestatus(timedelta))
                    singlefound = True
                    break
            if not singlefound:
                print(f'Not found on any truck.')

        elif choice == '2':
            truckmanifest()
            print('')
            for packageIDall in range(1, 41):
                allfound = False

                for truck in [truck1, truck2, truck3]:
                    if int(packageIDall) in truck.truckpackages:
                        print(f'On truck {truck.trucknumber}')
                        package = myHashTable.lookup(int(packageIDall))
                        package.updatestatus(timedelta)
                        print(package.updatestatus(timedelta))
                        allfound = True
                        break
                if not allfound:
                    print(f'Not found on any truck.')

        elif choice == '3':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice.')

main()