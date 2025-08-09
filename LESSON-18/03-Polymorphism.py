# Polymorphism

# Polymorphism in Python is a core concept of Object-Oriented Programming (OOP) that allows objects of different classes to be treated as instances of a common superclass or to respond to the same method call in a way specific to their own class. The term "polymorphism" originates from Greek words meaning "many forms." 

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}!!")


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
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

for v in (cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
    print("______________________")