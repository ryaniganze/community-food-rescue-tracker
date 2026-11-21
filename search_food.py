def search_food(db):
    print("\n--- Search Food ---")
    keyword = input("Enter a food name or location: ").strip()

    if not keyword:
        print("Please enter a search word.")
        return

    results = db.search_food(keyword)
    if not results:
        print("No matching food records were found.")
        return

    for food in results:
        print("-" * 40)
        print(f"Food ID: {food['id']}")
        print(f"Name: {food['name']}")
        print(f"Quantity: {food['quantity']} {food['unit']}")
        print(f"Location: {food['location']}")
        print(f"Expiry date: {food['expiry_date']}")
        print(f"Status: {food['status']}")