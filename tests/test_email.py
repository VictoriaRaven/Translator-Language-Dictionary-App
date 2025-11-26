from typing import Optional
import webbrowser

def send_history_email(
    to_addr: str,
    subject: str,
    body: str,
    attachment_path: Optional[str] = None
):
    """
    Sends email via Outlook if available, otherwise falls back to mailto: link.
    Attachment may be None.
    """
    try:
        import win32com.client as win32
        outlook = win32.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)
        mail.To = to_addr
        mail.Subject = subject
        mail.Body = body

        if attachment_path:
            mail.Attachments.Add(attachment_path)

        mail.Send()
        return True

    except Exception:
        # fallback mailto
        import urllib.parse

        mailto = f"mailto:{to_addr}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
        webbrowser.open(mailto)
        return False
