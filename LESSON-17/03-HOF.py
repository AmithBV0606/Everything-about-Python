# Higher Order Functions

from functools import reduce

# Maps :
numbers = [3, 5, 7, 9, 10, 12,4]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

# Filter :
odd_numbers = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_numbers))

# Reducer :
add_nums1 = reduce(lambda acc, curr: acc + curr, numbers)
print("Reduce Method :", add_nums1)

# Reducer with initial value 
add_nums2 = reduce(lambda acc, curr: acc + curr, numbers, 30)
print("Reduce Method starting with 30 :", add_nums2)

# Alternative method to add the elements of a list 
print("In-built Sum method : ", sum(numbers))