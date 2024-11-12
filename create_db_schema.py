import sqlite3

try:
    # Connect to the database
  conn = sqlite3.connect("database.sqlite")
  cursor = conn.cursor()

  # Read the SQL file
  with open('schema.sql', 'r') as sql_file:
      sql_script = sql_file.read()

  # Execute the SQL script
  cursor.executescript(sql_script)

  # Commit the changes and close the connection
  conn.commit()
  print("Tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()