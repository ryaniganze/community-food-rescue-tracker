from datetime import date
 
 
def update_collection_status(db):
    print("\n--- Update Collection Status ---")
 
    try:
        food_id = int(input("Enter the food ID: ").strip())
        if food_id <= 0:
            print("Food ID must be a positive number.")
            return
    except ValueError:
        print("Please enter a valid whole-number food ID.")
        return
 
    food = db.get_food_by_id(food_id)
    if food is None:
        print("No food record was found with that ID.")
        return
 
    if food["status"] != "Available":
        print("This food has already been collected or is unavailable.")
        return
 
    collector_name = input("Collector name: ").strip()
    if not collector_name:
        print("Collector name cannot be empty.")
        return
 
    collection_date = input(
        f"Collection date (YYYY-MM-DD, default {date.today()}): "
    ).strip()
    if not collection_date:
        collection_date = date.today().isoformat()
 
    try:
        parsed_date = date.fromisoformat(collection_date)
        if parsed_date > date.today():
            print("Collection date cannot be in the future.")
            return
    except ValueError:
        print("Enter the collection date in YYYY-MM-DD format.")
        return
 
    updated = db.update_collection(food_id, collector_name, collection_date)
    if updated:
        print("Collection status updated to Collected.")
    else:
        print("The record could not be updated. Please check its status.")
