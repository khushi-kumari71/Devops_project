import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        available_copies INTEGER NOT NULL
    )
''')

# Insert sample books
cursor.execute("INSERT INTO books (title, author, genre, available_copies) VALUES (?, ?, ?, ?)",
               ("Atomic Habits", "James Clear", "Self-help", 5))

cursor.execute("INSERT INTO books (title, author, genre, available_copies) VALUES (?, ?, ?, ?)",
               ("The Alchemist", "Paulo Coelho", "Fiction", 3))

conn.commit()
conn.close()

