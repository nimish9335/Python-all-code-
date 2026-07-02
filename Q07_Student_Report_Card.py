def report_card(Data,rolenumber):
    if rolenumber in Data:
        name=Data[rolenumber]["name"]
        math=Data[rolenumber]["math"]
        science=Data[rolenumber]["science"]
        english=Data[rolenumber]["english"]
        print("========== REPORT CARD ==========")
        print(f"Roll Number : {rolenumber}")
        print(f"Name        : {name}")
        print(f"Maths       : {math}")
        print(f"Science     : {science}")
        print(f"English     : {english}")

        total_marks=math+science+english
        avg_marks=total_marks/3
        print(f"Total       : {total_marks}")
        print(f"Average     : {avg_marks}")
    else:
        print("Student Not Found")

n=int(input("Enter the number of students information:"))
Data={}
for i in range(n):

    roleNumber,name,math,science,english=input(f"Enter the datails of {i+1}th student:").split()
    Data[int(roleNumber)] = {}
    Data[int(roleNumber)]["name"] = name
    Data[int(roleNumber)]["math"] = int(math)
    Data[int(roleNumber)]["science"] = int(science)
    Data[int(roleNumber)]["english"] = int(english)

stu_rolenumber=int(input("Enter the student rolenumbe:"))
report_card(Data,stu_rolenumber)