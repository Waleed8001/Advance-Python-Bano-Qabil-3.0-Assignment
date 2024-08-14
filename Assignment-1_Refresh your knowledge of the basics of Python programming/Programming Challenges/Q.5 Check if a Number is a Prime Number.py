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