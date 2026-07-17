def grouping_helper(grouped,employ_info):
    for id,info in employ_info.items():
        depart=info["depart"]
        name=info["name"]

        if depart not in grouped:
            grouped[depart]=[]

        grouped[depart].append({
            "id":id,
            "name":name
        })

def printer(grouped):
    print("========== DEPARTMENT REPORT ==========")
    for depart,coll in grouped.items():
        print(depart.upper())
        print("------------------")
        for emp in coll:
            print(f"{emp['id']}. {emp['name']}")

n=int(input("Enter the number of employees info:"))

employ_info={}
for i in range(n):
    id,name,depart=input(f"Enter the info of {i+1}th employee:").split()
    employ_info[int(id)]={
        "name":name,
        "depart":depart
    }
grouped={}
grouping_helper(grouped,employ_info)

printer(grouped)