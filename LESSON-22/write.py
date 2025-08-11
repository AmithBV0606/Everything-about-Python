# Write (overwrite) : Also creates the file if it doesn't exist

f = open("context.txt", "w")
f.write("I deleted all of the context!!")
f.close()

f = open("context.txt")
print(f.read())
f.close()
