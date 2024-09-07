import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name varchar(100), path varchar(1000))"
# cursor.execute(query)

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), url varchar(1000))"
# cursor.execute(query)

# query = "CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name varchar(100), mobile_no varchar(255), email varchar(255))"
# cursor.execute(query)

conn.commit()