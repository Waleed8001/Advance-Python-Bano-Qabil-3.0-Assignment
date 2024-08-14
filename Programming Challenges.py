# Q.1/ Find the Median of Three Numbers.
# Input:
number = input("Enter three numbers separated by space: ").split()  # Enter three numbers separated by space: 10 5 20  or  Enter three numbers separated by space: 10 5 10
number2 = []
length = len(number)
for i in range(length):
    number2.insert(i,int(number[i]))

number2 = sorted(number2)
if number2[0] < number2[1] and number2[2] > number2[1]:
    # Output:
    print("Median is:",number2[1])   # Median is: 10
else:
    print("No Median")   # No Median


# Q.2/ Count the Number of Words in a Sentence.
# Input:
string = input("Enter a sentence: ").split()   # Enter a sentence: The quick brown fox jumps over the lazy dog. 
# Output:
print("Number of words:",len(string))   # Number of words: 9


# Q.3/ Calculate the Sum of Digits in a Number.
# Input:
sum = 0
number = int(input("Enter a number: "))   # Enter a number: 12345
while number >= 1:    
    divide = int(number % 10)
    number = int(number / 10)
    sum = sum + divide
    
print("Sum of digits:",sum)   # Sum of digits: 15


# Q.5/ Check if a Number is a Prime Number
count = 0
# Input:
num = int(input("Enter a number: "))   # Enter a number: 29  or  Enter a number: 28
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    # Output:
    print(num,"is a prime Number.")   # 29 is a prime number.
else:
    # Output:
    print(num,"is not a prime Number.")   # 28 is not a prime number.