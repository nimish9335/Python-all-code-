# ---------------- Numbers ----------------

nums = [5, 2, 9, 1, 7]

print("Original:", nums)

print("\nAscending:")
print(sorted(nums, key=lambda x: x))

print("\nDescending:")
print(sorted(nums, key=lambda x: -x))


# ---------------- Tuple ----------------

students = [
    ("Rahul", 90),
    ("Aman", 80),
    ("Nimish", 95),
    ("Karan", 90)
]

print("\nOriginal:")
print(students)

print("\nSort by Name:")
print(sorted(students, key=lambda x: x[0]))

print("\nSort by Marks:")
print(sorted(students, key=lambda x: x[1]))

print("\nSort by Marks Descending:")
print(sorted(students, key=lambda x: -x[1]))

print("\nSort by Marks then Name:")
print(sorted(students, key=lambda x: (x[1], x[0])))

print("\nSort by Marks Descending then Name:")
print(sorted(students, key=lambda x: (-x[1], x[0])))


# ---------------- String ----------------

words = ["python", "c", "java", "javascript", "cpp"]

print("\nOriginal Words:")
print(words)

print("\nSort by Length:")
print(sorted(words, key=lambda x: len(x)))

print("\nSort by Last Character:")
print(sorted(words, key=lambda x: x[-1]))


# ---------------- Dictionary ----------------

employees = [
    {"name": "Rahul", "salary": 50000},
    {"name": "Aman", "salary": 30000},
    {"name": "Nimish", "salary": 70000}
]

print("\nSort Dictionary by Salary:")
print(sorted(employees, key=lambda x: x["salary"]))

print("\nSort Dictionary by Name:")
print(sorted(employees, key=lambda x: x["name"]))