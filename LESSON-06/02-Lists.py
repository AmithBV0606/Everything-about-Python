# Sorting the list (Modifies the existing list):

nums = [5, 3, 2, 6, 7, 4]
new_names = ['Hulk', 'Thor', 'Captain America', 'Iron man', 'black panther']

# Ascending order sort :
nums.sort()
print("Ascending : ", nums)

# Descending order sort :
nums.sort(reverse=True)
print("Descending : ", nums)

new_names.sort()
print(new_names)

# To adjust/include the non capital letter word in sorting :
new_names.sort(key=str.lower)
print(new_names)

print('______________________________________________________________')

# Array flip :
random_nums = [11, 14, 42, 56, 1, 8]
random_nums.reverse()
print(random_nums)

print('______________________________________________________________')

# Sorting without affecting original list :
print("Sorting without effecting the original list : ",
      sorted(random_nums, reverse=True))
print(random_nums)

print('______________________________________________________________')

# Copying the list

# Method 1 :
print("Original List :", random_nums)
new_random_nums_1 = random_nums.copy()
print("Copy of Original List :", new_random_nums_1)

new_random_nums_1.sort()
print(new_random_nums_1)
print(random_nums)

# Method 2 :
new_random_nums_2 = list(random_nums)

# Method 3 :
new_random_nums_3 = random_nums[:]

print('______________________________________________________________')

# Type of list :
print(type(nums))

# Creating list using constructor :
newList = list([1, "Neil", True])
print(newList)
