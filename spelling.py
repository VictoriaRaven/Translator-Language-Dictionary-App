#Multilingual spell-checking auto for searches only if online lanuage correct avalible.
#Supports: English-French-Spanish-Portuguese-Italian-Dutch-German-Polish-Russian ONLY
from functools import lru_cache
import re
try:
    import language_tool_python as lt
    from language_tool_python import LanguageTool, utils
    LANGUAGE_TOOL_AVAILABLE = True
except Exception:
    LANGUAGE_TOOL_AVAILABLE = False
    utils = None

#Supports: ONLY Ukrainian via SymSpell
# Optional Ukrainian fallback (SymSpell)
try:
    from symspellpy import SymSpell, Verbosity
    SYM_AVAILABLE = True
except Exception:
    SYM_AVAILABLE = False

# For auto-detecting input language
try:
    from langdetect import detect
    LANGDETECT_AVAILABLE = True
except Exception:
    LANGDETECT_AVAILABLE = False

# Detect Ukrainian letters
UKRAINIAN_CHARS = re.compile(r"[іІїЇєЄґҐ]")

# Build minimal SymSpell for Ukrainian ONLY if installed
sym_uk = None
if SYM_AVAILABLE:
    sym_uk = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    # minimal tiny dictionary
    base_uk = [
        "привіт", "слово", "текст", "книга",
        "переклад", "мова", "будинок", "вікно"
    ]
    for w in base_uk:
        sym_uk.create_dictionary_entry(w, 5)

class SpellChecker:
    """
    Wraps LanguageTool with caching and safe fallbacks.
    Supports languages auto with 'multilingual' mode.
    """

    def __init__(self):
        self.tools = {}
        if LANGUAGE_TOOL_AVAILABLE:
            # Preload supported languages (for speed)
            self.supported_languages = [
                "en-US", "fr", "es", "pt", "it", "nl", "de", "pl", "ru"
            ]
            for lang in self.supported_languages:
                try:
                    self.tools[lang] = LanguageTool(lang)
                except Exception:
                    continue
    @lru_cache(maxsize=500)                 
    def correct(self, text: str) -> str:
        """Return corrected text, cached for speed."""
        if not text:
            return text

        # Ukrainian detection
        if SYM_AVAILABLE and UKRAINIAN_CHARS.search(text) and sym_uk:
            suggestions = sym_uk.lookup_compound(text, max_edit_distance=2)
            if suggestions:
                return suggestions[0].term

        # Auto-detect language if possible
        lang_to_use = "en-US"  # default fallback
        if LANGUAGE_TOOL_AVAILABLE and LANGDETECT_AVAILABLE:
            try:
                from langdetect import detect
                detected_lang = detect(text)
                # Map langdetect codes to LT codes if needed
                lang_map = {
                    "en": "en-US",
                    "fr": "fr",
                    "es": "es",
                    "pt": "pt",
                    "it": "it",
                    "nl": "nl",
                    "de": "de",
                    "pl": "pl",
                    "ru": "ru",
                }
                lang_to_use = lang_map.get(detected_lang, "en-US")
            except Exception:
                lang_to_use = "en-US"

        # Use corresponding LanguageTool
        tool = self.tools.get(lang_to_use)
        if not tool:
            return text

        try:
            if LANGUAGE_TOOL_AVAILABLE:
                return tool.correct(text)
        except Exception:
            return text

        return text


# Global instance for fast repeated calls
SPELL_CHECKER = SpellChecker()


def auto_correct(text: str) -> str:
    """
    Public helper function for admin.py
    """
    return SPELL_CHECKER.correct(text)
