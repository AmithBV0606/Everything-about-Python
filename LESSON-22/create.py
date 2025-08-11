# Create

import os

# There are two ways to create a new file :

# 1. Opens a file for writing, creates the file if it does not exists
# f = open("Names_Lists.txt", "w")
# f.write("Hello, This is the new file!!\n")
# f.close()

# f = open("Names_Lists.txt")
# print(f.read())
# f.close()

# 2. Creates the specified file, but returns an error if the file exists
if not os.path.exists("Amith.txt"):
    f = open("Amith.txt", "x")
    f.write("Hello, My name is Amith andddd I'mmmma BATMAN!!\n")
    f.close()

    f = open("Amith.txt")
    print(f.read())
    f.close()
