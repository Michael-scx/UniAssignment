
name = input("Enter your name: ")
income = int(input("Enter your monthly net income: "))

c, d, e, f = map(int, input("Enter fixed expenses (Rent, Utilities, Internet, Phone Bill): ").split())
g, h, q = map(int, input("Enter variable expenses (Groceries, Transportation, Entertainment): ").split())

current_savings = int(input("Enter your current savings: "))
goal = int(input("Enter your apartment down payment goal: "))
months = int(input("Enter months until desired purchase: "))

total_fixed = c + d + e + f
total_variable = g + h + q
total_expenses = total_fixed + total_variable
monthly_savings = income - total_expenses
savings_rate = (monthly_savings / income) * 100
if income > 0:
     savings_rate = (monthly_savings / income) * 100
else :
     savings_rate = 0
projected_savings = monthly_savings * months
total_projected = current_savings + projected_savings
monthly_needed = goal / months
additional_needed = monthly_needed - monthly_savings
shortfall_or_surplus = total_projected - goal


critical_warning = total_expenses >= income
below_recommended = savings_rate < 20
good_position = 20 <= savings_rate < 30
excellent_position = savings_rate >= 30
goal_achievable = total_projected >= goal

print(f"\n--- Personal Finance Report for {name} ---")
print(f"Monthly Income: {income}")
print(f"Fixed Expenses: {total_fixed}")
print(f"Variable Expenses: {total_variable}")
print(f"Total Expenses: {total_expenses}")
print(f"Monthly Savings: {monthly_savings}")
print(f"Savings Rate: {savings_rate:.2f}%")
print(f"Current Savings: {current_savings}")
print(f"Projected Savings in {months} months: {projected_savings}")
print(f"Total Projected: {total_projected}")
print(f"Down Payment Goal: {goal}")
print(f"Monthly Savings Needed: {monthly_needed:.2f}")
print(f"Additional Monthly Savings Needed: {additional_needed:.2f}")
print(f"Shortfall/Surplus: {shortfall_or_surplus}")

print("\n--- Status Indicators ---")
print(f"Critical Warning (Expenses >= Income): {critical_warning}")
print(f"Below Recommended (<20%): {below_recommended}")
print(f"Good Position (20-29%): {good_position}")
print(f"Excellent Position (>=30%): {excellent_position}")
print(f"Goal Achievable: {goal_achievable}")
