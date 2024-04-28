import sqlite3

try:
    conn = sqlite3.connect('instance/db.sqlite')
    cur = conn.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO events
                          (title, decription, date) 
                           VALUES 
                          ('New year', 'New year in Shyszinsk', 24);"""

    count = cur.execute(sqlite_insert_query)
    conn.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
    cur.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
finally:
    if conn:
        conn.close()
        print("The SQLite connection is closed")