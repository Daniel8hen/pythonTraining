import sqlite3

#Session - OOP - now we'll insert everything to a class called Database
class Database:

    # the __init__ is a constructor method within the Database
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    # Note - there's a default value ("") for a case where the user would like to seach by 1 value
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title =? OR author =? OR year =? OR isbn =?", (title, author, year, isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id =?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?", (title, author, year, isbn, id))
        self.conn.commit()

    # Destructor
    def __del__(self):
        self.conn.close()

# Testing
# insert("The earth", "John smith", 191, 4123915)
# delete(3)
# update (4, "The moon", "John Smooooth", 1917, 9124)
# print(view())
# print(search(author="John smith"))
