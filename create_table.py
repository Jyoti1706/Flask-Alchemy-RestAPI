import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()  # responsible for running and storing result.
create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username text, password text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items( id INTEGER PRIMARY KEY AUTOINCREMENT, name text, price real)"
cursor.execute(create_table)
cursor.execute("Insert into items values (1,'The Gita for Children',7.99)")
connection.commit()
connection.close()
