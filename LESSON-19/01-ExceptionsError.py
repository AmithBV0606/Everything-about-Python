# Exception handling :

# Different types of Built-in Exceptions : https://www.w3schools.com/python/python_ref_exceptions.asp

# Example 1 :
# try:
#     print(x)
# except NameError:
#     print(f"NameError means something is probably undefined!!")

# Example 2 :
x = 2

try:
    print(x / 0)
    # print(x / 1)
except NameError:
    print(f"NameError means something is probably undefined!!")
except ZeroDivisionError:
    print("You're probably trying to divide a number by zero")
else:
    print("No errors!!")
finally:
    print("I'm going to print with or without an error!!!")
