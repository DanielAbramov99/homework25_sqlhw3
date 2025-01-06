# import sqlite3
#
# conn = sqlite3.connect("hw_solution.db")
# conn.row_factory = sqlite3.Row
#
# cursor = conn.cursor()
#
# 1
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS shopping (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     amount INTEGER
# )
# ''')

# 2
# cursor.execute('''INSERT INTO shopping VALUES (1, 'Avokado', 5);''')
# cursor.execute('''INSERT INTO shopping VALUES (2, 'Milk', 2);''')
# cursor.execute('''INSERT INTO shopping VALUES (3, 'Bread', 3);''')
# cursor.execute('''INSERT INTO shopping VALUES (4, 'Chocolate', 8);''')
# cursor.execute('''INSERT INTO shopping VALUES (5, 'Bamba', 5);''')
# cursor.execute('''INSERT INTO shopping VALUES (6, 'Orange', 10);''')
# conn.commit()
# conn.close()
# 3
# cursor.execute('SELECT * FROM shopping')
# rows = cursor.fetchall()
# print("Data in 'shopping' table:")
# for row in rows:
#     print(tuple(row))
#
# conn.close()

# 4
# cursor.execute('SELECT * FROM shopping WHERE amount > 5')
# rows=cursor.fetchall()
# print("Data in 'shopping' table:")
# for row in rows:
#     print(tuple(row))
#
# conn.close()

# 5
# cursor.execute('DELETE FROM shopping WHERE name LIKE "orange"')
# conn.commit()
# cursor.execute('SELECT * FROM shopping')
# rows = cursor.fetchall()
# print("Data in 'shopping' table:")
# for row in rows:
#     print(tuple(row))
#
# conn.close()

# 6
# cursor.execute('UPDATE shopping SET name = "bisli" Where name LIKE "bamba"')
# cursor.execute('UPDATE shopping SET amount == 1 Where name LIKE "milk" ')
# conn.commit()
# cursor.execute('SELECT * FROM shopping')
# rows = cursor.fetchall()
# print("Data in 'shopping' table:")
# for row in rows:
#     print(tuple(row))
#
# conn.close()
#
# 7
# cursor.execute('SELECT COUNT(*) FROM shopping')
# count = cursor.fetchone()[0]
# print(f"amount of items:{count} ")
# conn.close()
#
# 8
# cursor.execute('SELECT * FROM shopping WHERE id > 0')
# rows = cursor.fetchall()
# print("Data in 'shopping' table:")
# for row in rows:
#     print(tuple(row))
#
# conn.close()

