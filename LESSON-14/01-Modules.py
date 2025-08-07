# import math
from math import pi
import sys
# import random
import random as rdm
from enum import Enum
import India
import Exercise

# print(math.pi)
print(pi)

# print(random.choice("123"))
print(rdm.choice("123"))

# _______________________________________________________

# To find what's inside a module :
# print(dir(rdm)) 

# for item in dir(rdm):
#     print(item)

print("_______________________________________________________")

print(India.capital)

India.randomfunfact()

print("_______________________________________________________")

# To know module name 
print(__name__)
print(India.__name__)

print("_______________________________________________________")

# Rock Paper Scissors :
Exercise.rock_paper_scissors()