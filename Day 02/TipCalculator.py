# Program to calculate and split the bills 

print("Tip Calculator")
bill = float(input("Enter total bill : "))
tip = int(input("How much would you like to tip ? "))
people = int(input("How many people to split the bill ? "))
bill_with_tip = float(tip/100 * bill + bill)
print("Everyone should pay : ")
print(round(bill_with_tip, 2))

