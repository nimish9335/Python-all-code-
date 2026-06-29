name = ["Nimish", "Rahul", "Aman"]
age = [21, 22, 20]
city = ["Ujjain", "Delhi", "Indore"]

# Create zip object
data = zip(name, age, city)

print("Zip Object :", data)
print("Type :", type(data))

# Convert to list
data = list(data)

print("\nList:")
print(data)

print("\nLoop:")
for n, a, c in data:
    print(f"Name: {n}, Age: {a}, City: {c}")

print("\nUsing enumerate():")
for i, (n, a, c) in enumerate(data):
    print(f"{i} -> {n}, {a}, {c}")

print("\nLength:", len(data))

print("\nAccess:")
print(data[0])
print(data[1][0])   # Rahul
print(data[2][2])   # Indore