class RentCalculator:
    def __init__(self, friends, rent, food, units, charge_per_unit):
        self.friends = friends
        self.rent = rent
        self.food = food
        self.units = units
        self.charge_per_unit = charge_per_unit

    def calculate_total(self):
        electricity_bill = self.units * self.charge_per_unit
        return self.rent + self.food + electricity_bill
        
    def split(self):
        if self.friends == 0:
            return "Error: Number of friends cannot be zero"
        return self.calculate_total() / self.friends


try:
    friends = int(input("Number of friends: ")) 
    if friends == 0:
        print("Number of friends cannot be zero")
        exit()
    rent = int(input("Rent of Room/PG: "))
    food = int(input("Total amount spent on food: "))
    units = int(input("No. of units consumed: "))
    charge_per_unit = int(input("Charge per unit: "))

    calculator = RentCalculator(friends, rent, food, units, charge_per_unit)
    total = calculator.calculate_total()
    split = calculator.split()

    print(f"Total amount to be paid is {total}\nHence, the split among each member is {split}")

except ValueError:
    print("Enter a valid number")