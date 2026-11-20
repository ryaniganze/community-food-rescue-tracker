from database import Database
from add_food import add_food
from view_food import view_food
from update_status import update_collection_status
from search_food import search_food
 
 
def display_menu():
    print("\n===================================")
    print("     COMMUNITY FOOD RESCUE TRACKER")
    print("===================================")
    print("1. Add Surplus Food")
    print("2. View Available Food")
    print("3. Update Food Collection Status")
    print("4. Search Food")
    print("0. Exit")
def main():
    db = Database()
 
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
 
        if choice == "1":
            add_food(db)
        elif choice == "2":
            view_food(db)
        elif choice == "3":
            update_collection_status(db)
        elif choice == "4":
            search_food(db)
        elif choice == "0":
            print("Thank you for using Community Food Rescue Tracker.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 0.")
 
 
if __name__ == "__main__":
    main()
