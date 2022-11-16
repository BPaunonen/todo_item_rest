import sqlite3

conn = sqlite3.connect('todos.db', check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Todos (
                Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                Content TEXT
                )""")

def get_all_todos():
        cursor.execute("SELECT * FROM Todos")
        return cursor.fetchall()
    
    
def get_single_todo(id):
        cursor.execute("SELECT * FROM Todos WHERE Id = ?", [id])
        row = cursor.fetchone()
        if row is None:
            return None
        rowDict = dict(zip([c[0] for c in cursor.description], row))
        return rowDict

def create_todo(content):
    with conn:
        cursor.execute("INSERT INTO Todos (Content) VALUES (?)", [content])
        conn.commit()
        return cursor.lastrowid

def update_todo(content, id):
    with conn:
        cursor.execute("UPDATE Todos SET Content = :content WHERE id = :id" ,
                    {'content': content, 'id':id} )
        conn.commit()
        return cursor.rowcount

def delete_todo(id):
    with conn:
        cursor.execute("DELETE FROM Todos WHERE id = ?", [id])
        conn.commit()
        return cursor.rowcount