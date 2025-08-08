def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
print(addTen(7))

addTwenty = funcBuilder(20)
print(addTwenty(7))
