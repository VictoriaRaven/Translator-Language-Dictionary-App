import webbrowser, os

# ---------------- Email connector (OUTLOOK ONLY) --------------
def send_history_email(to_addr: str, subject: str, body: str, attachment_path: str = None):
    """
    Sends email using:
      1. MS Outlook (if installed)
      2. Otherwise, fallback to mailto
    """
    # 1. OUTLOOK AVAILABLE? Try to import Outlook COM (Windows only)
    try:
        import win32com.client as win32
        OUTLOOK_AVAILABLE = True
    except Exception:
        OUTLOOK_AVAILABLE = False

    if OUTLOOK_AVAILABLE:
        try:
            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = to_addr
            mail.Subject = subject
            mail.Body = body
            # Attach file only if exists
            if attachment_path and os.path.exists(attachment_path):
                mail.Attachments.Add(os.path.abspath(attachment_path))
            mail.Display()   # opens draft window
            return True, None
        except Exception as e:
            # Outlook installed but failed → fallback
            print("Outlook error:", e)

    # 2. MAILTO FALLBACK
    try:
        import urllib.parse
        subject_enc = urllib.parse.quote(subject)
        body_enc = urllib.parse.quote(body)
        mailto_url = f"mailto:{to_addr}?subject={subject_enc}&body={body_enc}"
        webbrowser.open(mailto_url)
        return True, "Outlook unavailable — used mailto (no attachment support)."
    except Exception as e:
        return False, str(e)