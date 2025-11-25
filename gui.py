import threading
import tkinter as tk
from tkinter import ttk, messagebox

from database import *
from settings import LANG_OPTIONS, DEEP_TRANSLATOR_AVAILABLE
from translation import sql_translate, online_translate
from validation import validate_input_word
from admin_panel import AdminPanel

# ---------------- Main Application ----------------
class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        if test_mode:
            # Hide the GUI so pytest does not open real windows
            self.master = None
            self.withdraw()
        self.title("Translator App")
        self.geometry("500x400")

        # Title
        title = tk.Label(self, text="Translator App", font=("Arial", 18, "bold"))
        title.pack(pady=10)

        # Word input
        tk.Label(self, text="Enter word:").pack()
        self.word_input = tk.Text(
            self,
            font=("Arial", 14),
            height=4,
            width=50,
            wrap="word"
        )
        self.word_input.pack(pady=5, fill="x", padx=10)

        # Language selector
        tk.Label(self, text="Select language:").pack()
        self.lang_var = tk.StringVar()
        self.lang_menu = ttk.Combobox(
            self,
            values=[l[0] for l in LANG_OPTIONS],
            textvariable=self.lang_var,
            state="readonly"
        )
        self.lang_menu.set(LANG_OPTIONS[0][0])
        self.lang_menu.pack(pady=5)

        # Online toggle
        self.use_online_var = tk.IntVar(value=1 if DEEP_TRANSLATOR_AVAILABLE else 0)
        tk.Checkbutton(self, text="Use Online Translation", variable=self.use_online_var).pack(pady=3)

        # Clear button (Top)
        clear_button = tk.Button(
            self,
            text="Clear",
            command=self.clear,
            bg="#e53935",
            fg="white",
            font=("Arial", 12),
        )
        clear_button.pack(padx=10)

        # Translate button (Bot)
        translate_button = tk.Button(
            self,
            text="Translate",
            command=self.translate,
            bg="#4caf50",
            fg="white",
            font=("Arial", 12),
        )
        translate_button.pack(padx=10)

        # Admin panel button (BOT Bot)
        admin_button = tk.Button(
            self,
            text="Open Admin Panel",
            command=self.open_admin,
            bg="#455a64",
            fg="white",
            font=("Arial", 12)
        )
        admin_button.pack(pady=10)

        # Result (Bot Bot Bot)
        self.result_label = tk.Label(
            self,
            text="",
            font=("Arial", 14),
            wraplength=450,  # wrap text inside 450px
            justify="left"
        )
        self.result_label.pack(padx=10)
        self.word_input.bind("<Return>", lambda e: self.translate())

    # ----------------- Logic -----------------
    def resize_to_fit_text(self):
        self.update_idletasks()
        # get requested size after wrapping text
        new_height = self.winfo_reqheight()
        current_height = self.winfo_height()
        # Only grow window, never shrink automatically
        if new_height > current_height:
            self.geometry(f"800x{new_height}")

    def translate(self):
        word = self.word_input.get("1.0", tk.END).strip()
        if not word:
            messagebox.showwarning("Input Error", "Please enter a word.")
            return

        lang_name = self.lang_var.get()
        lang_code = None
        for n, code in LANG_OPTIONS:
            if n == lang_name:
                lang_code = code
                break

        if not lang_code:
            messagebox.showerror("Error", "Unsupported language")
            return

        # Try local DB first
        translated, used_online = sql_translate(word, lang_code)
        if translated:
            self.result_label.config(text=f"{word} → {translated} ({lang_name})")
            self.resize_to_fit_text()
            save_history(word, translated, lang_name, used_online=False)
            return

        # Online fallback
        if self.use_online_var.get():
            if not DEEP_TRANSLATOR_AVAILABLE:
                messagebox.showerror(
                    "Dependency Missing",
                    "Install: pip install deep-translator"
                )
                return

            threading.Thread(
                target=self._online_translate_thread,
                args=(word, lang_code, lang_name),
                daemon=True
            ).start()
            self.result_label.config(text="Translating online...")
        else:
            messagebox.showinfo(
                "Not Found",
                "Word not found locally. Enable online mode."
            )

    def _online_translate_thread(self, word, lang_code, lang_name):
        trans = online_translate(word, lang_code)
        if trans:
            save_history(word, trans, lang_name, used_online=True)
            self.after(0, lambda: self.result_label.config(
                text=f"{word} → {trans} ({lang_name})"
            ))
            self.after(0, self.resize_to_fit_text)
        else:
            self.after(0, lambda: messagebox.showerror(
                "Online Error", "Online translation failed."
            ))

    def clear(self):
        self.word_input.delete("1.0", tk.END)
        self.result_label.config(text="")

    def open_admin(self):
        AdminPanel(self)
