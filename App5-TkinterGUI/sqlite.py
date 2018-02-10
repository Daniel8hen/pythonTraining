import psycopg2

# Steps to query DB:
# 1. Connect to DB
# 2. Create a cursor object
# 3. Write a SQL query
# 4. Commit changes to DB
# 5. Close connection (1)
def create_table():
#1
    conn =sqlite3.connect("lite.db")
#2
    cur = conn.cursor()
#3
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
#4
    conn.commit()
#5
    conn.close()

def insert(item, quantity, price):
#1
    conn =sqlite3.connect("lite.db")
#2
    cur = conn.cursor()
#3
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
#4
    conn.commit()
#5
    conn.close()

def view():
    conn =sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn =sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item, ))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn =sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? where item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

update(11, 6, "Water glass")
#delete("Wine Glass")
# insert("Coffee cup", 10, 5)
print(view())
