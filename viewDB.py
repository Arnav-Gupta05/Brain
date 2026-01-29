# View and reset database memory entries

# view
import sqlite3

conn = sqlite3.connect("memory.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM memory")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()



# # Clear Database
# from database import get_connection

# conn = get_connection()
# cursor = conn.cursor()

# cursor.execute("DELETE FROM memory")
# cursor.execute("DELETE FROM sqlite_sequence WHERE name='memory'")

# conn.commit()
# conn.close()

# print("Table and ID sequence reset")
