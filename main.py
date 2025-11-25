from gui import TranslatorApp
from database import init_db

def main():
    # Initialize database
    init_db()
    # Run the UI
    # show main app
    app = TranslatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()