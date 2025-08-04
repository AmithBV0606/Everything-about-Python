# Numeric data type :

# Integer :
import math
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

print('________________________')

# Float :
gpa = 4.2
y = float(1.14)

print(type(gpa))

print('________________________')

# Complex :
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print('________________________')

# Built-in functions for numbers :
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

print('________________________')

# Imported methods :
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

print('________________________')

# Casting a string to a number :
zipcode = "560060"
zip_value = int(zipcode)
print(type(zip_value))

# Error
new_error = int("New York")
# print(new_error)
