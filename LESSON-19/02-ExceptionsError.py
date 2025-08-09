x = 2

try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed!!")
except NameError:
    print(f"NameError means something is probably undefined!!")
except ZeroDivisionError:
    print("You're probably trying to divide a number by zero")
except Exception as error:
    print(error)
else:
    print("No errors!!")
finally:
    print("I'm going to print with or without an error!!!")

print("________________________________________________________________")

# Custom Exception Type 1 :
try:
    raise Exception("I'm a custom exception!!")
except Exception as error:
    print(error)
finally:
    print("I'm going to print with or without an error!!!")

print("________________________________________________________________")

# Custom Exception Type 2(Named exception) :


class JustNotCoolError(Exception):
    pass


try:
    raise JustNotCoolError("This is not cool, man!!")
except Exception as error:
    print(error)
finally:
    print("I'm going to print with or without an error!!!")
