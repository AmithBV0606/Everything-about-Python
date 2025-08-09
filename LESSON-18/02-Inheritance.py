# Ingeritance

# Super : In Python, super() is a built-in function that provides a way to access methods and properties of a parent or superclass from within a child or subclass. It is particularly useful in the context of inheritance in object-oriented programming.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}!!")


# If we use same method from the "Vehicle" class it'll override, what it has inherited from the "Vehicle" class.
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print(f"Flies along... {self.faa_id}")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Skyhawk", "N-123321")
cessna.get_make_model()
cessna.moves()

print("________________________________________________________")

mack = Truck("Mack", "Pinnacle")
mack.get_make_model()
mack.moves()

print("________________________________________________________")

golfwagon = GolfCart("Yamaha", "GC100")
golfwagon.get_make_model()
golfwagon.moves()
