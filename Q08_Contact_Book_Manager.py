def Search(contact_info,name):
    if name in contact_info:
        information=contact_info[name]
        print("========== CONTACT ==========")
        print(f"Name  : {name}")
        print(f"Phone : {information['phone']}")
        print(f"Email : {information['email']}")
    else:
        print("User not found")

def Updatephonenumber(contact_info,name,phone):
    if name in contact_info:
        contact_info[name]["phone"]=phone
        print("Phone number updated successfully.")

def Displayallcontact(contact_info):
    for name, details in contact_info.items():
        print(name)
        print(f"  Phone : {details['phone']}")
        print(f"  Email : {details['email']}")


n=int(input("Enter the number of contact:"))

contact_info={}
for i in range(n):
    name,phone,email=input(f"Enter the contact details of {i+1}th person:").split()
    contact_info[name]={
        "phone":int(phone),
        "email":email
    }

while True:
    print("\n===== MENU =====")
    print("1. Search Contact")
    print("2. Update Phone Number")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter the name:")
        Search(contact_info,name)
    elif choice==2:
        name=input("Enter the name:")
        phone=int(input("Enter the phone Number:"))
        Updatephonenumber(contact_info,name,phone)
    elif choice==3:
        Displayallcontact(contact_info)
    elif choice==4:
        break; 
    else:
        print("Invalid Choice")
