import sqlite3

conn = sqlite3.connect("ice_cream.sqlite")

cursor = conn.cursor()
sql_query = """CREATE TABLE ice_cream (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price DOUBLE NOT NULL
);"""
    
cursor.execute(sql_query)
