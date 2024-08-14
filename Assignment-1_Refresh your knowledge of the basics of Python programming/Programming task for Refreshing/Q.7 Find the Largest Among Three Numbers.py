# Input:
number = input("Enter three numbers separated by space: ").split()   # Enter three numbers separated by space: 10 25 5
try:
    n1 = int(number[0])
    n2 = int(number[1])
    n3 = int(number[2])
    if n1 > n2 and n1 > n3:
        print("The largest number is:",n1)
    elif n2 > n1 and n2 > n3:
        print("The largest number is:",n2)   # The largest number is: 25
    elif n3 > n1 and n3 > n2:
        print("The largest number is:",n3)
except Exception as e:
    print("Error:",e)        