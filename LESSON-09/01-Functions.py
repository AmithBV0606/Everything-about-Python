# FUNCTIONS

# Functions are reusable block of code.

def hello_world():
    print('Hello world!')


hello_world()

# NOTE : No capital letter or special character in a function name.

print("_____________________________________________________________")

# Parameter and Arguements :


def sum(num1, num2):  # Parameters(Placeholders) : Never changes
    print(num1 + num2)


sum(5, 10)  # Arguements : Changes with each function call
sum(50, 150)
sum(500, 1500)

print("_____________________________________________________________")

# Function that returns :


def mul(num1, num2):
    product = num1 * num2
    return product


multiply = mul(2, 8)
print(multiply)

print("_____________________________________________________________")

# Input Validation


# def div(num1, num2):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     divide = num1 / num2
#     return divide


# division = div("2", 8)
# print(division)

# Default values :

def div(num1=10, num2=2):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    divide = num1 / num2
    return divide


# division = div()
division = div("20")
print(division)
