def helper(store):
    sorted_store = sorted(
        store.items(),
        key=lambda x: (-x[1]["unit"], x[1]["name"])
    )

    print("========== SALES LEADERBOARD ==========")
    for rank, (key, values) in enumerate(sorted_store, start=1):
        print(f"{rank}. {values['name']} - {values['unit']}")


n = int(input("Enter the number of product: "))

store = {}
for i in range(n):
    name, unit = input("Enter the details of product: ").split()
    store[i] = {
        "name": name,
        "unit": int(unit)
    }

helper(store)