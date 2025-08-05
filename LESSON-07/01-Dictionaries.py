# Dictinaries (Like objects in JavaScript)

from turtle import clear


band = {
    "vocals": "Plant",
    "guitar": "Page",
    "rock": "Hard"
}
print(band)

# Using constructor :
band2 = dict(vocals="Plant", guitar="Page")
print(band2)

# Type of Dict :
print(type(band))
print(len(band))

print("______________________________________________________")

# Access items :
print(band["vocals"])
print(band.get("guitar"))

print("______________________________________________________")

# List all keys and values :
print("Keys : ", band.keys())
print("Values : ", band.values())

# List of key/value pairs as tuples
print(band.items())

print("______________________________________________________")

# Verify a key's existance :
print("guitar" in band)
print("guitarrrr" in band)

print("______________________________________________________")

# Change values :
band["vocals"] = "Coverdale"
print(band)

band.update({"bass": "JPJ"})  # Can also be used to add new key:value pairs
print(band)

print("______________________________________________________")

# Remove items :
print("Removed Item : ", band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  # Returns tuple
print(band)

print("______________________________________________________")

# Delete Items :
del band["rock"]
print(band)

band2.clear()
print(band2)
