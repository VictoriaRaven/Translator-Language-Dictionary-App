# Translator-Language-Dictionary-App
[![Static Badge](https://img.shields.io/badge/Documents-DocFiles-blue)](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/docs) [![Static Badge](https://img.shields.io/badge/Databases-dbTxts-blue)](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/data) [![Static Badge](https://img.shields.io/badge/Tests-AllTests-blue)](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/tests) [![Static Badge](https://img.shields.io/badge/History-TranslationMachines-purple)](https://en.wikipedia.org/wiki/History_of_machine_translation)

## Copyright Usage and License
Regarding Copyright laws by GitHub, it states that a public repository without a license means that others must fork the repository to utilize and modify the code as the team retains all proprietary rights.
Links:  
- [GitHub Copyright and Licenses](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)

## 🎥 CS50 Video
- [CS50 Final Project Video Demonstration](https://youtu.be/f7c4AC6BHUo)
- [VictoriaRaven/Translator-Language-Dictionary-App](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App)

## ⚠️ Important Notice

This Project is a Basic Python GUI application of a Translator-Language-Dictionary-App. This uses the import of Tkinter (GUI: Graphical User Interface) library for Python and the Python Dictionary method through the (language).txt files uploaded. The user can input the english word or vice versa (incuding accents) and then it will translate the language and search for the word based on the user input and laws. I will gradually update this throughout my studies at UMGC. Git will be used for version control, and testing will ensure each component meets requirements. Deliverables include an intuitive GUI, featuring gui translaster app components and, an interactive buttons to export the dicitonary or translation histories as well as wother unique features. The development will be tracked through version controll, SDLC methods (like a CS capstone) and tested using all types of testing including automated.

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

### Contact and Outside Contributing
- Feel free to reach out to me on GitHub if you want to use my code under a specific license, without needing to fork this repository, or want to be a part of the contribution team.

## Author / Team
  - Note: These roles are what the majority of the time each person is completing, but the team is willing to swap out roles to help out in other sections.
  - **Victoria Lee** - *Project Manager / Technical Writer / Developer/ Git Lead (.py files) / Tester (GitHub Actions / Repo / ALL TESTS(Unit; Manual Tests; System; Auto))*

## Table of Contents (Key Parts Only)
  * [**CS50 Video - Final**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#-cs50-video)
  * [**CS 50 Concepts Integrated**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#cs50-concepts-integrated)
  * [**CS50 Q and A - Project Requirements**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#-cs50-project-questions-answers)
  * [**How to Set Up the GUI**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#how-to-set-up-the-gui)
  * [**How to Navigate the GUI**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#how-to-navigate-the-translator-app-gui)
  * [**History of Translation Machines**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#history-of-translation-machines)
  * [**Introduction, Requirements, and Objectives**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#introduction-requirements-and-objectives)
    + [Automated Testing and Manual Testing Instructions](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#automated-testing-and-manual-testing-instructions)
    + [Overview of Progress and Conclusion](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#overview-of-progress-and-conclusion)
    + [User Guide](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#user-guide-before-deployment)
  * [**Acknowledgements**](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#acknowledgments)

## 🌐 Overview
A multi-language offline/online translator built with **Python**, **Tkinter**, **SQLite**, and modular architecture. This project is designed and documented according to **CS50’s 2025 final project expectations**. This desktop application allows users to translate words between English and several supported languages using:
  - Offline dictionary files (only with most common words people use often; 100)
  - An SQLite-powered dictionary  
  - Optional online translation (Free version Google API translator)  
  - History logging and export  
  - A Tkinter-based GUI  
  - Admin and data-management tools  
      - The project emphasizes clean architecture, modularity, abstraction, and error-resistant design, aligning with core CS50 principles.

## ✦ Features
#### ✦ Offline Dictionary Translation  
Loads local language dictionaries for immediate lookup.
#### ✦ Online Translation (Fallback Mode)  
Queries the MyMemory translation API when local data is insufficient.
#### ✦ Search, Sorting, and Pagination  
The dictionary and history pages allow fast navigation even with large datasets.
#### ✦ SQLite-Backed History Logging  
Every translation is logged with:
  - Input word  
  - Output word  
  - Language  
  - Local vs online source  
  - Timestamp  
#### Export Tools  
Supports:
  - **JSON export** (full history dump)  
  - **PDF export** using bundled DejaVu font (UTF-8 safe)
  - **Excel(.XLSX)** using UTF-8 safe written file in UTF format
     - **Note:** EXCEL has a *specific way* of opening the data! Go to the [Tutorial to Import UTF-8 EXCEL Data here](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/main/README.md#tutorial-to-import-utf-8-excel-data). 
#### Email Integration  
Can open Outlook to send history exports or use a `mailto:` fallback.
#### CS50-Friendly Modular Design  
- ✦ **Separated into modules:**
```bash

TranslatorApp (gui.py) → manages windows, tabs, events
│
├── admin_panel.py # features of dictionary history settings tab in gui
├── algorithms.py # Selection and Binary Search/Sort
├── database.py # SQLite handler
├── emailer.py # Email export helper
├── exports.py # JSON-PDF-EXCEL exporter
├── gui.py # Tkinter GUI (TranslatorApp class)
├── main.py # → launches the app (USER MUST RUN HERE)
├── requirements-dev.txt #pip for req pack/imports tests
├── requirements.txt # pip for req pack/imports
├── settings.py  # Config for API + email
├── spelling.py # Grammar and Spelling check translation
├── translation.py # Online translation logic
├── validation.py # validates inputs to not exceed boundaries
├── data/
│ ├── translations.db # SQLite database
│ └── ...all-dictionary...
├── DejaVuSans/ # font for utf-8 ru and ukr
│ └── ...DejaVuSans.ttf
├── docs/ # all the plans-reports-docs
│ └── ...file.pdf
│ └── ...file.docx
│ └── ...file.xlsx
├── tests/ # Pytest test suite
│ └──...all-test_.py...

```

## CS50 Concepts Integrated
To connect this project to CS50 foundational computer science concepts, the following topics are utilized or paralleled in the design mentioned below. The hub also integrates Git for version control to manage the development lifecycle. This project intentionally incorporates a wide range of CS50 foundational concepts. The following list explicitly maps your application’s design and features to CS50’s 2025 curriculum.
### Algorithms
  - Searching dictionary entries mirrors linear search.
  - Sorting and pagination apply selection and ordering techniques.
  - Selection sort - returns a new sorted list. O(n^2)
  - Binary search on a sorted list. Returns index or -1. O(log n)
  - Online/offline fallback mimics decision-based algorithm selection.
### Data Structures
  - Python dictionaries and lookups parallel CS50’s hash tables.
  - SQLite tables (rows, indices) reflect structured storage similar to C structs.
  - Tuples returned from DB queries mirror fixed-format records.
### Memory (C-Inspired Concepts Applied in Python)
  - Input validation is modeled after CS50’s emphasis on safe buffer handling.
  - Separation of:
      - GUI  
      - translation logic  
      - database logic  
      - exporter : which resembles stack/heap/code/data segment separation.
### File I/O
  - Dictionary text files are parsed similar to C’s `fopen`, `fgets`, and tokenizing.
  - JSON export demonstrates structured serialization.
  - PDF creation illustrates writing data into formatted output streams.
### APIs and Abstraction
  - MyMemory API usage parallels CS50’s introduction to HTTP and API requests.
  - Functions such as `translate_online()` encapsulate complexity via abstraction.
  - Modules interact through clear interface boundaries (CS50-style modularization).
### Databases (SQL)
  - Fully uses SQLite with:
      - `SELECT`, `INSERT`, `UPDATE`, `DELETE`
      - indices  
      - pagination via LIMIT/OFFSET  
  - Directly mirrors CS50 SQL problem sets.
### Threading / Concurrency
  - Optional background translation threads mirror CS50 performance discussions.
  - Preventing UI freeze reflects conceptual concurrency management.
### Event-Driven Programming
  - Tkinter relies on an event loop (`mainloop()`), paralleling CS50’s introduction to asynchronous UI design.
### Error Handling
  - Try/except blocks are Python’s version of CS50-style defensive programming.
  - Graceful fallbacks (offline mode → online mode → error message).

## ❓ CS50 Project Questions Answers
### What will your software do?  What features will it have? How will it be executed?
  - **1) This program is a standalone desktop translator application where it:**
     - Loads local dictionary files  
     - Uses SQLite for history  
     - Translates text between multiple languages  
  - **2) Features:**
     - Offers optional online translation  
     - Allows search, filtering, and pagination  
     - Exports results to PDF/JSON/Excel(.XLSX - UTF-8 format)
     - Sends emails with attachments
     - No server required
  - **3) It runs by executing:** `python main.py`
### What new skills will you need to acquire?
  - Tkinter GUI design  (python knowledge; including cs50 file open/reader lessons)
  - SQL table management and schema design  (cs50's sql intro)
  - Strong software architecture (SLDC: docs and tests folder for more details) 
  - Data structure and algorithms (Selection and Binary)
  - REST API requests  (Google Free / CS50)
  - Encoding issues (UTF-8 fonts, Russian/Ukrainian support)  
  - PDF generation with ReportLab  (python)
  - Error-handling strategies  (coding practices)
  - Markdown documentation (CS50-style)
### If working with classmates, who will do what?
  - This is a solo project.  
  - All design, programming, testing, documentation, and debugging were completed by me.
### What is a good outcome, better outcome, and best outcome?
#### Good Outcome
  - Basic GUI  
  - Load dictionary  
  - Perform translations  
#### Better Outcome
  - SQLite history  
  - Online translation mode  
  - Search + pagination  
  - Export functions  
#### Best Outcome (Achieved)
  - Offline + online translation pipeline  
  - PDF + JSON + Excel(.XLSX - UTF-8 format) + (maybe email) export with UTF-8 fonts  
  - Admin data tools  
  - Clean architecture with modular separation  
  - CS50-conformant documentation and diagrams  
### Goal Milestones to Stay on Track
1. Implement Tkinter GUI  
2. Load dictionary text files  
3. Add translation logic  
4. Connect SQLite database  
5. Implement history + pagination  
6. Add export and email tools  
7. Test all modules  
8. Write documentation + CS50 final video  
### Architecture Summary
```bash

TranslatorApp (gui.py) → manages windows, tabs, events
│
├── admin_panel.py # features of dictionary history settings tab in gui
├── algorithms.py # Selection and Binary Search/Sort
├── database.py # SQLite handler
├── emailer.py # Email export helper
├── exports.py # JSON-PDF-EXCEL exporter
├── gui.py # Tkinter GUI (TranslatorApp class)
├── main.py # → launches the app (USER MUST RUN HERE)
├── requirements-dev.txt #pip for req pack/imports tests
├── requirements.txt # pip for req pack/imports
├── settings.py  # Config for API + email
├── spelling.py # Grammar and Spelling check translation
├── translation.py # Online translation logic
├── validation.py # validates inputs to not exceed boundaries
├── data/
│ ├── translations.db # SQLite database
│ └── ...all-dictionary...
├── DejaVuSans/ # font for utf-8 ru and ukr
│ └── ...DejaVuSans.ttf
├── docs/ # all the plans-reports-docs
│ └── ...file.pdf
│ └── ...file.docx
│ └── ...file.xlsx
├── tests/ # Pytest test suite
│ └──...all-test_.py...

```

### Installation
```bash

pip install -r requirements.txt
pip install -r requirements-dev.txt
python main.py

```
  - Make sure DejaVuSans.ttf is placed in the DejaVuSans/ directory for PDF export!
  - 🎥 CS50 Video: A link will be added after recording the final demonstration, as required by CS50 over here...

### Final Notes
This project is designed to meet — and exceed — the expectations of the CS50 2025 Final Project, demonstrating:
- Modular design
- Real-world architecture
- Practical use of SQL
- File I/O
- API usage
- GUI design
- Documentation quality
- Testing Quality
- SDLC

## **How to Set Up the GUI**
### 0. Forking Repository
This option is **ONLY** if you have a Git Account and are comfortable using Git to run the application. This is also for users who would like to add contributions to our game as well as per the GitHub policies previously mentioned in the Copyright / License Section. **Skip to 1)** if you do not want to use this method.
- First, Login with your Git account
- Go to the repository page of this project
- Then click **Fork**
- Then select **Create a new fork**
- Make sure to copy only main
- Then Go to the step of *2) Options to Run Application* **part c**

### 1. Download the Zip / Clone Repository
To get started with the project, first go to the repository page of this project. Then CLICK in this order at the top right-hand green button:
```bash
<>Code -> Download Zip
OR
<>Code -> $ git clone https://github.com/VictoriaRaven/Translator-Language-Dictionary-App.git
```
This will allow you to download the Zip file or clone the repository successfully. If you have the Zip file extract it onto a Python IDE Directory folder of the new project, but you must have Python installed on your machine.
## **2. Options to Run Application**
- **a)** [Run through a Python IDE](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#a-a-set-up-pycharm-set-up-a-virtual-environment-install-dependencies-run-application)
- **b)** [Run through Python Terminal after setting up the virtual environment](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#b-set-up-a-virtual-environment-install-dependencies-run-application)
- **c)** [Run through Python IDE after Forking Repository](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#c-a-after-forking-set-up-pycharm-set-up-virtual-environment-install-dependencies-run-application)

### **a-a. Set up PyCharm, Set up a virtual environment, Install dependencies, Run Application**
  - If you do not have PyCharm and want to install [VS Code (Visual studio Code) go to a-b](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#a-b-set-up-visual-studio-code-vs-code-set-up-a-virtual-environment-install-dependencies-run-application)
  - Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/). Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed PyCharm [Download PyCharm Community for Windows](https://www.jetbrains.com/pycharm/download/?section=windows) OR [Download PyCharm Community for Mac](https://www.jetbrains.com/pycharm/download/?section=mac) OR [Download PyCharm Community for Linux](https://www.jetbrains.com/pycharm/download/?section=linux).
  - Then you must open PyCharm:
  - Make a new Project with these instructions: [Create a Python Project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Close the project and exit the application.
  - Go to the Directory of the project you created
  - Extract the Zip files into that folder
  - Open PyCharm again and access the project you created as it should have all the files in the Project
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git)
  - Next, once Python and Pycharm are set up and installed, you'll need to install the dependencies for the project through the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **.py** FILES, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python main.py
```
  - OR you could go to the top, double click on the **main.py** file
  - Then go to the top left corner near the arrow run button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** button which is the Green Arrow.

### **a-b. Set up Visual Studio Code (VS Code), Set up a virtual environment, Install dependencies, Run Application**
  - If you do not have VS Code (Visual studio Code) and want to install [PyCharm go to a-a](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#a-a-set-up-pycharm-set-up-a-virtual-environment-install-dependencies-run-application)
  - Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/). Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed VS Code [Download VS CODE (DOWNLOADS)](https://code.visualstudio.com/Download). Then read the Overview: [VSC Overview](https://code.visualstudio.com/docs/setup/setup-overview).
  - Then you must open VS CODE:
  - INSTALL *all* [**EXTENTIONS for PYTHON + OTHERS**](https://code.visualstudio.com/docs/getstarted/extensions)
  - SETUP Article VSC based on OS: [Windows VSC](https://code.visualstudio.com/docs/setup/windows)  or [Linux](https://code.visualstudio.com/docs/setup/mac)  or [Linux](https://code.visualstudio.com/docs/setup/linux)
  - Make a new Project with these instructions: [Create a Python Project (GET STARTED TUTORIAL)](https://code.visualstudio.com/docs/getstarted/getting-started)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Close the project and exit the application.
  - Go to the Directory of the project you created
  - Extract the Zip files into that folder
  - Open VS Code again and access the project you created as it should have all the files in the Project
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)
  - Next, once Python and VS CODE are set up and installed, you'll need to install the dependencies for the project through the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **.py** FILES, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python main.py
```
  - OR you could go to the top, double click on the **main.py** file
  - Then go to the top left corner near the **Arrow Run** button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** arrow button.

### **b. Set up a virtual environment, Install dependencies, Run Application**
Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/).
Once Python is installed, you'll need to install the dependencies for the project through the Python terminal that you installed. Use these commands to navigate to them and install them:
```bash
cd <directory location where you put the project files>
[ex: cd D:\Translator-Language-Dictionary-App]
```
Next, set up a virtual environment:
  - For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
  - macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
Next, these dependencies are listed in the **requirements.txt** for running the applicaiton AND **requirements-dev.txt** for testing the applciation. install both files and Make sure pip is updated. Use the following commands to install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
Run the Python application: After the dependencies are installed, they can simply run the Python application, for example:
```bash
python main.py
```

### **c-a. After Forking, Set up PyCharm, Set up virtual environment, Install dependencies, Run Application**
  - If you do not have PyCharm and want to install [VS Code (Visual studio Code) go to c-b](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#c-b-after-forking-set-up-visual-studio-code-vs-code-set-up-virtual-environment-install-dependencies-run-application)
  - Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/). Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed PyCharm [Download PyCharm Community for Windows](https://www.jetbrains.com/pycharm/download/?section=windows) OR [Download PyCharm Community for Mac](https://www.jetbrains.com/pycharm/download/?section=mac) OR [Download PyCharm Community for Linux](https://www.jetbrains.com/pycharm/download/?section=linux).
  - Then you must open PyCharm:
  - Make a new Project with these instructions: [Create a Python Project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Login the Git into the Python and use the Git Clone or fetch the repository of the Forked repository you made. [Forking PyCharm Help](https://www.jetbrains.com/help/pycharm/fork-github-projects.html)
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#put-existing-project-under-Git)
  - Next, once Python and Pycharm are set up and installed, you'll need to install the dependencies for the projectthrough the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **.py** FILES, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python main.py
```
  - OR you could go to the top, double click on the **main.py** file
  - Then go to the top left corner near the arrow run button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** button which is the Green Arrow.

### **c-b. After Forking, Set up Visual Studio Code (VS Code), Set up virtual environment, Install dependencies, Run Application**
  - If you do not have VS Code (Visual studio Code) and want to install [PyCharm go to c-a](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#c-a-after-forking-set-up-pycharm-set-up-virtual-environment-install-dependencies-run-application)
  - Before running the application, make sure you have **Python** installed on your machine. You can download Python from the official website: [Download Python](https://www.python.org/downloads/). Once Python is installed, you'll need to install the dependencies for the project either through the PYTHON IDE terminal that you installed VS Code [Download VS CODE (DOWNLOADS)](https://code.visualstudio.com/Download). Then read the Overview: [VSC Overview](https://code.visualstudio.com/docs/setup/setup-overview).
  - Then you must open VS CODE:
  - INSTALL *all* [**EXTENTIONS for PYTHON + OTHERS**](https://code.visualstudio.com/docs/getstarted/extensions)
  - SETUP Article VSC based on OS: [Windows VSC](https://code.visualstudio.com/docs/setup/windows)  or [Linux](https://code.visualstudio.com/docs/setup/mac)  or [Linux](https://code.visualstudio.com/docs/setup/linux)
  - Make a new Project with these instructions: [Create a Python Project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
  - Follow all steps including making sure a virtual environment is set up with the Python you installed.
  - Login the Git into the Python and use the Git Clone or fetch the repository of the Forked repository you made. [Forking VS Code Help](https://code.visualstudio.com/docs/sourcecontrol/github)
  - 2) This option would be to use the Git clone but you *must* clone it to the new project's directory. See this link: [Git Clone to Project](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)
  - Next, once Python and VS CODE are set up and installed, you'll need to install the dependencies for the project through the Python terminal that you installed. Make sure pip is updated. Use these commands to navigate to them and install them:
```bash
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt
```
  - Next, if this does not work, you will have to install the imports one by one by clicking on all the **.py** FILES, and at the top of the imports, click on every imports so that they can be automatically downloaded through PyCharm's Python. Or go to each of them and then type in the Python Packages search bar for each one and install them there.
  - Then once done, **Run** the Python application:
```bash
python main.py
```
  - OR you could go to the top, double click on the **main.py** file
  - Then go to the top left corner near the arrow run button and click on the **tab** -> **CurrentFile**.
  - Then while staying on that file click on the **Run** button which is the Green Arrow.

## **How to Navigate the Translator App GUI**
### Main (Main GUI)
- Once *"main.py"* is running, the user can input:
    - Words or phrases or sentences (Note: this app does not check spelling or grammar errors!)
- Then, the user can select the following options:
    - Languages:  French; Spanish; Portuguese; Italian; German; Netherlands(Dutch); Polish; Ukrainian; Russian
    - Clear:  Clears the input text in text box
    - Translate:  Translate the text to the selected language
    - Open Admin Panel:  Opens the Panel to the Dictionary; History; Settings tabs.
    - Translation appears below Admin Button if translated button is clicked and is translated.
### Dictionary Tab
- Select Open Admin Panel from the main menu main.py
- Selects the Dictionary tab from the Open Admin Panel
- This shows ALL of the words in the translation.db dictionary currently there
- The user can search the words in the dicitonary from search bar with serach and clear buttons
- The user can export or import CSV to the dicitonary
- The user can edit words
- The user can Refresh the database manually if the user modified data
- The user can allow 10,220,50, or 100 entries to appear in the dicitonary
- The user can go to the Next or Prev pages of the dicitonary database
### History Tab
- Select Open Admin Panel from the main menu main.py
- Selects the History tab from the Open Admin Panel
- This shows ALL of the words in the translation.db dictionary currently there
- The user can search the words in the dicitonary from search bar with serach and clear buttons
- The user can export history Email(Outlook only), PDF, JSON, CSV
- [Tutorial to Import UTF-8 EXCEL Data here](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App?tab=readme-ov-file#tutorial-to-import-utf-8-excel-data). 
- The user can Refresh the database manually if the user modified data
- The user can edit words
- The user can allow 10,220,50, or 100 entries to appear in the dicitonary
- The user can go to the Next or Prev pages of the dicitonary database
### Settings Tab
- Select Open Admin Panel from the main menu main.py
- Selects the Settings tab from the Open Admin Panel
- The user can import the SQL lite datebase .db file using import with the .txt files
- The user can toggle online or offline
### Exit
- Select the X red button on the GUI
- It will Exit the Translation Application GUI and exit the Python Application.

## Tutorial to Import UTF-8 EXCEL Data
### OPEN EXCEL
- Click on ```Excel``` to open it by itself (blank file)
- Select ```Blank Workbook```
- Click on ```Data``` tab
- Select ```From Text/CSV``` on the left side inside Data tab
- Go to the directory with your ```database.db``` file that was exported
- Select the file to import it
- Make sure have these **Settings =>**  ``` File Origin: 65001:Unicode(UTF-8)``` ; ``` Delimiter: Commma```; ``` Data Type Detection Row: Based on the first 200 rows```
- Then click ```load`` to finalize the imported data
- It should have all formats correctly converted since the file is in UTF format

## History of Translation Machines
### Wikipedia's Historical Context Short Summary
- [Wikipedia's History of Machine Translation](https://en.wikipedia.org/wiki/History_of_machine_translation)
- Machine translation evolved from early conceptual ideas in the Middle Ages and Enlightenment to practical but limited mechanical proposals in the 1930s. Real computational MT began in the 1950s with dictionary-based systems like the Georgetown–IBM experiment.
- Progress stalled after the 1966 ALPAC report, which concluded MT was slow and ineffective, leading to a collapse in U.S. funding. However, rule-based and domain-specific systems continued in Europe and Canada.
- A major shift in the 1980s and 1990s saw the introduction of statistical and example-based MT, which drove the first widespread public systems and early web translators.
- In the 2000s, MT expanded into speech translation and broad-domain content.
- From 2014 onward, neural machine translation (NMT) revolutionized the field, enabling high-quality, fluent, context-aware translation—the foundation of modern tools like Google Translate and DeepL.
### How it's related to my Translation Applicaiton?
- My Translation Applicaiton is a simple multi-language GUI translator built with Python that supports both online and local translation methods by using a database like SQL(sqlite).
- It uses a dictionary-style approach, can connect to a free online API like Google Translate, and allows users to translate words or phrases across many languages and offers local support by importing in dicitonary .txt files to add to the SQL (sqlite) database.
- The app handles Unicode fonts for languages such as lanauges that need support like Cyrillic which lets users maintain and export a history of translated words, and provides a clean interface for entering text, viewing results, editing data, and saving data.

## **Introduction, Requirements, and Objectives**
This document outlines the deliverables for a CS50 Capstone Final Project: a Translation Appolcaiton developed with Python, SQL(sqlite), IT/Cyber(email features), and exporting datas within a unified GUI. The project follows the Waterfall/Agile development model, progressing through defined phases: Requirements Analysis, System Design, Implementation, Testing, and Maintenance. This focuses on gathering detailed requirements, initial design, and prototyping, as well as developing functional modules and early versions of the gui. The project’s purpose is to create a centralized local and online tranlsation application, allowing users to translate words, sentences, or phrases in one application. Git will be used for version control, and testing(unit;auto;system;manual;integration) will ensure each component meets requirements. Deliverables include a fully functional translation game with intuitive GUI, featuring Admin Panel to allow the user to see the translation.db database (SQL)(sqlite) from the Dictionary, History, and Settings tab. Then the user will also have access to import or export the data.
### Testing/Debugging Requirements:
  - To track progress on each coding section, we will use Git for Version Control.
  -  Each process will include a Git commit section
  - Each readme file will ensure that the user knows how the set the requirements of the software and run the application to play the games.
  - Note: Refer to "doc" folder which is up-to-date with all our Technical Documentation per Unit (weeks: 1-8)
### Version Control with Git
This project uses Git for version control. Git will be used to track the progress of the project, manage code changes, and ensure collaboration between developers. Every change made to the codebase will be tracked with commit messages, providing a clear history of the project's development. Here's how we manage code changes:
#### Branching and Commit Process
- Create a Branch: Each developer creates a separate feature branch for a specific task
- Commit Changes: Developers commit incremental changes with descriptive commit messages
- Push Changes: After completing tasks in a remote branch that was created, developers push the branch to GitHub.
- Pull Request (PR): Create a Pull Request for code review. Once approved, the changes are merged into the main branch.
### Code Review and Merge
- If changing major game files `.py`, the Git Leader will get approvals from the PR and ensure code quality and functionality.
- If changing minor files (txt, md, not game files, etc) the user(name of team) will get approvals from the PR and ensure code quality and functionality.
- Once the Git Leader/User(team) passes the review, it will be merged into the main branch.
- The Project Manager and the Testers will ensure that each update is working and tested.
- Developers will regularly pull the latest changes from the main branch to keep their feature branches up to date and avoid conflicts.
- If any merge conflicts arise, the developer will resolve them before pushing their changes, ensuring that the codebase remains functional and consistent.
#### See Git History Progress
  - To see the Progress go to the project repository [CS50 Final Capstone: Translator-Language-Dictionary-App](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App)
  - Click on Branches to see all Branches. Then click on Each branch individually to see the changes in each branch. Once finished, go back to the project
  - Click on Pull Requests to see all the branches that were merged into the main. Opens are the ones not merged but able to be compared, the closed ones should show the branches that were merged into the main after approval and comparison. This method protects the main final and makes sure that the main files are not touched. Once, finished, go back to the project.
- Click on the Issues to see all the open and closed issues per milestones and tags.
- Click on the Actions to see all the Unit Tests run through GitHub actions by the (.yml) files.
  - Note: You can also see each Weekly Unit progress on Git through the "docs" folder where it shows per each week.
### Testing and Debugging
- Automated Testing: Test each game module for correctness.
- Integration Testing: Ensure the main menu and individual game modules work seamlessly together.
- System Testing: Test the full application to ensure the overall user experience is smooth.
### **Automated Testing and Manual Testing Instructions:**
- Go to the file **"tests/((all test .py files here...))"** in the main branch and Run it. It should test all types of tests in that folder directory.
- If it doesn't work, click on each method section for the game and run it one by one.
0)  **Steps/Procedures**:
1) **GitHub Actions (tests) (Skip if you do not have access to the Repo)**:
- Go to [https://github.com/VictoriaRaven/Translator-Language-Dictionary-App](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App)
- Go to Actions Tab
- If Workflow is Disabled, Enable it
- Click on the Workflow [1) Auto Run Tests For Mac with all push; Auto Run Tests For Windows with all push; Auto Run Tests For Ubuntu with all push ](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/actions)
- Go to the right side of “This workflow has a workflow_dispatch event trigger.”
- Click on Run Workflow
- Make sure it’s on Main branch (the .yml files autoruns on separate branches even if run through main)
- Click Run Workflow (green to confirm)
- Refresh the page to see the GitHub Action process and if green it passes
- Environments runs (Win, Mac, Linux), but Windows for this tk(gui python) has glitches due to Git’s ongoing issue.
2) **Testing in IDE**:
- Download the code from GitHub in the “main” branch. 
- Open IDE and open the project from where it was saved
- Install all needed libraries (IDE should prompt to do this automatically)
- Go to the /tests/ directory with cd
```bash
D:// cd tests
```
- Run all of the .py tests in the directory of "tests/...all test .py files here..." (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest
```
- To Run a sigle .py test in the directory do:
```bash
D:// ... directory of the project...
python -m pytest tests/test_algorithms.py
```
- If it does not work go to main root with ```cd```
- Run all of the .py tests again in the root directory of project imported (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest
```
3) **Manual Test Data preparation**:
- Testing will be done through the “main” branch of the GitHub, test.py.
- Manual Testing will be done through the “main” and other branches.
- All test files should be located in: ```tests/...all test .py files here..." (Works for WIN; MAC; UBU)```
- All ```lang_dictionary.txt``` files and ```translations.db (SQL)``` database should be in the directory: ```data/...all data files here..." (Works for WIN; MAC; UBU)```
- The ```requirments.txt``` and ```requirements-dev.txt``` are in the root directory
- All workflows located in the github actions workflows as well as the security bot.
4) **Test Environment Configuration**:
- Operating System: Windows, macOS, or Linux
- Python Version: 3.9 or later
- Terminal Tools: Command line, PowerShell, terminal, or IDE
- Required Libraries: ```requirments.txt``` and ```requirements-dev.txt``` are in the root directory (all are in this file)
- Audio: Ensure audio output is enabled to validate sound-related tests.
- Display: Use a resolution of at least 600x400 for consistent rendering.
- GitHub Actions:  Required you have access to the Repository and can go to the Actions tab
0) **Manual Testing.xlsx (Manual Testing):**
- Go to the docs to find a copy of the Excel/Sheets/table for manual testing. 
- Or Go to the docs in to get the link to the Excel/Sheets/table for manual testing.
- This is Manual Tests using the Excel/Sheets/table method
- Docs Link to All Testing: [Here](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/docs)
1) **Steps/Procedures**:
- Command line, terminal or PowerShell steps: 
- Download the code from GitHub in the “main” branch of folder containing ```tests/...all test .py files here..." (Works for WIN; MAC; UBU)```. Refer to README.md for help.
- Navigate to the project directory
- Ensure installation of dependencies through the ```requirments.txt``` and ```requirements-dev.txt`` like shown in README.md
- Run a sigle .py test in the directory of "tests/...all test .py files here..." (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest tests/test_algorithms.py
```
- Run all of the .py tests in the directory of "tests/...all test .py files here..." (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest
```
- From there test each linked .py sections
- Follow the steps provided in the Manual Testing.xlsx file
- For each test Perform the Input/Action
- Observe the result
- Compare it against the Expected Result
- Log pass/fail status
2) **Testing in IDE**:
- Download the code from GitHub in the “main” branch. 
- Open IDE and open the project from where it was saved
- Install all needed libraries (IDE should prompt to do this automatically)
- Go to the /tests/ directory with cd
```bash
D:// cd tests
```
- Run all of the .py tests in the directory of "tests/...all test .py files here..." (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest
```
- If it does not work go to main root with ```cd```
- Run all of the .py tests again in the root directory of project imported (Works for WIN; MAC; UBU)
```bash
D:// ... directory of the project...
python -m pytest
```
3) **Test Data preparation**:
- Testing will be done through the “main” branch of the GitHub, test.py.
- Manual Testing will be done through the “main” and other branches.
- All test files should be located in: ```tests/...all test .py files here..." (Works for WIN; MAC; UBU)```
- All ```lang_dictionary.txt``` files and ```translations.db (SQL)``` database should be in the directory: ```data/...all data files here..." (Works for WIN; MAC; UBU)```
- The ```requirments.txt``` and ```requirements-dev.txt``` are in the root directory
- All workflows located in the github actions workflows as well as the security bot.
4) **Test Environment Configuration**:
- Operating System: Windows, macOS, or Linux
- Python Version: 3.9 or later
- Terminal Tools: Command line, PowerShell, terminal, or IDE
- Required Libraries: ```requirments.txt``` and ```requirements-dev.txt``` are in the root directory (all are in this file)
- Audio: Ensure audio output is enabled to validate sound-related tests.
- Display: Use a resolution of at least 600x400 for consistent rendering.
- GitHub Actions:  Required you have access to the Repository and can go to the Actions tab
#### Testing Overview:
Automated testing was implemented using Python’s import frameworks to validate critical components of the other .py modules. Once verification is complete, the process will move into integration testing to ensure smooth interaction between components, including menu navigation, addtional features, and CS50's integraiton of lessons learned. System testing will follow, simulating real-world usage scenarios to confirm that the application performs reliably under typical and extreme conditions. Lastly, acceptance testing will be performed to validate that all project requirements have been met and the application aligns with stakeholder expectations. Testing outcomes will be documented in detail, and any issues uncovered will be addressed through a feedback loop prior to final deployment. This structured approach ensures a thorough and sequential validation of the system’s readiness for delivery. Through the testing approach, we will also use the software engineering techniques of Testing to ensure that each part is tested and debugged correctly.
- **Next Phase Testing (Breakdown)**:
  - Future testing will follow the Waterfall/Agile methodology, starting after full system implementation.
  - **Auto-Testing**: Verify core functionalities (AI decisions, answer validation, collision detection).
  - **Integration Testing**: Ensure smooth interaction between components (menu navigation, game transitions, audio/visual responses).
  - **System Testing**: Simulate real-world scenarios to confirm reliability under typical and extreme conditions.
  - **Acceptance/Manual Testing**: Validate that all project requirements are met and align with stakeholder expectations.
  - All testing outcomes will be documented, and issues will be addressed through a feedback loop before final deployment.
- **Debugging Process (Simple Breakdown)**:
  - Debug each module systematically to identify and fix issues.
  - **UI Debugging**: Ensure the interface is intuitive and responsive across devices and screen sizes.
  - **Performance Testing**: Confirm data/gui load in under 3 seconds and run smoothly, even on lower-end devices.
  - **Cross-Platform Compatibility**: Test the application on multiple platforms to ensure consistent functionality across operating systems.
#### Debugging Process
- Use Git to track and resolve issues by creating separate branches for bug fixes.
- Issues can be either included in the Git or done thorough a local machine.
- Each commit / new push after a PR will document the changes and improvements made during debugging.

## Project Architecture
This portion is included in the document folder **"docs"** and the diagrams included in one of the sections.
### Start of the Implementation:
- **Implementation Of GUI**: All of it is in the DOCS folder. [HERE](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/docs)
### Class/UML/Use Case/Activity Diagrams
The use case diagram illustrates how users interact with the application: starting from launching the app, selecting a option from the main menu (main.py), and engaging with the mechanics. The activity diagram shows the flow of actions, starting from the application launch, progressing through the deicitonary tabs selection of Open Admin Panel, importing/exporting data, editing data, veiwing data, page changes. The class and uml diagram is similar to the activity diagram but includes the classes, codes, and functions/methods and how it intreacts with each other.
## Overview of Progress and Conclusion
### Project Plan Goals:
- Develop a application
- Use a modular design for easy maintenance and future gui/tk additions.
- Integrate version control with Git and implement testings for component verification.
- Follow the Waterfall/Agile development model for structured project phases.
### Project Design Goals:
- Create a centralized menu system 
- Implement individual modules with interactive user interfaces.
- Ensure scalability and maintainability for future enhancements.
### Phase 1 Goals:
- Focus on requirements gathering, initial design, and prototyping.
- Develop early functional modules and working versions of the gui.
- Ensure alignment between project objectives and technical execution.
- Set a foundation for reliable, maintainable development in subsequent phases.
### Testing Goals:
- Implement automated tests using Python’s import framework to validate mechanics.
- Perform testings for gui logic (tranlsations), UI components, import/export data, send emails, searches, editing data, error handling, and performance.
- Follow a structured testing approach including unit, integration, system, manual and acceptance testing.
- Document testing outcomes and address issues before final deployment.
### Phase 2 Goals:
- Conduct full system implementation with finalized features and functionality.
- Perform integration testing to ensure smooth interaction between components
- Simulate real-world usage scenarios through system testing.
- Conduct acceptance testing to confirm the application meets all project requirements and stakeholder expectations.
### User Guide (Before Deployment):
- Develop a clear and concise **User Guide** detailing how to navigate the Game Hub.
- Provide instructions for starting the application, selecting the buttons, dicitonary, serach, pages/exports/imports, and using UI features.
- Include troubleshooting tips, known issues, and any additional features or options available
- Refer to the docs folder section to access our User Guide version.
- Link is here: [User Guide](https://github.com/VictoriaRaven/Translator-Language-Dictionary-App/tree/main/docs)
### Deployment Goals:
- Finalize the application after testing and bug fixes.
- Ensure cross-platform compatibility and smooth performance on different devices.
- Deploy the project for user access, ensuring all requirements are met.
- Monitor post-deployment performance and user feedback for future updates.

### Contact
Feel free to pm me (VictoriaRaven) if you want to use my code under a specific license and without needing to fork my repository and also for details on our code
of conduct, and the process for submitting pull requests to me if you wish to collaborate.

## Authors
  - **Victoria Lee** - [VictoriaRaven](https://github.com/VictoriaRaven)
  - Contributers: None/NA

## Acknowledgments
- [Google Scholar](https://scholar.google.com/)
- [Python Doc](https://docs.python.org/3/)
- [GeeksforGeeks SDLC Waterfall Model](https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/)
- [GeeksforGeeks SDLC Agile Model](https://www.geeksforgeeks.org/software-engineering/agile-sdlc-software-development-life-cycle/)
- [GitHub Resources](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- [Google Scholar](https://scholar.google.com/)
- [Wikipedia](https://www.wikipedia.org/)
- [UMGC Library](https://libguides.umgc.edu/home)
- [UMGC CS Resources](https://libguides.umgc.edu/c.php?g=316603&p=2114865)
- Bradley N. Miller, David L. Ranum, and Julie Anderson, *Python Programming in Context*, 3rd ed., Jones & Bartlett Learning, Oct. 2019. [Online Textbook Available](https://www.oreilly.com/library/view/python-programming-in/9781284175578/.)
 - Thank you!
 - VictoriaRaven
