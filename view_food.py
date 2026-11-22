def view_food(db):
    print("\n--- Available Food ---")
    foods = db.get_available_food()
 
    if not foods:
        print("There is currently no food available for collection.")
        return
 
    for food in foods:
        print("-" * 40)
        print(f"Food ID: {food['id']}")
        print(f"Name: {food['name']}")
        print(f"Quantity: {food['quantity']} {food['unit']}")
        print(f"Condition: {food['condition']}")
        print(f"Location: {food['location']}")
        print(f"Expiry date: {food['expiry_date']}")
        print(f"Status: {food['status']}")