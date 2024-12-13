import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    review TEXT NOT NULL
)
""")

# Insert sample reviews
reviews = [
    ("This product is amazing!",),
    ("I really disliked the experience.",),
    ("Not bad, but could be improved.",),
    ("Worst purchase ever.",),
    ("Highly recommend this to everyone.",)
]

cursor.executemany("INSERT INTO reviews (review) VALUES (?)", reviews)

# Commit changes and close connection
conn.commit()
conn.close()

print("Database setup complete!")
