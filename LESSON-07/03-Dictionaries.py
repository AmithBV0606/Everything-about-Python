# Nested Dictionaries :

member1 = {
    "name": "Plant",
    "instrument": "Vocals"
}
member2 = {
    "name": "Page",
    "instrument": "Guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)

# Accessing these values :
print(band["member1"]["name"])
print(band["member2"]["name"])
