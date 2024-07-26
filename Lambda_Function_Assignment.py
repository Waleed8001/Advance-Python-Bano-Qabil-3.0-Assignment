# Question 1: You have a list of strings ['apple', 'banana', 'cherry', 'date', 'elderberry']. Use the filter function and a lambda function to create a new list that contains only the strings with more than 5 characters.
# Input: ['apple', 'banana', 'cherry', 'date', 'elderberry']
# Expected Output: ['banana', 'cherry', 'elderberry']

list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry']
list2 = list(filter(lambda x:len(x)>5,list1))
print(list2)

# Question 2: Given a list of numbers [2, 4, 6, 8, 10], first use the map function and a lambda function to double each number. Then, use the reduce function to find the product of the doubled numbers.
# Input: [2, 4, 6, 8, 10]
# Expected Output: 122880 (Product of [4, 8, 12, 16, 20])

import functools  # For using reduce function we import functools
list3 = [2, 4, 6, 8, 10]
list4 = list(map(lambda x:x*2,list3))
list5 = functools.reduce(lambda x,y:x*y,list4)
print(list5,"(Product of [4,8,12,16,20])")