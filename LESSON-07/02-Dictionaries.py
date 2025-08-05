# Copying a Dictionary :

myself = {
    "name": "Amith B V",
    "age": 25,
    "Gender": "Male",
    "Role": "Software Engineer"
}

# Way not to copy dictionaries : Shallow Copy
me = myself
print("Bad copy!!")

# NOTE : This creates a reference in the memory(Means changes made to "myself" will be reflected in "me" as well)

# Example :
print("Myself : ", myself)
print("Me : ", me)

me["name"] = "Amit Rao"
print("Myself : ", myself)
print("Me : ", me)

print("_________________________________________________________")

# Actual way to copy dictionaries : Deep Copy
me = myself.copy()

# Example :
print("Myself : ", myself)
print("Me : ", me)

me["name"] = "Amit Menon"
print("Myself : ", myself)
print("Me : ", me)

print("_________________________________________________________")

# Copy using constructor function :
me2 = dict(myself)
print("Me2 : ", me2)
