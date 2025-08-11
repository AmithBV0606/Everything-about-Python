# Append - Creates the file if it doesn't exists

f = open("names.txt", "a")  # a - append, by default it's read
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()