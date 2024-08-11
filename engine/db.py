import sqlite3

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name varchar(100), url varchar(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES(null, 'youtube', 'https://youtube.com/')"
cursor.execute(query)

conn.commit()