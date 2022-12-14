# Program to display age in months, weeks and days 

age = int(input("Enter your age : "))
rem_years = 90 - age
rem_months = rem_years * 12
rem_weeks = rem_years * 52
rem_days = rem_years * 365
Answer = f"You have {rem_days} days, {rem_weeks} weeks and {rem_months} months remaining"
print(Answer)
