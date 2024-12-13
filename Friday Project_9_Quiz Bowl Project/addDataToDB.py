import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# List of categories
categories = ['Countries', 'Sports', 'Movies', 'Travel', 'Nature']

# Function to drop existing tables
def drop_tables():
    for category in categories:
        cursor.execute(f"DROP TABLE IF EXISTS {category}")
    conn.commit()

# Function to create a table for each category
def create_category_table(category_name):
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {category_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
    ''')
    conn.commit()

# Drop existing tables and create new ones
drop_tables()
for category in categories:
    create_category_table(category)

# Function to insert a question into a category table
def insert_question(category_name, question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute(f'''
    INSERT INTO {category_name} (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions for each category with labeled options (A, B, C, D)
questions_data = {
    'Countries': [
        ("What is the capital of France?", "A) Paris", "B) London", "C) Berlin", "D) Madrid", "A) Paris"),
        ("Which country is known as the Land of the Rising Sun?", "A) China", "B) Thailand", "C) Japan", "D) Korea", "C) Japan"),
        ("Which country is the largest in the world by land area?", "A) USA", "B) Russia", "C) China", "D) India", "B) Russia"),
        ("Which continent has the highest number of countries?", "A) Asia", "B) Africa", "C) Europe", "D) South America", "B) Africa"),
        ("What is the currency of Japan?", "A) Yen", "B) Dollar", "C) Euro", "D) Won", "A) Yen"),
        ("Which country is famous for tulips?", "A) Netherlands", "B) Switzerland", "C) Belgium", "D) France", "A) Netherlands"),
        ("Which country has the highest number of islands?", "A) Philippines", "B) Sweden", "C) Indonesia", "D) Canada", "B) Sweden"),
        ("What is the capital of Canada?", "A) Toronto", "B) Vancouver", "C) Ottawa", "D) Montreal", "C) Ottawa"),
        ("Which country is home to the kangaroo?", "A) India", "B) Australia", "C) New Zealand", "D) South Africa", "B) Australia"),
        ("What is the official language of Brazil?", "A) Portuguese", "B) Spanish", "C) French", "D) English", "A) Portuguese")
    ],
    'Sports': [
        ("Which sport uses a racket?", "A) Soccer", "B) Basketball", "C) Tennis", "D) Boxing", "C) Tennis"),
        ("How many players are on a soccer team?", "A) 11", "B) 9", "C) 10", "D) 8", "A) 11"),
        ("Which country won the 2018 FIFA World Cup?", "A) Germany", "B) Argentina", "C) France", "D) Brazil", "C) France"),
        ("What is the highest score in bowling?", "A) 100", "B) 200", "C) 250", "D) 300", "D) 300"),
        ("Which sport is known as the 'king of sports'?", "A) Basketball", "B) Soccer", "C) Baseball", "D) Cricket", "B) Soccer"),
        ("In which sport would you perform a slam dunk?", "A) Basketball", "B) Tennis", "C) Soccer", "D) Golf", "A) Basketball"),
        ("What is the length of an Olympic swimming pool?", "A) 25m", "B) 50m", "C) 100m", "D) 75m", "B) 50m"),
        ("Which sport is associated with Wimbledon?", "A) Cricket", "B) Golf", "C) Tennis", "D) Rugby", "C) Tennis"),
        ("How many points is a touchdown worth in American football?", "A) 3", "B) 5", "C) 6", "D) 7", "C) 6"),
        ("Which country invented the sport of cricket?", "A) Australia", "B) India", "C) England", "D) South Africa", "C) England")
    ],
    'Movies': [
        ("Who directed 'Inception'?", "A) Christopher Nolan", "B) Steven Spielberg", "C) James Cameron", "D) Quentin Tarantino", "A) Christopher Nolan"),
        ("In which movie does the character 'Forrest Gump' appear?", "A) Titanic", "B) Forrest Gump", "C) The Godfather", "D) Shrek", "B) Forrest Gump"),
        ("Which movie features the song 'Let It Go'?", "A) Moana", "B) Frozen", "C) Tangled", "D) Toy Story", "B) Frozen"),
        ("Who played Jack in Titanic?", "A) Leonardo DiCaprio", "B) Brad Pitt", "C) Johnny Depp", "D) Tom Cruise", "A) Leonardo DiCaprio"),
        ("Which movie series has a character named 'Iron Man'?", "A) DC", "B) Marvel", "C) Star Wars", "D) Harry Potter", "B) Marvel"),
        ("Who played the Joker in 'The Dark Knight'?", "A) Heath Ledger", "B) Joaquin Phoenix", "C) Jared Leto", "D) Jack Nicholson", "A) Heath Ledger"),
        ("Which animated movie is about toys coming to life?", "A) Shrek", "B) Frozen", "C) Toy Story", "D) Cars", "C) Toy Story"),
        ("In 'The Matrix', what color is the pill that Neo takes?", "A) Blue", "B) Green", "C) Yellow", "D) Red", "D) Red"),
        ("Which movie is famous for the line 'I'll be back'?", "A) Terminator", "B) Rocky", "C) Predator", "D) Rambo", "A) Terminator"),
        ("What is the name of the hobbit played by Elijah Wood in 'The Lord of the Rings'?", "A) Frodo", "B) Sam", "C) Merry", "D) Pippin", "A) Frodo")
    ],
    'Travel': [
        ("Which city is known as the Big Apple?", "A) Los Angeles", "B) Chicago", "C) New York", "D) San Francisco", "C) New York"),
        ("Where is the Eiffel Tower located?", "A) Berlin", "B) Madrid", "C) Paris", "D) Rome", "C) Paris"),
        ("Which country has the Great Wall?", "A) India", "B) China", "C) Japan", "D) South Korea", "B) China"),
        ("Which is the tallest building in the world?", "A) Shanghai Tower", "B) Burj Khalifa", "C) Eiffel Tower", "D) One World Trade Center", "B) Burj Khalifa"),
        ("Where would you find the Colosseum?", "A) Athens", "B) Rome", "C) Paris", "D) London", "B) Rome"),
        ("Which city is famous for its canals?", "A) Venice", "B) Amsterdam", "C) Copenhagen", "D) Tokyo", "A) Venice"),
        ("Which country has a city called Bangkok?", "A) China", "B) Thailand", "C) Vietnam", "D) Malaysia", "B) Thailand"),
        ("What is the capital of Egypt?", "A) Cairo", "B) Beirut", "C) Riyadh", "D) Dubai", "A) Cairo"),
        ("Which desert is the largest in the world?", "A) Gobi", "B) Kalahari", "C) Sahara", "D) Arctic", "C) Sahara"),
        ("Which city has the Christ the Redeemer statue?", "A) Lima", "B) Bogota", "C) Rio de Janeiro", "D) Buenos Aires", "C) Rio de Janeiro")
    ],
    'Nature': [
        ("What is the largest mammal?", "A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Shark", "B) Blue Whale"),
        ("What process do plants use to make food?", "A) Respiration", "B) Digestion", "C) Photosynthesis", "D) Fermentation", "C) Photosynthesis"),
        ("What is the most common gas in the Earth's atmosphere?", "A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen", "B) Nitrogen"),
        ("How many legs does a spider have?", "A) 6", "B) 8", "C) 10", "D) 12", "B) 8"),
        ("What is the tallest type of grass?", "A) Bamboo", "B) Wheat", "C) Corn", "D) Reed", "A) Bamboo"),
        ("What is the largest land animal?", "A) Elephant", "B) Giraffe", "C) Rhino", "D) Hippopotamus", "A) Elephant"),
        ("Which ocean is the largest?", "A) Indian", "B) Atlantic", "C) Arctic", "D) Pacific", "D) Pacific"),
        ("What type of animal is a Komodo dragon?", "A) Mammal", "B) Reptile", "C) Bird", "D) Amphibian", "B) Reptile"),
        ("What do you call a group of lions?", "A) Pack", "B) Flock", "C) Pride", "D) Herd", "C) Pride"),
        ("Which is the tallest mountain in the world?", "A) K2", "B) Kangchenjunga", "C) Everest", "D) Makalu", "C) Everest")
    ]
}

# Insert questions into each category table
for category, questions in questions_data.items():
    for question in questions:
        insert_question(category, *question)

print("All questions have been added to the database.")

# Function to read data from the database and display it
def read_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all tables
    print("Tables in the database:")
    for idx, table in enumerate(tables):
        print(f"{idx + 1}. {table[0]}")
    
    # Ask the user to select a table
    table_index = int(input("Enter the number of the table you want to view: ")) - 1
    selected_table = tables[table_index][0]
    
    # Retrieve and print all data from the selected table
    print(f"\nData from table '{selected_table}':")
    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()
    
    # Print column headers
    column_names = [description[0] for description in cursor.description]
    print("\t".join(column_names))
    
    # Print each row of data
    for row in rows:
        print("\t".join(str(cell) for cell in row))
    
    # Close the connection
    conn.close()

# Call the function to read data from the database
read_database('questions.db')
