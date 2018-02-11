import sqlite3

#Session - OOP - now we'll insert everything to a class called Database
class Database:

    # the __init__ is a constructor method within the Database
    def __init__(self, db):
        conn =sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn =sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()
        return rows

    # Note - there's a default value ("") for a case where the user would like to seach by 1 value
    def search(self, title="", author="", year="", isbn=""):
        conn =sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year =? OR isbn =?", (title, author, year, isbn))
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn =sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id =?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn =sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()

# Testing
# insert("The earth", "John smith", 191, 4123915)
# delete(3)
# update (4, "The moon", "John Smooooth", 1917, 9124)
# print(view())
# print(search(author="John smith"))
