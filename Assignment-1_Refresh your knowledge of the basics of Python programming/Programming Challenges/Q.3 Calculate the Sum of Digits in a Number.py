sum = 0
number = int(input("Enter a number: "))   # Enter a number: 12345
while number >= 1:    
    divide = int(number % 10)
    number = int(number / 10)
    sum = sum + divide
    
print(sum)