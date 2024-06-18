monthly_income = int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expenses: "))
monthly_savings = float(monthly_income) - float(monthly_expense)
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are "+ str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: " + str(annual_savings) + ".")

