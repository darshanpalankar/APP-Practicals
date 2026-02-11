import sqlite3 as sql

print("Performed By 42 & 47")

def connect_DB(db_name) -> sql:
    connection = sql.connect(db_name)  # Connect to the database
    print(f"Connected to database {db_name}")
    return connection

def create_table(connection):
    cur = connection.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    
    connection.commit()
    print("Table 'students' created successfully.")

def insert_data(connection):
    cur = connection.cursor()
    cur.execute("""INSERT INTO students(name,age) VALUES('Yuvraj','18')""")
    cur.execute("""INSERT INTO students(name,age) VALUES('Darshan','17')""")
    cur.execute("""INSERT INTO students(name,age) VALUES('Kunal','19')""")
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\nInserted data in 'students' table:")
    for row in rows:
        print(row)

def update_data(connection):
    cur = connection.cursor()
    cur.execute("UPDATE students SET age = 18 WHERE name = 'Darshan' ")
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\nUpdated data in 'students' table:")
    for row in rows:
        print(row)

def display_data(connection):
    cur = connection.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\nCurrent data in 'students' table:")
    for row in rows:
        print(row)

def drop_table(connection):
    cursor = connection.cursor() 
    cursor.execute("DROP TABLE IF EXISTS Students")
    connection.commit()
    print("\nTable 'students' dropped successfully.")


def main():
    # Step 1: Connect to the SQLite database (it creates the database if it doesn't exist)
    connection = connect_DB("Student_Information.db")

    # Step 2: Create the 'users' table
    create_table(connection)

    # Step 3: Insert data into the table
    insert_data(connection)

    # Step 4: Update a user's data
    update_data(connection) 

    # Step 5: Display data 
    display_data(connection)

    # Step 6: Drop the table (optional)
    drop_table(connection)

    # Close the connection
    connection.close()

if __name__ == "__main__":

    main()
