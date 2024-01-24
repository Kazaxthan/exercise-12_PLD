#Exercise 12: Calculate income tax for the given income by adhering to the rules below

income = 11000
tax = 0

if income <= 10000:
    tax = 0
elif income <= 20000:
    i = income - 10000
    tax = i * 0.10

else:
    
    tax = 0
    
    tax = 10000 * 0.10
    
    tax += (income - 20000) * 0.20
    
print ("total of amount of tax to be paidd is:", tax)
    