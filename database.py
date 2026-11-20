import sqlite3
from dataclasses import dataclass
 
 
@dataclass
class Food:
    name: str
    quantity: float
    unit: str
    condition: str
    location: str
    expiry_date: str
 
 
class Database:
    def __init__(self, db_name="food_rescue.db"):
        self.db_name = db_name
        self.initialize()
 
    def connect(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection
 
    def initialize(self):
        with self.connect() as connection:
            connection.execute("""
                CREATE TABLE IF NOT EXISTS food (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity REAL NOT NULL CHECK(quantity > 0),
                    unit TEXT NOT NULL,
                    condition TEXT NOT NULL,
                    location TEXT NOT NULL,
                    expiry_date TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Available',
                    collector_name TEXT,
                    collection_date TEXT
                )
            """)
 
    def add_food(self, food):
        with self.connect() as connection:
            cursor = connection.execute("""
                INSERT INTO food
                (name, quantity, unit, condition, location, expiry_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (food.name, food.quantity, food.unit, food.condition,
                  food.location, food.expiry_date))
            return cursor.lastrowid
 
    def get_available_food(self):
        with self.connect() as connection:
            return connection.execute("""
                SELECT * FROM food
                WHERE status = 'Available'
                ORDER BY expiry_date, id
            """).fetchall()
 
    def get_all_food(self):
        with self.connect() as connection:
            return connection.execute(
                "SELECT * FROM food ORDER BY id"
            ).fetchall()
 
    def get_food_by_id(self, food_id):
        with self.connect() as connection:
            return connection.execute(
                "SELECT * FROM food WHERE id = ?", (food_id,)
            ).fetchone()
 
    def update_collection(self, food_id, collector_name, collection_date):
        with self.connect() as connection:
            cursor = connection.execute("""
                UPDATE food
                SET status = 'Collected',
                    collector_name = ?,
                    collection_date = ?
                WHERE id = ? AND status = 'Available'
            """, (collector_name, collection_date, food_id))
            return cursor.rowcount == 1
 
    def search_food(self, keyword):
        pattern = f"%{keyword}%"
        with self.connect() as connection:
            return connection.execute("""
                SELECT * FROM food
                WHERE name LIKE ? OR location LIKE ?
                ORDER BY expiry_date, id
            """, (pattern, pattern)).fetchall()