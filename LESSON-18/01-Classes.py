# Classes in python is a blueprints for creating objects

# class Vehicle:
#     def moves(self):
#         print("Moves along...")

# my_car = Vehicle()
# my_car.moves()

# "my_car" is an object created from the "Vehicle" class.

# NOTE : The first letter of Class name should be capital

# ________________________________________________________________________

# Classes can have properties
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def moves(self):
#         print("Moves along...")

# my_car = Vehicle("Tesla", "Model 3")
# print(my_car.make)
# print(my_car.model)

# _________________________________________________________________________

# The SET/GET method that access the properties of that class :

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}!!")


my_car = Vehicle("Tesla", "Model 3")
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()
