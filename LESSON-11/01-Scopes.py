# Scopes in Python

# Global Scope :
name = "Amith"
# print(name)

# Global Scope inside a function :
# def greetings():
#     print("Hello, " + name)

# greetings()

# A function has local scope as well :
# def greetings():
#     color = "blue"
#     print(color)
#     print("Hello, " + name)

# greetings()
# print(color) # Color variable is in the local scope of the function.

# ______________________________________________________________________
# def greetings(firstname):
#     color = "blue"
#     print(color)
#     print("Hello, " + firstname)

# greetings("Arun")

print("______________________________________________________________________")

# Calling another function inside a local scope of a function :
# def another():
#     greetings("Jhon")

# another()

print("______________________________________________________________________")

# Function inside another function :
def another():
    color = "blue"

    def greetings(firstname):
        print(color)
        print("Hello, " + firstname)

    greetings("Jack")

another()
