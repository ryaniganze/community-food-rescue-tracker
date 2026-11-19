# COMMUNITY FOOD RESCUE TRACKER

## 1. Project Overview

The Community Food Rescue Tracker is a Python-based terminal application designed to help communities manage surplus food donations and collections.

The project aims to reduce food waste by making it easier to record available surplus food, view food donations and track their collection status.

The application uses Python and an SQLite database to organize and store food information.

## 2. Problem Statement

Food waste is a significant challenge in many communities. Restaurants, shops and individuals may have surplus food that could be useful to people in need, but there is not always an organized way to record and track these donations.

Our project addresses this problem by developing a simple application that allows users to record surplus food, check available donations and monitor food collections.

## 3. Project Objectives

Our main objectives are:

- To provide a simple way to record surplus food donations.
- To allow users to view available food.
- To track whether donated food has been collected.
- To store food information for future access.
- To contribute to reducing food waste in our communities.

## 4. Application Features

The application is planned to include the following features:

1. **Add Surplus Food:** Allows users to enter food names, quantities, conditions, locations and expiry dates.
2. **View Available Food:** Displays food records that are available for collection.
3. **Update Collection Status:** Allows users to update food records when donations have been collected.
4. **Search for Food:** Allows users to search for food by name or location.
5. **Exit Program:** Allows users to close the application safely.

## 5. Technologies Used

- Python – Main programming language.
- SQLite – Database management and permanent data storage.
- Visual Studio Code – Development environment.
- Git and GitHub – Version control and teamwork.

## 6. Project Structure

```text
community-food-rescue-tracker/
│
├── main.py
├── database.py
├── add_food.py
├── view_food.py
├── update_status.py
├── search_food.py
├── test_app.py
├── food_rescue.db
├── README.md
└── .gitignore
```

## 7. Installation and Setup

### Requirements

- Python 3 installed on your computer.
- Git installed.
- Visual Studio Code or another Python IDE.

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Open the project folder

```bash
cd community-food-rescue-tracker
```

### Step 3: Run the application

```bash
python main.py
```

Note: SQLite is included with Python through the sqlite3 module, so a separate database server is not required.

## 8. How to Use the Application

1. Run the application using Python.
2. Select an option from the main menu.
3. Enter the requested information.
4. Follow the instructions displayed on the terminal.
5. View or update food records when necessary.
6. Select 0 to exit the application.

## 9. Database Management

The application uses SQLite to store food donation and collection information.

The database keeps records such as:

- Food ID
- Food name
- Quantity
- Food condition
- Food location
- Expiry date
- Collector name
- Collection date
- Collection status

This allows information to remain available even after the application is closed.

## 10. Team Members and Responsibilities

| Member | GitHub Username | Responsibility |
|---|---|---|
| Ryan Iganze | ryaniganze | Main application and menu |
| Tona Faradowza | Tona-tech-byte | Database management |
| Kamikazi Shekinah | Shekinah2807 | Adding surplus food |
| Karemera Ochri | Ochr1 | Viewing available food |
| Keza Fiorella | DembaFiorella | Updating collection status |
| Jeremie Rufora | rufora | Search, testing and documentation |

## 11. Testing

The application will be tested to ensure that:

- Users can add food records successfully.
- Available food records are displayed correctly.
- Collection statuses can be updated.
- Search functionality works correctly.
- Invalid inputs are handled without crashing the application.
- Food information remains saved in the database.

## 12. Future Improvements

Possible future improvements include:

- Adding a graphical user interface.
- Introducing user accounts and login functionality.
- Sending notifications about food close to expiry.
- Adding more search and filtering options.
- Connecting food donors with collection organizations.

## 13. Project Mission

Our mission is to contribute to reducing food waste by providing a simple digital solution that helps communities record surplus food, identify available donations and track food collections.

**Together, we can reduce food waste and support communities.**