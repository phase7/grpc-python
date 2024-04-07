import sqlite3

def initialize_db():
    conn = sqlite3.connect('items.db')
    c = conn.cursor()
    
    # Create table
    c.execute('''CREATE TABLE items (id TEXT PRIMARY KEY, name TEXT)''')
    
    # Insert initial items
    items = [('1', 'Item 1'), ('2', 'Item 2'), ('3', 'Item 3'), ('4', 'Item 4')]
    c.executemany('INSERT INTO items VALUES (?, ?)', items)
    
    # Save (commit) the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
