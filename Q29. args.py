def calculate(operation, *args):
    print("Operation :", operation)
    print("Arguments :", args)
    print("Type :", type(args))

    print("\nLoop:")
    for i, value in enumerate(args):
        print(f"Index {i} -> {value}")

    print("\nLength :", len(args))
    print("Maximum :", max(args))
    print("Minimum :", min(args))
    print("Sum :", sum(args))

    result = 1
    for num in args:
        result *= num
    print("Product :", result)


calculate("Math", 10, 20, 30, 40, 50)