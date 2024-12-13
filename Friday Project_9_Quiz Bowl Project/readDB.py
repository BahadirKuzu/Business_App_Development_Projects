import sqlite3

# Function to read tables from the database
def read_database(db_file):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Retrieve all table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Check if there are any tables
        if not tables:
            print("No tables found in the database.")
            return
        
        # Print all tables
        print("Tables in the database:")
        for idx, table in enumerate(tables):
            print(f"{idx + 1}. {table[0]}")

        # Ask the user to select a table to view data
        while True:
            try:
                table_index = int(input("Enter the number of the table you want to view: ")) - 1
                if 0 <= table_index < len(tables):
                    break
                else:
                    print("Invalid number. Please select a valid table number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

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
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Call the function and specify the database file name
read_database('questions.db')
