AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


def cars():
    print(" ")     
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")

    print("********************************")
    print("Please Enter the following number below from the following menu:")

    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")


cars()
finder = int(input("Please Enter a Number: "))

while finder !=2:
    if finder == 1:
        print(" ")
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in AllowedVehiclesList:
            print(vehicle)
    cars()
    finder = int(input("Please Enter a Number: "))

print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")