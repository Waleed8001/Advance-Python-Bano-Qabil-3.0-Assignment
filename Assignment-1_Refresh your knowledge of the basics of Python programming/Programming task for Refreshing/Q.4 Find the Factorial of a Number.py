def factorial(n,number):
    for i in range(n,number+1):
        n = i * n
    return n    

# Input
n = 1
number = int(input("Enter a number: "))   # Enter a number: 5
print("Factorial of",number,"is:",factorial(n,number))
