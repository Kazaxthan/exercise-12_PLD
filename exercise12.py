#Exercise 12: Calculate income tax for the given income by adhering to the rules below






def calculate_income_tax(income):
    if income <= 10000:
        # first income tax is 0%
        tax = 0
    elif income <= 20000:
        # for the second income there will be a tax of 10%
        tax = (income - 10000) * 0.10
    else:
        # in the third income the tax will icrease by 10%
        tax = 10000 * 0 + 10000 * 0.10 + (income - 20000) * 0.20
    return tax

# user input the income
user_input = input("Enter the your Income: ")

try:
    # switch the user input to an integer
    taxable_income = int(user_input)
    # Validation!
except ValueError:
    print("Invalid input. Please enter a valid taxable income.")
    exit()

# result
income_tax = calculate_income_tax(taxable_income)
print(f"Income tax payable: ${income_tax:.2f}")