# Q.1/ Question: Create a lambda function that multiplies two numbers and returns the result. Use this lambda function to multiply 5 by 7.

mul = lambda a,b: a*b
print(mul(5,7))

# Q.2/ Question: You have a list of numbers [1, 2, 3, 4, 5]. Use the map function and a lambda function to create a new list where each number is increased by 10.

list1 = [1,2,3,4,5]
list2 = list(map(lambda x: x + 10,list1))
print(list2)

# Q.3/ Question: Given a list of numbers [3, 6, 9, 12, 15, 18, 21], use the filter function to select numbers greater than 10. Then, use the reduce function to calculate the sum of the filtered numbers.

import functools  # For using reduce function we import functools
list3 = [3, 6, 9, 12, 15, 18, 21]
list4 = list(filter(lambda x:x>10,list3))
list5 = functools.reduce(lambda x,y:x+y,list4)
print(list5)