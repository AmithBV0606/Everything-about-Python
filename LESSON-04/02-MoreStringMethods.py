# Build a menu :
title = 'menu'.upper()
print(title.center(20, "="))
print('Coffee'.ljust(16, ".") + "$1".rjust(4))
print('Muffin'.ljust(16, ".") + "$2".rjust(4))
print('Cheese Cake'.ljust(16, ".") + "$4".rjust(4))

print('___________')

# String Index value : 
fname = "Amith"
lname = "Rao"
print(fname[1])
print(fname[-1]) # Last letter
print(fname[0:-2]) # Ami
print(fname[0:-1]) # Amit
print(fname[1:])

print('___________')

# String methods which returns boolean data : 
print(fname.startswith("A"));
print(fname.endswith("H"));