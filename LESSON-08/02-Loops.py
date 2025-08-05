# 2) for loops : For loop iterates over lists, tuples, dictionaries and sets

names = ["Amith", "Sara", "Jhon"]

# for x in names:
#     print("Hello, ", x)

# for x in "Mississippi":
#     print(x)

# _____________________________________________________________________________________

# Break keyword :
# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# Continue keyword :
# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# _____________________________________________________________________________________

# Ranges : Starts at index 0
# for x in range(4):
#     print(x)

# Starts at the specified numbers :
# for x in range(1, 4):
#     print(x)

# Increment in for loop
# for x in range(0, 50, 5):
#     print(x)
# else:
#     print('Glad that\'s over!!')

# _____________________________________________________________________________________

# Nested loops :
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action)
