def query(dict,id):
    if id in dict:
        print("Employee Details")
        print(f"id:{id}")
        print(f"Name:{dict[id][0]}")
        print(f"Department:{dict[id][1]}")
    else:
        print("Employee Not Found")



n=int(input("Enter the number of employees:"))
dict={}
for i in range(n):
    id,name,department=input(f"Enter the {i+1}th employee information:").split()
    dict[int(id)]=(name,department)

id=int(input("Enter the id:"))
query(dict,id)
