count = 0

# Example 1 :
# def scopes_lesson():
#     count = 2
#     print(count)

# scopes_lesson()

# _____________________________________________

# Example 2 :
# def scopes_lesson():
#     count += 2
#     print(count)

# scopes_lesson() # Error

# Fixes :
# def scopes_lesson():
#     global count
#     count += 4
#     print(count)
    

# scopes_lesson() 

# _____________________________________________

# Example 3 : 
def scopes_lesson():
    global count
    count += 4
    print(count)
    
    color = "blue"

    def greetings(firstname):
        nonlocal color
        color = "Green"
        print(color)
        print("Hello, " + firstname)

    greetings("Jack")


scopes_lesson()