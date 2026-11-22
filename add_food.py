from datetime import date
from database import Food
 
 
def add_food(db):
    print("\n--- Add Surplus Food ---")
    name = input("Food name: ").strip()
    if not name:
        print("Food name cannot be empty.")
        return
 
    try:
        quantity = float(input("Quantity: ").strip())
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number for quantity.")
        return
 
    unit = input("Unit (e.g. kg, packets, boxes): ").strip()
    condition = input("Food condition (e.g. fresh, packaged): ").strip()
    location = input("Pickup location: ").strip()
    expiry_date = input("Expiry date (YYYY-MM-DD): ").strip()
 
    if not all([unit, condition, location, expiry_date]):
        print("All fields are required.")
        return
 
    try:
        expiry = date.fromisoformat(expiry_date)
        if expiry < date.today():
            print("Expiry date cannot be in the past.")
            return
    except ValueError:
        print("Enter the expiry date in YYYY-MM-DD format.")
        return
 
    food = Food(name, quantity, unit, condition, location, expiry_date)
    food_id = db.add_food(food)
    print(f"Food added successfully. Food ID: {food_id}")