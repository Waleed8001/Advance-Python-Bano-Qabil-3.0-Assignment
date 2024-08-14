def simple_interest1(a,b,c):
    simple_interest = a/(b*c)
    return simple_interest

# Input:
principal_amount = float(input("Enter the principal amount: "))   # Enter the principal amount: 1000
rate_of_interest = float(input("Enter the rate of interest: "))   # Enter the rate of interest: 5
time_period = float(input("Enter the time period in years: "))   # Enter the time period in years: 2

simple_interest = simple_interest1(principal_amount,rate_of_interest,time_period)
print("Simple Interest: ",simple_interest)   # Simple Interest: 