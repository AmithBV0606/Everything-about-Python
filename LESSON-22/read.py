# Read - Error if the file doesn't exists

# f = open("names.txt", "r") 
f = open("names.txt") # By default it'll be set to read("r")
# print(f.read())
# print(f.read(4))

# To read the first line of the file :
# print(f.readline())
# print(f.readline())

# Loop through each line :
for line in f:
    print(line)

f.close()

print("___________________________________________________________")

# Trying to open a file that doesn't exists :
try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("\nThe file you want to read doesn't exist!!")
finally:
    f.close()
