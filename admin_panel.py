import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
from datetime import datetime
from database import *
from exports import *
from emailer import *
from settings import PAGE_SIZE, DEEP_TRANSLATOR_AVAILABLE, TXT_FILES


# ----------------- GUI APP -----------------
class AdminPanel(tk.Toplevel):
    """
    Admin panel with tabs: Dictionary, History, Settings
    Includes editing, pagination, sorting, import CSV, export CSV
    """
    def __init__(self, master):
        super().__init__(master)
        self.title("Admin Panel")
        self.geometry("1000x600")
        self.transient(master)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=6, pady=6)
        # Dictionary tab
        self.dict_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.dict_frame, text="Dictionary")
        # History tab
        self.hist_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.hist_frame, text="History")
        # Settings tab
        self.set_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.set_frame, text="Settings")
        # Shared state for sorting and pagination
        self.dict_order_by = "id DESC"
        self.hist_order_by = "id DESC"
        self.dict_page = 0
        self.hist_page = 0
        self.dict_page_size = PAGE_SIZE
        self.hist_page_size = PAGE_SIZE
        self.dict_filter = ""
        self.hist_filter = ""
        self._build_dictionary_tab()
        self._build_history_tab()
        self._build_settings_tab()

    # ---------------- Dictionary Tab ----------------
    def _build_dictionary_tab(self):
        top = ttk.Frame(self.dict_frame)
        top.pack(fill="x", padx=8, pady=6)
        ttk.Label(top, text="Search:").pack(side="left")
        self.dict_search_entry = ttk.Entry(top, width=40)
        self.dict_search_entry.pack(side="left", padx=6)
        ttk.Button(top, text="Search", command=self.dict_search).pack(side="left", padx=4)
        ttk.Button(top, text="Clear", command=self.dict_clear_search).pack(side="left", padx=4)
        ttk.Button(top, text="Import CSV", command=self.import_dictionary_csv).pack(side="right", padx=4)
        ttk.Button(top, text="Export CSV", command=self.export_dictionary_csv).pack(side="right", padx=4)
        cols = ("id", "word", "translation", "language")
        self.dict_tree = ttk.Treeview(self.dict_frame, columns=cols, show="headings", height=18)
        for col in cols:
            self.dict_tree.heading(col, text=col.capitalize(), command=lambda c=col: self.sort_dictionary(c))
            self.dict_tree.column(col, width=200 if col!='id' else 60, anchor="w")
        self.dict_tree.pack(fill="both", expand=True, padx=8, pady=6)
        self.dict_tree.bind("<Double-1>", self.on_dict_double_click)
        # Page(s)
        pag_frame = ttk.Frame(self.dict_frame)
        pag_frame.pack(fill="x", padx=8, pady=4)
        self.dict_status_label = ttk.Label(pag_frame, text="Dictionary: 0 items")
        self.dict_status_label.pack(side="left")
        ttk.Button(pag_frame, text="Prev", command=self.dict_prev_page).pack(side="right", padx=4)
        ttk.Button(pag_frame, text="Next", command=self.dict_next_page).pack(side="right", padx=4)
        ttk.Label(pag_frame, text="Page size:").pack(side="right", padx=(10,2))
        self.dict_page_size_var = tk.IntVar(value=self.dict_page_size)
        ttk.Combobox(pag_frame, textvariable=self.dict_page_size_var, values=[10,20,50,100], width=5).pack(side="right")
        # refresh
        ttk.Button(pag_frame, text="Refresh", command=self.load_dictionary_page).pack(side="right", padx=6)
        self.load_dictionary_page()

    def dict_search(self):
        self.dict_filter = self.dict_search_entry.get().strip()
        self.dict_page = 0
        try:
            self.dict_page_size = int(self.dict_page_size_var.get())
        except:
            self.dict_page_size = PAGE_SIZE
        self.load_dictionary_page()

    def dict_clear_search(self):
        self.dict_search_entry.delete(0, tk.END)
        self.dict_filter = ""
        self.dict_page = 0
        self.load_dictionary_page()

    def dict_next_page(self):
        self.dict_page += 1
        self.load_dictionary_page()

    def dict_prev_page(self):
        if self.dict_page > 0:
            self.dict_page -= 1
        self.load_dictionary_page()

    def sort_dictionary(self, column):
        # Toggle asc/desc
        col_map = {"id":"id", "word":"word", "translation":"translation", "language":"language"}
        col = col_map.get(column, "id")
        if self.dict_order_by.lower().startswith(col + " asc"):
            self.dict_order_by = f"{col} DESC"
        else:
            self.dict_order_by = f"{col} ASC"
        self.load_dictionary_page()

    def load_dictionary_page(self):
        # compute offset
        try:
            self.dict_page_size = int(self.dict_page_size_var.get())
        except:
            self.dict_page_size = PAGE_SIZE
        offset = self.dict_page * self.dict_page_size
        rows, total = query_dictionary(filter_text=self.dict_filter, order_by=self.dict_order_by, limit=self.dict_page_size, offset=offset)
        # update tree
        for r in self.dict_tree.get_children():
            self.dict_tree.delete(r)
        for row in rows:
            self.dict_tree.insert("", "end", values=row)
        # update status
        start = offset + 1 if total>0 else 0
        end = min(offset + self.dict_page_size, total)
        self.dict_status_label.config(text=f"Dictionary: showing {start}-{end} of {total} (page {self.dict_page+1})")

    def on_dict_double_click(self, event):
        item = self.dict_tree.selection()
        if not item:
            return
        item = item[0]
        vals = self.dict_tree.item(item, "values")
        row_id, word, translation, language = vals
        # open edit dialog
        EditDialog(self, row_id, word, translation, language, table="dictionary", refresh_callback=self.load_dictionary_page)

    def import_dictionary_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files","*.csv"),("All files","*.*")])
        if not path:
            return
        count = 0
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if not set(["word","translation","language"]).issubset(reader.fieldnames):
                messagebox.showerror("CSV Error", "CSV must have headers: word, translation, language")
                return
            for r in reader:
                w = r.get("word","").strip()
                t = r.get("translation","").strip()
                lang = r.get("language","").strip()
                if w and t and lang:
                    insert_dictionary_row(w, t, lang)
                    count += 1
        messagebox.showinfo("Import Complete", f"Imported {count} rows into dictionary.")
        self.load_dictionary_page()

    def export_dictionary_csv(self):
        # Export current filtered results (all pages)
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if not path:
            return
        rows, total = query_dictionary(filter_text=self.dict_filter, order_by=self.dict_order_by, limit=None, offset=None)
        with open(path, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id","word","translation","language"])
            writer.writerows(rows)
        messagebox.showinfo("Exported", f"Exported {len(rows)} rows to {path}")

    # ---------------- History Tab ----------------
    def _build_history_tab(self):
        top = ttk.Frame(self.hist_frame)
        top.pack(fill="x", padx=8, pady=6)
        ttk.Label(top, text="Search:").pack(side="left")
        self.hist_search_entry = ttk.Entry(top, width=40)
        self.hist_search_entry.pack(side="left", padx=6)
        ttk.Button(top, text="Search", command=self.hist_search).pack(side="left", padx=4)
        ttk.Button(top, text="Clear", command=self.hist_clear_search).pack(side="left", padx=4)
        ttk.Button(top, text="Export CSV", command=self.export_history_csv).pack(side="right", padx=4)
        ttk.Button(top, text="Export JSON", command=self.export_history_json).pack(side="right", padx=4)
        ttk.Button(top, text="Export PDF", command=self.export_history_pdf).pack(side="right", padx=4)
        ttk.Button(top, text="Email History", command=self.email_history_dialog).pack(side="right", padx=4)
        cols = ("id", "input_word", "output_word", "language", "used_online", "timestamp")
        self.hist_tree = ttk.Treeview(self.hist_frame, columns=cols, show="headings", height=18)
        for col in cols:
            self.hist_tree.heading(col, text=col.capitalize(), command=lambda c=col: self.sort_history(c))
            self.hist_tree.column(col, width=140 if col!='id' else 60, anchor="w")
        self.hist_tree.pack(fill="both", expand=True, padx=8, pady=6)
        # Bind double-click to edit (for input_word/output_word/language)
        self.hist_tree.bind("<Double-1>", self.on_hist_double_click)
        # Pagination controls
        pag_frame = ttk.Frame(self.hist_frame)
        pag_frame.pack(fill="x", padx=8, pady=4)
        self.hist_status_label = ttk.Label(pag_frame, text="History: 0 items")
        self.hist_status_label.pack(side="left")
        ttk.Button(pag_frame, text="Prev", command=self.hist_prev_page).pack(side="right", padx=4)
        ttk.Button(pag_frame, text="Next", command=self.hist_next_page).pack(side="right", padx=4)
        ttk.Label(pag_frame, text="Page size:").pack(side="right", padx=(10,2))
        self.hist_page_size_var = tk.IntVar(value=self.hist_page_size)
        ttk.Combobox(pag_frame, textvariable=self.hist_page_size_var, values=[10,20,50,100], width=5).pack(side="right")
        ttk.Button(pag_frame, text="Delete Selected", command=self.delete_hist_selected).pack(side="right", padx=6)
        ttk.Button(pag_frame, text="Delete ALL", command=self.delete_hist_all).pack(side="right", padx=6)
        ttk.Button(pag_frame, text="Refresh", command=self.load_history_page).pack(side="right", padx=6)
        self.load_history_page()

    def hist_search(self):
        self.hist_filter = self.hist_search_entry.get().strip()
        self.hist_page = 0
        try:
            self.hist_page_size = int(self.hist_page_size_var.get())
        except:
            self.hist_page_size = PAGE_SIZE
        self.load_history_page()

    def hist_clear_search(self):
        self.hist_search_entry.delete(0, tk.END)
        self.hist_filter = ""
        self.hist_page = 0
        self.load_history_page()

    def hist_next_page(self):
        self.hist_page += 1
        self.load_history_page()

    def hist_prev_page(self):
        if self.hist_page > 0:
            self.hist_page -= 1
        self.load_history_page()

    def sort_history(self, column):
        col_map = {"id":"id", "input_word":"input_word", "output_word":"output_word", "language":"language", "used_online":"used_online", "timestamp":"timestamp"}
        col = col_map.get(column, "id")
        if self.hist_order_by.lower().startswith(col + " asc"):
            self.hist_order_by = f"{col} DESC"
        else:
            self.hist_order_by = f"{col} ASC"
        self.load_history_page()

    def load_history_page(self):
        try:
            self.hist_page_size = int(self.hist_page_size_var.get())
        except:
            self.hist_page_size = PAGE_SIZE
        offset = self.hist_page * self.hist_page_size
        rows, total = query_history(filter_text=self.hist_filter, order_by=self.hist_order_by, limit=self.hist_page_size, offset=offset)
        for r in self.hist_tree.get_children():
            self.hist_tree.delete(r)
        for row in rows:
            # format used_online column nicely
            row_list = list(row)
            row_list[4] = "ONLINE" if row_list[4] else "LOCAL"
            self.hist_tree.insert("", "end", values=row_list)
        start = offset + 1 if total>0 else 0
        end = min(offset + self.hist_page_size, total)
        self.hist_status_label.config(text=f"History: showing {start}-{end} of {total} (page {self.hist_page+1})")

    def on_hist_double_click(self, event):
        item = self.hist_tree.selection()
        if not item:
            return
        item = item[0]
        vals = self.hist_tree.item(item, "values")
        row_id, inp, outp, lang, used_online, ts = vals
        # open edit dialog
        EditDialog(self, row_id, inp, outp, lang, table="history", refresh_callback=self.load_history_page)

    def delete_hist_selected(self):
        selected = self.hist_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "No entry selected.")
            return
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        for item in selected:
            entry_id = self.hist_tree.item(item)["values"][0]
            c.execute("DELETE FROM history WHERE id=?", (entry_id,))
            self.hist_tree.delete(item)
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "Selected history entries deleted.")
        self.load_history_page()

    def delete_hist_all(self):
        if not messagebox.askyesno("Confirm", "Delete ALL history?"):
            return
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM history")
        conn.commit()
        conn.close()
        messagebox.showinfo("Deleted", "All history deleted.")
        self.load_history_page()

    def export_history_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if not path:
            return
        rows, total = query_history(filter_text=self.hist_filter, order_by=self.hist_order_by, limit=None, offset=None)
        with open(path, "w", newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(["id","input_word","output_word","language","used_online","timestamp"])
            writer.writerows(rows)
        messagebox.showinfo("Exported", f"Exported {len(rows)} rows to {path}")

    # ---------------- Exports (JSON / PDF / Email) ----------------
    def export_history_json(self):
        """Export history to JSON (export_history_json utility.)"""
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON","*.json")])
        if not path:
            return
        rows, total = query_history(filter_text=self.hist_filter, order_by=self.hist_order_by, limit=None, offset=None)
        ok, err = export_history_json(path, rows)
        if ok:
            messagebox.showinfo("Exported", f"Exported {len(rows)} rows to {path}")
        else:
            messagebox.showerror("Export Error", f"Failed to export JSON: {err}")

    def export_history_pdf(self):
        """Export history to PDF (reportlab if available; otherwise txt)."""
        path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF","*.pdf"),("Text","*.txt")])
        if not path:
            return
        rows, total = query_history(filter_text=self.hist_filter, order_by=self.hist_order_by, limit=None, offset=None)
        ok, msg = export_history_pdf(path, rows, title="Translation History")
        if ok:
            messagebox.showinfo("Exported", f"Exported {len(rows)} rows to {path}")
        else:
            # msg may communicate fallback or error text
            messagebox.showwarning("Export Warning", f"PDF export returned: {msg}")

    def email_history_dialog(self):
        """
        Prompt for recipient and then email the exported history
        """
        # ask for recipient
        to_addr = simpledialog.askstring("Email History", "Send history to (email):")
        if not to_addr:
            return
        # create temp JSON file with current filter
        rows, total = query_history(filter_text=self.hist_filter, order_by=self.hist_order_by, limit=None, offset=None)
        tmp_path = os.path.join(os.getcwd(), "temp_history.json")
        ok, err = export_history_json(tmp_path, rows)
        if not ok:
            messagebox.showerror("Export Error", f"Failed to write temp attachment: {err}")
            return
        # get SMTP settings
        smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.environ.get("SMTP_PORT", os.environ.get("SMTP_PORT", 587)))
        from_env = "EMAIL_FROM"  # environment var name for from address (used by send_history_email)
        subject = f"Translation History export from {os.environ.get('HOSTNAME', 'TranslatorApp')}"
        body = f"Attached is the translation history exported at {datetime.now().isoformat()}."
        ok, err = send_history_email(to_addr=to_addr,subject=subject,body=body, attachment_path=tmp_path)
        try:
            os.remove(tmp_path)
        except Exception:
            pass
        if ok:
            messagebox.showinfo("Email Sent", f"NOTE: Attach Files to Email Address: {to_addr}")
        else:
            messagebox.showerror("Email Error", f"Failed to send email: {err}")

    # ---------------- Settings Tab ----------------
    def _build_settings_tab(self):
        frm = ttk.Frame(self.set_frame)
        frm.pack(fill="both", expand=True, padx=8, pady=8)
        ttk.Label(frm, text="Load .txt dictionaries into DB").pack(anchor="w", pady=(0,6))
        ttk.Button(frm, text="Load .txt files (match English file and language files)", command=self.load_txt_files).pack(anchor="w", pady=4)
        ttk.Separator(frm).pack(fill="x", pady=8)
        ttk.Label(frm, text="Online Translator").pack(anchor="w", pady=(0,6))
        self.online_var = tk.IntVar(value=1 if DEEP_TRANSLATOR_AVAILABLE else 0)
        ttk.Checkbutton(frm, text=f"Enable online translator (deep-translator) — available: {DEEP_TRANSLATOR_AVAILABLE}", variable=self.online_var).pack(anchor="w", pady=2)
        ttk.Label(frm, text="CSV import/export expectations: CSV headers 'word,translation,language'").pack(anchor="w", pady=6)

    def load_txt_files(self):
        # Requires eng_dictionary.txt + other language txts
        base_path = os.getcwd()
        # check english file
        en_file = TXT_FILES.get("en")
        if not os.path.isfile(en_file):
            messagebox.showerror("Missing file", f"English file '{en_file}' not found in folder: {base_path}")
            return
        # read english words
        with open(en_file, encoding='utf-8') as f:
            eng_words = [line.strip() for line in f if line.strip()]
        inserted = 0
        # for each language other than en
        for lang, fname in TXT_FILES.items():
            if lang == "en":
                continue
            if not os.path.isfile(fname):
                print(f"Skipping {lang}: file {fname} missing.")
                continue
            with open(fname, encoding='utf-8') as f:
                other_words = [line.strip() for line in f if line.strip()]
            # zip and insert rows
            for eng, oth in zip(eng_words, other_words):
                if eng and oth:
                    insert_dictionary_row(eng.lower(), oth.lower(), lang)
                    inserted += 1
        messagebox.showinfo("Done", f"Loaded {inserted} word pairs into dictionary (from available .txt files).")
        # refresh dictionary tab if open
        self.load_dictionary_page()

# ------------------ Edit Dialog ------------------
class EditDialog(tk.Toplevel):
    """
    For Editing a row in dictionary or history.
    For dictionary: fields = word, translation, language
    For history: fields = input_word, output_word, language (and can save back to history)
    """
    def __init__(self, master, row_id, field1, field2, field3, table="dictionary", refresh_callback=None):
        super().__init__(master)
        self.title("Edit Entry")
        self.row_id = row_id
        self.table = table
        self.refresh_callback = refresh_callback
        self.geometry("420x220")
        self.transient(master)
        # labels depend on table
        if table == "dictionary":
            lbl1, lbl2, lbl3 = "Word", "Translation", "Language"
            val1, val2, val3 = field1, field2, field3
        else:
            lbl1, lbl2, lbl3 = "Input Word", "Output Word", "Language"
            val1, val2, val3 = field1, field2, field3
        ttk.Label(self, text=lbl1).pack(anchor="w", padx=8, pady=(10,2))
        self.e1 = ttk.Entry(self)
        self.e1.pack(fill="x", padx=8)
        self.e1.insert(0, val1)
        ttk.Label(self, text=lbl2).pack(anchor="w", padx=8, pady=(10,2))
        self.e2 = ttk.Entry(self)
        self.e2.pack(fill="x", padx=8)
        self.e2.insert(0, val2)
        ttk.Label(self, text=lbl3).pack(anchor="w", padx=8, pady=(10,2))
        self.e3 = ttk.Entry(self)
        self.e3.pack(fill="x", padx=8)
        self.e3.insert(0, val3)
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill="x", pady=12, padx=8)
        ttk.Button(btn_frame, text="Save", command=self.save).pack(side="right", padx=6)
        ttk.Button(btn_frame, text="Cancel", command=self.destroy).pack(side="right")
        if table == "dictionary":
            ttk.Button(btn_frame, text="Delete", command=self.delete_row).pack(side="left", padx=6)
        else:
            ttk.Button(btn_frame, text="Delete", command=self.delete_history_row).pack(side="left", padx=6)

    def save(self):
        new1 = self.e1.get().strip()
        new2 = self.e2.get().strip()
        new3 = self.e3.get().strip()
        if not (new1 and new2 and new3):
            messagebox.showwarning("Validation", "All fields required.")
            return
        if self.table == "dictionary":
            update_dictionary_row(self.row_id, new1, new2, new3)
        else:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()
            c.execute("UPDATE history SET input_word=?, output_word=?, language=? WHERE id=?", (new1.lower(), new2.lower(), new3, self.row_id))
            conn.commit()
            conn.close()
        if self.refresh_callback:
            self.refresh_callback()
        self.destroy()

    def delete_row(self):
        if not messagebox.askyesno("Confirm Delete", "Delete this dictionary row?"):
            return
        delete_dictionary_row(self.row_id)
        if self.refresh_callback:
            self.refresh_callback()
        self.destroy()

    def delete_history_row(self):
        if not messagebox.askyesno("Confirm Delete", "Delete this history entry?"):
            return
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("DELETE FROM history WHERE id=?", (self.row_id,))
        conn.commit()
        conn.close()
        if self.refresh_callback:
            self.refresh_callback()
        self.destroy()
