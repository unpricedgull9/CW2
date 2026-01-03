# CIS1702 CW2 – Dictionary API Program

This project was developed as part of the CIS1702 Programming 1 Coursework 2 group assignment.

The program is a command-line Python application that allows the user to enter a word, retrieves its definition from an online dictionary API, and displays useful information about that definition. It also stores search history so previous searches can be tracked between program runs.

---

## What the program does
When the program runs, it:
- Prompts the user to enter a word
- Sends a request to a public dictionary API
- Retrieves the definition and part of speech
- Checks that a valid definition is returned
- Calculates the number of characters and words in the definition
- Displays the results clearly in the terminal
- Logs the searched word with a timestamp
- Counts how many times the same word has been searched before

---

## Files used by the program
- **Main Python file**  
  Contains all program logic including user input, API communication, analysis, and file handling.

- **past_words.txt**  
  Stores a history of searched words in the format:  
  `word | part of speech | date and time`

These files are created automatically if they do not already exist.

---

How to Use the Program

### Step 1: Open Command Prompt and type "pip install requests" and press enter

### Step 2: Run the code in either 'VS Code' or 'Python'

### Step 3: Enter the word you would like to search in the dictionary

### Step 4: The program will loop until user inputs "!Exit"