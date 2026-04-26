try:
    friends = int(input("Number of friends: "))
    if friends == 0:
        print("Number of friends cannot be 0")
        exit()
    rent = int(input("Total rent of Room/PG: "))
    food = int(input("Total amount spent on food: "))
    units = int(input("Number of units consumed: "))
    charge_per_unit = int(input("Charge per unit : "))
except ValueError:
    print("Enter a valid number")