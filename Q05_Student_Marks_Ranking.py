def arrange(student):
    student.sort(key=lambda x: (-x[1], x[0]))
    return student

n = int(input("Enter the size of list: "))
student = []

for i in range(n):
    name, number = input(f"Enter the name and marks of {i+1}th student: ").split()
    student.append((name, int(number)))

result = arrange(student)

for i in range(len(result)):
    print(f"{i+1}. {result[i][0]} - {result[i][1]}")