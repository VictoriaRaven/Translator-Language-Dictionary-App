from settings import DEEP_TRANSLATOR_AVAILABLE
from settings import *
import sqlite3
# ------------- TRANSLATION HELPERS -------------
def sql_translate(word: str, lang_code: str):
    try:
        # Try English -> Other and Other -> English with dictionary rows
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        # First try: word in dictionary as english word for target language
        c.execute("SELECT translation FROM dictionary WHERE word = ? AND language = ?", (word.lower(), lang_code))
        r = c.fetchone()
        if r:
            conn.close()
            return r[0], False
        # Try reverse: word matches translation in target language -> return associated word
        c.execute("SELECT word FROM dictionary WHERE translation = ? AND language = ?", (word.lower(), lang_code))
        r = c.fetchone()
        conn.close()
        if r:
            return r[0], False
        return None, False
    except Exception as e:
        print("sql_translate error:", e)
    return None, False

def online_translate(word: str, target_code: str):
    if not DEEP_TRANSLATOR_AVAILABLE:
        return None
    try:
        return GoogleTranslator(source='auto', target=target_code).translate(word)
    except Exception as e:
        print("Online translate error:", e)
        return None