
# Community Food Rescue Tracker
# Main application
# Developer: Ryan Kamana Iganze

def display_menu():
    print("\n" + "=" * 50)
    print("       COMMUNITY FOOD RESCUE TRACKER")
    print("=" * 50)

    print("1. Add Surplus Food")
    print("2. View Available Food")
    print("3. Update Food Collection Status")
    print("4. Search for Food")
    print("0. Exit Program")

    print("=" * 50)


def main():
    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (0-4): "))

            if choice == 1:
                print("Add Surplus Food selected.")

            elif choice == 2:
                print("View Available Food selected.")

            elif choice == 3:
                print("Update Collection Status selected.")

            elif choice == 4:
                print("Search for Food selected.")

            elif choice == 0:
                print("Thank you for using our application!")
                break

            else:
                print("Invalid choice. Please select 0-4.")

        except ValueError:
            print("Error: Please enter a number.")


if __name__ == "__main__":
    main()
