n1 = int(input("Enter size of first dictionary: "))

d1 = {}

for _ in range(n1):
    key = input("Key: ")
    value = int(input("Value: "))
    d1[key] = value

n2 = int(input("Enter size of second dictionary: "))

d2 = {}

for _ in range(n2):
    key = input("Key: ")
    value = int(input("Value: "))
    d2[key] = value

final = {}

for key, value in d1.items():
    final[key] = value

for key, value in d2.items():
    if key in final:
        final[key] += value
    else:
        final[key] = value

print(final)