# Loops

# Types of Loops : 1) While loop 2) for loop

# 1) while loop : Executes the block of code untill/while the condition is true

value = 0
# while value < 10:
#     print(value)
#     value += 1

# while value <= 10:
#     print(value)
#     value += 1

# _____________________________________________________________________________________

# break keyword :
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# continue keyword :
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
