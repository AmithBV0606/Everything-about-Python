# F-String

# Old Method : Before F-string was invented
person = "Amith"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

print("========================================================")

# Somewhat easier way :
message1 = "\n%s has %s coins left." % (person, coins)
print("Message 1 : ", message1)

# Format method give more control than "%s" would ever give :
message2 = '\n{} has {} coins left.'.format(person, coins)
print("Message 2 : ", message2)

message3 = '\n{1} has {0} coins left.'.format(person, coins)
print("Message 3 : ", message3)

message4 = '\n{person} has {coins} coins left.'.format(
    person=person, coins=coins)
print("Message 4 : ", message4)

player = {
    'person': 'Amith Rao',
    'coins': 3
}

message5 = '\n{person} has {coins} coins left.'.format(**player)
print("Message 5 : ", message5)

print("========================================================")
