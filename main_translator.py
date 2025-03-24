import tkinter as tk
from tkinter import messagebox

# Dictionaries to store translations
english_to_french = {}  # fr
french_to_english = {}
english_to_russian = {}  # ru
russian_to_english = {}
english_to_ukrainian = {}  # ukr
ukrainian_to_english = {}
english_to_spanish = {}  # sp
spanish_to_english = {}
english_to_portuguese = {}  # por
portuguese_to_english = {}
english_to_italian = {}  # ita
italian_to_english = {}
english_to_german = {}  # gr
german_to_english = {}
english_to_netherlands = {}  # dth
netherlands_to_english = {}
english_to_polish = {}  # poh
polish_to_english = {}

# Function to load translation data from the files
def load_translation_data():
    try:
        # Read the English words with UTF-8 encoding
        with open("eng_dictionary.txt", "r", encoding="utf-8") as file:
            english_words = [line.strip() for line in file.readlines()]

        # Read the French words with UTF-8 encoding
        with open("fr_dictionary.txt", "r", encoding="utf-8") as file:
            french_words = [line.strip() for line in file.readlines()]

        # Read the Russian words with UTF-8 encoding
        with open("ru_dictionary.txt", "r", encoding="utf-8") as file:
            russian_words = [line.strip() for line in file.readlines()]

        # Read the Ukrainian words with UTF-8 encoding
        with open("ukr_dictionary.txt", "r", encoding="utf-8") as file:
            ukrainian_words = [line.strip() for line in file.readlines()]

        # Read the Spanish words with UTF-8 encoding
        with open("sp_dictionary.txt", "r", encoding="utf-8") as file:
            spanish_words = [line.strip() for line in file.readlines()]

        # Read the Portuguese words with UTF-8 encoding
        with open("por_dictionary.txt", "r", encoding="utf-8") as file:
            portuguese_words = [line.strip() for line in file.readlines()]

        # Read the Italian words with UTF-8 encoding
        with open("ita_dictionary.txt", "r", encoding="utf-8") as file:
            italian_words = [line.strip() for line in file.readlines()]

        # Read the Dutch German words with UTF-8 encoding
        with open("gr_dictionary.txt", "r", encoding="utf-8") as file:
            german_words = [line.strip() for line in file.readlines()]

        # Read the Dutch Netherland words with UTF-8 encoding
        with open("nth_dictionary.txt", "r", encoding="utf-8") as file:
            netherlands_words = [line.strip() for line in file.readlines()]

        # Read the Polish words with UTF-8 encoding
        with open("poh_dictionary.txt", "r", encoding="utf-8") as file:
            polish_words = [line.strip() for line in file.readlines()]

        # Ensure both files have the same number of words
        if len(english_words) != len(french_words) != len(russian_words) != len(ukrainian_words) != len(spanish_words) != len(portuguese_words) != len(italian_words) != len(german_words) != len(netherlands_words) != len(polish_words):
            print("Warning: The number of words in the Language files do not match!")

        # Create multidirectional dictionaries
        for eng_word, fr_word, ru_word, ukr_word, sp_word, por_word, ita_word, gr_word, nth_word, poh_word in zip(english_words, french_words, russian_words, ukrainian_words, spanish_words, portuguese_words, italian_words, german_words, netherlands_words, polish_words):
            english_to_french[eng_word.lower()] = fr_word.lower()  # fr
            french_to_english[fr_word.lower()] = eng_word.lower()
            english_to_russian[eng_word.lower()] = ru_word.lower()  # ru
            russian_to_english[ru_word.lower()] = eng_word.lower()
            english_to_ukrainian[eng_word.lower()] = ukr_word.lower()  # ukr
            ukrainian_to_english[ukr_word.lower()] = eng_word.lower()
            english_to_spanish[eng_word.lower()] = sp_word.lower()  # sp
            spanish_to_english[eng_word.lower()] = eng_word.lower()
            english_to_portuguese[eng_word.lower()] = por_word.lower()  # por
            portuguese_to_english[eng_word.lower()] = eng_word.lower()
            english_to_italian[eng_word.lower()] = ita_word.lower()  # ita
            italian_to_english[eng_word.lower()] = eng_word.lower()
            english_to_german[eng_word.lower()] = gr_word.lower()  # gr
            german_to_english[eng_word.lower()] = eng_word.lower()
            english_to_netherlands[eng_word.lower()] = nth_word.lower()  # nth
            netherlands_to_english[eng_word.lower()] = eng_word.lower()
            english_to_polish[eng_word.lower()] = poh_word.lower()  # poh
            polish_to_english[eng_word.lower()] = eng_word.lower()

    except FileNotFoundError:
        print("Translation files not found! Please ensure all dictionary files exist.")
    except Exception as e:
        print(f"Error loading translations: {e}")


# Function to translate between English and selected language
def translate():
    input_word = word_input.get().strip().lower()

    if not input_word:
        messagebox.showwarning("Input Error", "Please enter a word to translate.")
        return

    selected_language = language_selector.get()

    # Mapping for each selected language
    translations = {
        "French": (english_to_french, french_to_english),
        "Russian": (english_to_russian, russian_to_english),
        "Ukrainian": (english_to_ukrainian, ukrainian_to_english),
        "Spanish": (english_to_spanish, spanish_to_english),
        "Portuguese": (english_to_portuguese, portuguese_to_english),
        "Italian": (english_to_italian, italian_to_english),
        "German": (english_to_german, german_to_english),
        "Dutch(Netherlands)": (english_to_netherlands, netherlands_to_english),
        "Polish": (english_to_polish, polish_to_english),
    }

    if selected_language not in translations:
        messagebox.showerror("Translation Error", "Unsupported language selected.")
        return

    lang_dict, reverse_dict = translations[selected_language]

    if input_word in lang_dict:
        translated_word = lang_dict[input_word]
        result_label.config(text=f"{input_word} (English) -> {translated_word} ({selected_language})")
    elif input_word in reverse_dict:
        translated_word = reverse_dict[input_word]
        result_label.config(text=f"{input_word} ({selected_language}) -> {translated_word} (English)")
    else:
        messagebox.showerror("Translation Error", "Word not found in dictionary.")


# Function to search for a word in the dictionary and show translation
def search_word():
    search_word = search_input.get().strip().lower()

    if not search_word:
        messagebox.showwarning("Search Error", "Please enter a word to search.")
        return

    selected_language = language_selector.get()

    # Mapping for each selected language
    translations = {
        "French": (english_to_french, french_to_english),
        "Russian": (english_to_russian, russian_to_english),
        "Ukrainian": (english_to_ukrainian, ukrainian_to_english),
        "Spanish": (english_to_spanish, spanish_to_english),
        "Portuguese": (english_to_portuguese, portuguese_to_english),
        "Italian": (english_to_italian, italian_to_english),
        "German": (english_to_german, german_to_english),
        "Dutch(Netherlands)": (english_to_netherlands, netherlands_to_english),
        "Polish": (english_to_polish, polish_to_english),
    }

    if selected_language not in translations:
        messagebox.showerror("Search Error", "Unsupported language selected.")
        return

    lang_dict, reverse_dict = translations[selected_language]

    if search_word in lang_dict:
        translated_word = lang_dict[search_word]
        messagebox.showinfo("Translation", f"{search_word} (English) -> {translated_word} ({selected_language})")
    elif search_word in reverse_dict:
        translated_word = reverse_dict[search_word]
        messagebox.showinfo("Translation", f"{search_word} ({selected_language}) -> {translated_word} (English)")
    else:
        messagebox.showerror("Search Error", "Word not found in dictionary.")


# Function to clear input fields
def clear_inputs():
    word_input.delete(0, tk.END)
    search_input.delete(0, tk.END)
    result_label.config(text="")


# Create the main window
root = tk.Tk()
root.title("Multilingual Translator")

# Input field for word to translate
tk.Label(root, text="Enter a word to translate:").pack(pady=5)
word_input = tk.Entry(root, width=50)
word_input.pack(pady=5)

# Dropdown to select target language
tk.Label(root, text="Select a language:").pack(pady=5)
language_selector = tk.StringVar(value="French")  # Default selection is French
language_options = ["French", "Russian", "Ukrainian", "Spanish", "Portuguese", "Italian", "German", "Dutch(Netherlands)", "Polish"]
language_menu = tk.OptionMenu(root, language_selector, *language_options)
language_menu.pack(pady=5)

# Button to translate the word
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=10)

# Label to display translation result
result_label = tk.Label(root, text="", height=2)
result_label.pack()

# Input field for searching a word in the dictionary
tk.Label(root, text="Search for a word:").pack(pady=5)
search_input = tk.Entry(root, width=50)
search_input.pack(pady=5)

# Button to search for the word and show translation
search_button = tk.Button(root, text="Search", command=search_word)
search_button.pack(pady=10)

# Button to clear inputs
clear_button = tk.Button(root, text="Clear Inputs", command=clear_inputs)
clear_button.pack(pady=10)

# Load translation data from the files when the program starts
load_translation_data()

# Run the main loop
root.mainloop()
