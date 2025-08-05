# Sets in Python :

nums = {1, 2, 3, 4}

# Using constructor functions :
nums2 = set((1, 2, 3, 4, 5, 6, 7))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed :
nums3 = {1, 2, 2, 3}
print(nums3)

# True is a dupe of 1, False is a dupe of zero
nums4 = {1, True, 2, False, 3, 4, 0}
print(nums4)

# Check if a value is in a set
print(2 in nums)

# NOTE : but you cannot refer to an element in the set with an index position or a key

print("___________________________________________________________")

# Add a new element to a set :
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# NOTE : You can use "update" method in set with list, tuples and dictionaries too.

print("___________________________________________________________")

# Merge two sets to create a new set :
nums5 = {1, 2, 3, 4, 5}
nums10 = {5, 6, 7, 8, 9}

new_set = nums5.union(nums10)
print(new_set)

# To keep only the duplicates :
nums5.intersection_update(nums10)
print(nums5)

# To keep everything but duplicates :
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
