import sqlite3
from tkinter import messagebox
from settings import DB_NAME

# ----------------- DATABASE HELPERS -----------------
def init_db():
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        # dictionary as rows (word, translation, language)
        c.execute("""
        CREATE TABLE IF NOT EXISTS dictionary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            translation TEXT NOT NULL,
            language TEXT NOT NULL
        )
        """)
        c.execute("""
        CREATE INDEX IF NOT EXISTS idx_dictionary_word_lang ON dictionary(word, language)
        """)
        # history table
        c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_word TEXT,
            output_word TEXT,
            language TEXT,
            used_online INTEGER DEFAULT 0,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        print("init_db error:", e)
        messagebox.showerror("Database Error", f"Failed to initialize DB: {e}")
    finally:
        try:
            conn.close()
        except:
            pass

def insert_dictionary_row(word, translation, language):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
        INSERT INTO dictionary (word, translation, language)
        VALUES (?, ?, ?)
        """, (word.lower(), translation.lower(), language))
        conn.commit()
        conn.close()
    except Exception as e:
        print("insert_dictionary_row error:", e)
    finally:
        try:
            conn.close()
        except:
            pass

def update_dictionary_row(row_id, word, translation, language):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
        UPDATE dictionary SET word=?, translation=?, language=? WHERE id=?
        """, (word.lower(), translation.lower(), language, row_id))
        conn.commit()
        conn.close()
    except Exception as e:
        print("update_dictionary_row error:", e)
    finally:
        try:
            conn.close()
        except:
            pass

def delete_dictionary_row(row_id):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM dictionary WHERE id=?", (row_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("delete_dictionary_row error:", e)
    finally:
        try:
            conn.close()
        except:
            pass

def query_dictionary(filter_text=None, order_by="id DESC", limit=None, offset=None):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        sql = "SELECT id, word, translation, language FROM dictionary"
        params = []
        if filter_text:
            sql += " WHERE word LIKE ? OR translation LIKE ? OR language LIKE ?"
            like = f"%{filter_text}%"
            params.extend([like, like, like])
        sql += f" ORDER BY {order_by}"
        if limit is not None:
            sql += " LIMIT ?"
            params.append(limit)
        if offset is not None:
            sql += " OFFSET ?"
            params.append(offset)
        c.execute(sql, params)
        rows = c.fetchall()
        # total count for pagination
        count_sql = "SELECT COUNT(*) FROM dictionary"
        count_params = []
        if filter_text:
            count_sql += " WHERE word LIKE ? OR translation LIKE ? OR language LIKE ?"
            count_params.extend([like, like, like])
        c.execute(count_sql, count_params)
        total = c.fetchone()[0]
        conn.close()
        return rows, total
    except Exception as e:
        print("query_dictionary error:", e)
        return [], 0
    finally:
        try:
            conn.close()
        except:
            pass

def query_history(filter_text=None, order_by="id DESC", limit=None, offset=None):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        sql = "SELECT id, input_word, output_word, language, used_online, timestamp FROM history"
        params = []
        if filter_text:
            sql += " WHERE input_word LIKE ? OR output_word LIKE ? OR language LIKE ?"
            like = f"%{filter_text}%"
            params.extend([like, like, like])
        sql += f" ORDER BY {order_by}"
        if limit is not None:
            sql += " LIMIT ?"
            params.append(limit)
        if offset is not None:
            sql += " OFFSET ?"
            params.append(offset)
        c.execute(sql, params)
        rows = c.fetchall()
        # count
        count_sql = "SELECT COUNT(*) FROM history"
        count_params = []
        if filter_text:
            count_sql += " WHERE input_word LIKE ? OR output_word LIKE ? OR language LIKE ?"
            count_params.extend([like, like, like])
        c.execute(count_sql, count_params)
        total = c.fetchone()[0]
        conn.close()
        return rows, total
    except Exception as e:
        print("query_history error:", e)
        return [], 0
    finally:
        try:
            conn.close()
        except:
            pass

def save_history(input_word, output_word, language, used_online=False):
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
        INSERT INTO history (input_word, output_word, language, used_online)
        VALUES (?, ?, ?, ?)
        """, (input_word.lower(), output_word.lower(), language, 1 if used_online else 0))
        conn.commit()
        conn.close()
    except Exception as e:
        print("save_history error:", e)
    finally:
        try:
            conn.close()
        except:
            pass