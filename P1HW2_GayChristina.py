#Python program for calculating travel expense
#02/16/2023
#CTI-110 P1HW2 - Travel Expense
#Christina Gay
#
print("This program calculates and displays travel expense")
Budget = int(input("Enter Budget:"))
Destination = input("Enter your destination:")
Fuel = int(input("How much do you think you will spend on gas?"))
Accommodation = int(input("Approximately, how much will you need for accommodation/hotel?"))
Food = int(input("Last, how much do you need for food?"))
print()
print("------------Travel Expenses------------")
print("Location:", Destination)
print("Initial Budget:", Budget)
print()
print("Fuel:", Fuel)
print("Accommodation:", Accommodation)
print("Food:", Food)
print()
print("Remaining Balance:", Budget - Fuel - Accommodation - Food)
