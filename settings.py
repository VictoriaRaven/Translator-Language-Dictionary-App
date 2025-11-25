# deep_translator for online translation; if unavailable, disable online feature
import os

try:
    from deep_translator import GoogleTranslator
    DEEP_TRANSLATOR_AVAILABLE = True
except Exception:
    DEEP_TRANSLATOR_AVAILABLE = False

LANG_OPTIONS = [
    ("French", "fr"),
    ("Russian", "ru"),
    ("Ukrainian", "uk"),
    ("Spanish", "es"),
    ("Portuguese", "pt"),
    ("Italian", "it"),
    ("German", "de"),
    ("Dutch(Netherlands)", "nl"),
    ("Polish", "pl"),
]

TXT_FILES = {
    "fr": "data/fr_dictionary.txt",
    "ru": "data/ru_dictionary.txt",
    "uk": "data/ukr_dictionary.txt",
    "es": "data/sp_dictionary.txt",
    "pt": "data/por_dictionary.txt",
    "it": "data/ita_dictionary.txt",
    "de": "data/gr_dictionary.txt",
    "nl": "data/nth_dictionary.txt",
    "pl": "data/poh_dictionary.txt",
    "en": "data/eng_dictionary.txt",
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "data", "translations.db")
PAGE_SIZE = 20