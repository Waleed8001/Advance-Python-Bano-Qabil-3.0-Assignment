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
0
1
1
2
3
5
8