def student(**kwargs):
    print("Dictionary :", kwargs)
    print("Type :", type(kwargs))

    print("\nKeys:")
    print(kwargs.keys())

    print("\nValues:")
    print(kwargs.values())

    print("\nItems:")
    print(kwargs.items())

    print("\nLoop:")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")

    print("\nAccess:")
    print("Name :", kwargs["name"])
    print("Age :", kwargs["age"])

    print("\nUsing get():")
    print("City :", kwargs.get("city"))
    print("Phone :", kwargs.get("phone", "Not Available"))


student(
    name="Nimish",
    age=21,
    college="NIT Raipur",
    branch="Metallurgy",
    cgpa=8.4,
    city="Ujjain"
)