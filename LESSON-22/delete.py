# Delete a file

import os

# Avoid an error if the file doesn't exists!
if os.path.exists("delete-sample.txt"):
    os.remove("delete-sample.txt")
else:
    print("The file you wish to delete, doesn't exist!!")

# New Syntax :
# with open("more_names.txt") as f:
#     content = f.read()

# with open("names.txt", "w") as f:
#     f.write(content)
