#Multilingual spell-checking auto for searches only if online lanuage correct avalible.
#Supports: English-French-Spanish-Portuguese-Italian-Dutch-German-Polish-Russian ONLY
from functools import lru_cache
import re
from typing import Any, Optional
from language_tool_python.utils import correct
try:
    import language_tool_python as lt
    from language_tool_python import utils
    LANGUAGE_TOOL_AVAILABLE = True
except Exception:
    LANGUAGE_TOOL_AVAILABLE = False
    lt = None
    utils = None

#Supports: ONLY Ukrainian via SymSpell
# Optional Ukrainian fallback (SymSpell)
try:
    from symspellpy import SymSpell, Verbosity
    SYM_AVAILABLE = True
except Exception:
    SYM_AVAILABLE = False

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
        if LANGUAGE_TOOL_AVAILABLE:
            try:
                # Load ONCE → slow the first time, fast after
                self.tool = lt.LanguageTool("multilingual")
            except Exception:
                self.tool = None
        else:
            self.tool = None

    @lru_cache(maxsize=500)
    def correct(self, text: str) -> str:
        """Return corrected text, cached for speed."""
        if not text or not self.tool:
            return text

        try:
            matches = self.tool.check(text)
            if not matches:
                return text
            return utils.correct(text, matches) if utils else text
        except Exception:
            # If LanguageTool fails → return original text
            return text


# GLOBAL instance so admin.py doesn't reload it each time
SPELL_CHECKER = SpellChecker()


def auto_correct(text: str) -> str:
    """
    Public helper function for admin.py
    """
    return SPELL_CHECKER.correct(text)