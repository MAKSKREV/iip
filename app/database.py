import sqlite3
from aiogram.types import PhotoSize

def init_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    
    # Create table for storing vopros2 interactions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vopros2_interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            group_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create table for storing vopros3 interactions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vopros3_interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            text TEXT,
            photo_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def log_vopros2_interaction(user_id, group_id):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO vopros2_interactions (user_id, group_id)
        VALUES (?, ?)
    ''', (user_id, group_id))
    
    conn.commit()
    conn.close()

def log_vopros3_interaction(user_id: int, text: str, photo: PhotoSize):
    try:
        conn = sqlite3.connect('bot_database.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO vopros3_interactions (user_id, text, photo_id)
            VALUES (?, ?, ?)
        ''', (user_id, text, photo.file_id))
        
        conn.commit()
        print(f"Successfully logged interaction for user {user_id}")
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()


def get_vopros3_interactions():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM vopros3_interactions')
    results = cursor.fetchall()
    
    conn.close()
    return results

def log_plus222_interaction(user_id: int, text: str, photo: PhotoSize):
    try:
        conn = sqlite3.connect('bot_database.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO vopros3_interactions (user_id, text, photo_id)
            VALUES (?, ?, ?)
        ''', (user_id, text, photo.file_id))
        
        conn.commit()
        print(f"Successfully logged plus222 interaction for user {user_id}")
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()
