# ---------------- Input Validation ----------------
import re

INPUT_WORD_RE = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s\-\_'\.,]{1,200}$")
def validate_input_word(word: str) -> bool:
    """Stricter validation that allows letters, accents, digits and common punctuation."""
    if not word:
        return False
    return bool(INPUT_WORD_RE.fullmatch(word.strip()))