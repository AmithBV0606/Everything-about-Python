from functools import reduce

names = ["Amith B V", "Killers From Northside", "BLAH Salesman"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)