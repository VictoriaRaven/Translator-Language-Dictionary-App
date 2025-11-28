# ---------------- CS50 Modifications based on lessons--------------
import json
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False
try:
    import language_tool_python
    LANGUAGE_TOOL_AVAILABLE = True
except Exception:
    LANGUAGE_TOOL_AVAILABLE = False

# ---------------- Export: JSON & PDF ----------------
def export_history_json(path: str, rows):
    """
    Export history rows to JSON. 'rows' expected as iterable of tuples:
    (id, input_word, output_word, language, used_online, timestamp)
    """
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "input_word": r[1],
            "output_word": r[2],
            "language": r[3],
            "used_online": bool(r[4]),
            "timestamp": r[5]
        })
    try:
        with open(path, "w", encoding="utf8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True, None
    except Exception as e:
        return False, str(e)

def export_history_pdf(path: str, rows, title="Translation History"):
    """
    Export history to PDF w/reportlab if available with a font DejaVuSans
    If not, export to UTF-8 text file if reportlab is missing.
    """
    if REPORTLAB_AVAILABLE:
        try:
            import os
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            # Register the font **once**
            # Build an absolute path to the TTF file (works on all OS)
            FONT_PATH = os.path.join(
                os.path.dirname(__file__), "DejaVuSans", "DejaVuSans.ttf"
            )
            pdfmetrics.registerFont(TTFont("DejaVu", FONT_PATH))
            
            c = canvas.Canvas(path, pagesize=letter)
            width, height = letter
            margin = 40
            y = height - margin
            # Use the registered font by NAME
            c.setFont("DejaVu", 14)
            c.drawString(margin, y, title)
            y -= 20
            c.setFont("DejaVu", 10)
            for r in rows:
                line = f"{r[0]} | {r[5]} | {r[1]} -> {r[2]} ({r[3]}) [{'ONLINE' if r[4] else 'LOCAL'}]"
                c.drawString(margin, y, line[:120])
                y -= 14
                if y < margin:
                    c.showPage()
                    c.setFont("DejaVu", 10)
                    y = height - margin
            c.save()
            return True, None
        except Exception as e:
            print(f"[PDF FONT ERROR] Could not register font: {e}")
            return False, str(e)

    else:
        # fallback: simple .txt file as .pdf
        try:
            txt_path = path if path.lower().endswith(".txt") else path + ".txt"
            with open(txt_path, "w", encoding="utf8") as f:
                f.write(title + "\n\n")
                for r in rows:
                    f.write(f"{r[0]} | {r[5]} | {r[1]} -> {r[2]} ({r[3]}) [{'ONLINE' if r[4] else 'LOCAL'}]\n")
            return True, f"reportlab not installed; wrote text fallback to {txt_path}"
        except Exception as e:
            return False, str(e)
