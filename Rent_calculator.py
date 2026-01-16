##. Inputs we need from he user
# Total rent
#Total food ordered for snacking
# Electricity units speed
# Charge per unit

## output
# Total amount you've to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
Electricity_spend = int(input("Enter the total of electricity spend = "))
Charge_per_unit = int(input("Enter the charge per unit = "))
Persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = Electricity_spend * Charge_per_unit

output = (food + rent + total_bill) // Persons

print("Each person will pay = ", output)