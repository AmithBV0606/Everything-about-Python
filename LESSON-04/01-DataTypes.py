# Data Types

# 1) String

# Literal assignment
first = 'Amith'
last = 'Rao'

# Type Checking :
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor function :
pizza = str("Chicken Pizza!!")

print('___________')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatination :
fullName = first + ' ' + last

print('___________')
print(fullName)

fullName += "!"
print(fullName)

# Type Casting : 
number = 2
toString = str(number)

print('___________')
print('Before Casting : ', type(number), number)
print('After Casting : ', type(toString), toString)

# Multiple lines : 
multiline = '''
Hii, 
How are you?
'''

print('___________')
print(multiline)

# Escaping special character :
sentence = 'I\'m back at work!\tHey!\nHello'
print('___________')
print(sentence)

# String Methods :
print('___________')
print(first)
print(first.lower())
print(first.upper())
print(first)

print('___________')
print(multiline.title())
print(multiline.replace("you", "THey"))
print(multiline)

# Length :
print('___________')
print(len(multiline))
multiline += "                     "
multiline = "                " + multiline;
print(len(multiline))

# Remove whitespace : 
print('___________')
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))