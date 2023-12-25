import sqlite3
connection = sqlite3.connect("squ.db")
cur = connection.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER, name, status, species, type, gender, origin_name, origin_url, location_name, location_url, image)''')
# commit the changes to db
#print(cur.execute('SELECT * FROM users ORDER BY id DESC LIMIT 1;').fetchall()[0][0])

#cur.execute('UPDATE users SET name = ? WHERE id = ?', (f"{row2[1]}", "1"))
"""cur.execute('INSERT INTO users VALUES (?, ?, ?)', row)"""
"""cur.execute(f'UPDATE users SET  name={row2[1]} WHERE id = 1')"""
#print(cur.execute('SELECT * FROM users').fetchall())
cur.execute('DROP TABLE users;')
connection.commit()
# close the connection
connection.close()