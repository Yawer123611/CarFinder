AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]


def cars():
    print(" ")     
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")

    print("********************************")
    print("Please Enter the following number below from the following menu:")

    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")


cars()
finder = int(input("Please Enter a Number: "))

while finder !=3:
    if finder == 1:
        print(" ")
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in AllowedVehiclesList:
            print(vehicle)
    cars()
    finder = int(input("Please Enter a Number: "))
   
     elif finder == 2:
       name = input("Please Enter the full Vehicle name:")
     for in AllowedVehiclesList:
        if name is == vehiclet:
        print( name, "is an authorized vehicle")
    else:
        print( name,"is not an authorized vehicle, if you received this in error please check the spelling and try again")


print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")