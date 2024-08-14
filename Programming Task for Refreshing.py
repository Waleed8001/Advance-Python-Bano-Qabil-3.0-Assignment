# Q.1/ Calculate the Area of a Rectangle.
# Input:
length = int(input("Enter the length of the rectangle: "))   # Enter the length of the rectangle: 3
width = int(input("Enter the width of the rectangle: "))   # Enter the width of the rectangle: 5
# Output:
print("The area of the rectangle is: ",length*width)   # The area of the rectangle is: 15


# Q.2/ Check if a Number is Even or Odd.
# Input:
number = int(input("Enter a number: "))  # Enter a number: 7  or  # Enter a number: 6
if number % 2 == 0:
    # Output:
    print(number,"is even.")   # 6 is even.
else:
    # Output:
    print(number,"is odd.")   # 7 is odd.


# Q.3/ Reverse a String.
# Input:
string = input("Enter a string: ")   # Enter a string: Hello
# Output:
print("Reversed string:",string[::-1])   # Reversed string: olleH


# Q.4/ Find the Factorial of a Number
def factorial(n,number):
    for i in range(n,number+1):
        n = i * n
    return n    

# Input:
n = 1
number = int(input("Enter a number: "))   # Enter a number: 5
# Output:
print("Factorial of",number,"is:",factorial(n,number))


# Q.5/ Check if a String is Palindrome or Not
def isPalindrome(str,str2):
    if str == str2:
        # Output:
        print(str,"is a palindrome.")   # radar is a palindrome.
    else:
        # Output:
        print(str,"is not a palindrome.")   # Hand is not a palindrome.

# Input:
str = input("Enter a string: ")   # Enter a string: radar  or  Enter a string: Hand
str2 = str[::-1]
isPalindrome(str,str2)


# Q.6/ Generate Fibonacci Series up to n terms
n1 = 0
n2 = 1
# Input:
number = int(input("Enter the number of terms: "))  # Enter the number of terms: 7
print("Fibonacci Series up to",number,"terms: ")
for i in range(number):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

# Output
# Fibonacci Series up to 7 terms: 
# 0
# 1
# 1
# 2
# 3
# 5
# 8


# Q.7/ Find the Largest Among Three Numbers
# Input:
number = input("Enter three numbers separated by space: ").split()   # Enter three numbers separated by space: 10 25 5
try:
    n1 = int(number[0])
    n2 = int(number[1])
    n3 = int(number[2])
    if n1 > n2 and n1 > n3:
        # Output:
        print("The largest number is:",n1)
    elif n2 > n1 and n2 > n3:
        # Output:
        print("The largest number is:",n2)   # The largest number is: 25
    elif n3 > n1 and n3 > n2:
        # Output:
        print("The largest number is:",n3)
except Exception as e:
    print("Error:",e)        


# Q.8/ Calculate Simple Interest
def simple_interest1(a,b,c):
    simple_interest = a/(b*c)
    return simple_interest

# Input:
principal_amount = float(input("Enter the principal amount: "))   # Enter the principal amount: 1000
rate_of_interest = float(input("Enter the rate of interest: "))   # Enter the rate of interest: 5
time_period = float(input("Enter the time period in years: "))   # Enter the time period in years: 2

simple_interest = simple_interest1(principal_amount,rate_of_interest,time_period)
# Output:
print("Simple Interest: ",simple_interest)   # Simple Interest: 100


# Q.9/ Convert Celsius to Fahrenheit.
# Input:
celsius = float(input("Enter temperature in Celsius: "))   # Enter temperature in Celsius: 37
fahrenheit = (9 / 5) * celsius + 32
# Output:
print("Temperature in Fahrenheit:","%.1f" % fahrenheit)   # Temperature in Fahrenheit: 98.6


# Q.10/ Check Leap Year.
# Input:
year = int(input("Enter a year: "))   # Enter a year: 2020  or  Enter a year: 2022
if year % 4 == 0:
    # Output:
    print(year,"is a leap year.")   # 2020 is a leap year.
else:
    # Output:
    print(year,"is not a leap year.")   # 2022 is not a leap year