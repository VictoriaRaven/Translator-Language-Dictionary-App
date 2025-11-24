# Translator-Language-Dictionary-App
## Copyright Usage and License

Regarding Copyright laws by GitHub it states that a public repository without a license means that if you want to use my code you must fork my repository as I retain all proprietary rights.

Links:  
- [GitHub Copyright and Licenses](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)

## Information

This Project is a Basic Python GUI application of a Translator-Language-Dictionary-App. This uses the import of Tkinter (GUI: Graphical User Interface) library for Python and the Python Dictionary method through the (language).txt files uploaded. The user can input the english word or vice versa (incuding accents) and then it will translate the language and search for the word based on the user input and laws. I will gradually update this throughout my studies at UMGC.

### Languages Support (Main Language: English)
- French
- Spanish
- Portuguese
- Italian
- German
- Netherlands(Dutch)
- Polish
- Ukrainian
- Russian



## CS50 Concepts Integrated

To connect this project to CS50 foundational computer science concepts, the following topics are utilized or paralleled in the design:

### **Algorithms**

* Searching through dictionary text files parallels linear search.
* Potential optimization could mimic binary search.

### **Data Structures**

* Python dictionaries replicate CS50's hash table concepts.
* Text file dictionaries act as key-value lookup tables.

### **Memory (C Concepts Applied Conceptually)**

* Input validation parallels buffer-handling and bounds-checking discipline from C.
* Separation of UI, database, and translation logic reflects memory segmentation thinking.

### **File I/O**

* Text dictionary file reading mirrors C's `fopen`, `fgets`, etc.
* CSV export resembles structured data handling.

### **APIs and Abstraction**

* Online translation via `GoogleTranslator` demonstrates API usage similar to CS50’s exploration of libraries.
* Functions are modular and follow abstraction principles.

### **Databases (SQL)**

* This app uses SQLite for logging translations.
* Connects to CS50’s `SQL` problem sets regarding CRUD operations.

### **Threading / Concurrency**

* Background translation threads parallel CS50 discussions on performance and parallelization.

### **Event-Driven Programming**

* Tkinter GUI widgets act similar to CS50’s introduction to event-driven models.

### **Error Handling**

* Try/except blocks mirror defensive programming emphasized in C.



## Getting Started — Project-Specific Answers

Below are the CS50 “Getting Started” questions answered specifically for this Translator‑Language‑Dictionary‑App based on your existing code and README.

**• What will your software do? What features will it have? How will it be executed?**
This project is a standalone Python desktop application built with **Tkinter**, **SQLite**, and multiple language dictionary text files. It allows users to translate words between English and several supported languages, search dictionary entries, view translation history, export/import SQL data, paginate results, and optionally use an online translation API via Deep Translator. It runs locally on the user’s computer without requiring a server.

**• What new skills will you need to acquire? What topics will you need to research?**
Skills include GUI development with Tkinter, structuring larger Python applications, SQLite relational database design, text‑file parsing, exception handling, pagination algorithms, and integrating external Python modules for translation. Additional research involved CS50 documentation standards, Markdown formatting, and application architecture.

**• If working with classmates, who will do what?**
This project is a **solo project**, so all programming, design decisions, UI layout, database construction, translation logic, documentation, and testing were completed by me.

**• What is a good outcome, better outcome, and best outcome?**

* **Good outcome:** GUI that loads dictionary files, performs basic translations, and shows results.
* **Better outcome:** SQLite history database, improved navigation, input validation, CSV/SQL export, multi‑language support.
* **Best outcome:** Online translation fallback (Deep Translator), full import/export workflows, pagination, refined UI design, extended language support, robust error handling, and polished documentation suitable for CS50’s final project expectations.

**• Goal milestones to stay on track:**

1. Set up Tkinter interface and layout.
2. Load dictionary text files and build the translation logic.
3. Implement SQLite database for history storage.
4. Add search tools, pagination, import/export features.
5. Integrate optional online translation functionality.
6. Finalize documentation and produce the project demonstration video.

### Contact

Feel free to pm me (VictoriaRaven) if you want to use my code under a specific license and without needing to fork my repository.

## Contributing

Please read [CONTRIBUTING.md](README.md) for details on our code
of conduct, and the process for submitting pull requests to me.

## Authors

  - **Victoria Lee** - *provided by the README* -
    [VictoriaRaven](https://github.com/VictoriaRaven)

See also the list of
[contributors](https://github.com/VictoriaRaven/Legal-Studies-IRAC-Python-Generator/main/README.md)
who participated in this project.

## Acknowledgments

- [Google Scholar](https://scholar.google.com/)
- [Python Doc](https://docs.python.org/3/)
- [Wikipedia](https://www.wikipedia.org/)
- [UMGC Library](https://libguides.umgc.edu/home)
- [UMGC CS Resources](https://libguides.umgc.edu/c.php?g=316603&p=2114865)
- Bradley N. Miller, David L. Ranum, and Julie Anderson, *Python Programming in Context*, 3rd ed., Jones & Bartlett Learning, Oct. 2019. [Online Textbook Available](https://www.oreilly.com/library/view/python-programming-in/9781284175578/.)
 - Thank you!
 - VictoriaRaven