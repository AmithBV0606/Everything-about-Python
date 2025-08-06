# Accepting indefinite(unknown) number of arguements :

def multiple_items(*args):
    print(args[0])
    print(args[1])
    print(args[2])
    print(type(args))


multiple_items(1, 2, "Amith")

print("_________________________________________")


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Amith", last="Gray")
mult_named_items(id=1, username="amith_rao")
