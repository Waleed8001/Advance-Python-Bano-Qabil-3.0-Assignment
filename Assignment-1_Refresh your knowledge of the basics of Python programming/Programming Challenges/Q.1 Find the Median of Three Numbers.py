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