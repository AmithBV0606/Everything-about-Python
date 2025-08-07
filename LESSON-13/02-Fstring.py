# Fstring :
person = "Amith"
coins = 3

player = {
    'person': 'Amith Rao',
    'coins': 3
}

f_string_message1 = f"\n{person} has {coins} coins left."
print(f_string_message1)

f_string_message2 = f"\n{person} has {5 * 5} coins left."
print(f_string_message2)

f_string_message3 = f"\n{person.lower()} has {5 * 5} coins left."
print(f_string_message3)

f_string_message4 = f"\n{player['person']} has {5 * 5} coins left."
print(f_string_message4)

print("========================================================")

# Formatting Options :
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n") # f = fixed

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

print("")
for num in range(1, 11):
    print(f"{num} divided by 2.25 is {num / 2.25:.2f}")