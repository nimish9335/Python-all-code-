fruits = ["Apple", "Banana", "Mango", "Orange"]

# Create enumerate object
data = enumerate(fruits)

print("Enumerate Object :", data)
print("Type :", type(data))

# Convert to list
data = list(data)

print("\nList:")
print(data)

print("\nLoop:")
for index, value in data:
    print(f"{index} -> {value}")

print("\nLength:", len(data))

print("\nAccess:")
print(data[0])
print(data[1][0])    # Index
print(data[1][1])    # Value

print("\nOnly Values:")
for index, value in data:
    print(value)

print("\nOnly Index:")
for index, value in data:
    print(index)