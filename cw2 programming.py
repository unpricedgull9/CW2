import requests          # Used to send HTTP requests to the API
import datetime          # Used to get the current date and time

while True:
    # Ask the user to enter a word and remove extra spaces
    word = input("Enter the word you would like definitions for (to quit write esc)\n").strip()

    # Exit condition
    if word.lower() == "esc":
        print("Program exited.")
        break

    # Build the API URL using the entered word
    url = f"https://dictionary-api-7hmy.onrender.com/define?word={word}"

    try:
        # Send a GET request to the dictionary API
        response = requests.get(url)
        
        # Raise an error if the response status is not successful
        response.raise_for_status()
        
        # Convert the response to JSON format
        data = response.json()
        
        # If the API returns a list, take the first item
        if isinstance(data, list) and len(data) > 0:
            data = data[0]

    # Handle HTTP errors (for example, word not found)
    except requests.exceptions.HTTPError:
        print(f"HTTP Error {response.status_code}: Word may not be found.")
        continue

    # Handle connection problems
    except requests.exceptions.RequestException:
        print("Couldn't connect to the dictionary API")
        continue

    # Function to extract definition and part of speech from API data
    def extract_word_data(data):
        # Get the definition or use a default message
        definition = data.get("definition", "No definition available.")
        
        # Get the part of speech or use N/A
        part_of_speech = data.get("partOfSpeech", "N/A")
        
        return definition, part_of_speech

    # Get the definition and part of speech
    definition, part_of_speech = extract_word_data(data)

    # Check if the definition is too short or missing
    if not definition or len(definition) < 5:
        definition = "No complete definition available from API."

    # Count the number of characters in the definition
    num_chars = len(definition)

    # Count the number of words in the definition
    num_words = len(definition.split())

    # Display results to the user
    print(f"\nFor the word '{word}' we have found:\n")
    print(f"Definition: {definition}")
    print(f"Part of Speech: {part_of_speech}\n")

    print(f"The definition is {num_chars} characters long")
    print(f"The definition is {num_words} words long\n")

    # Function to log the searched word into a text file
    def logword(word, part_of_speech, filename="past_words.txt"):
        # Get the current date and time
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y at %H:%M")
        
        # Open the file in append mode and save the search
        with open(filename, "a", encoding="UTF-8") as file:
            file.write(f"{word}|{part_of_speech}|{timestamp}\n")
        
        return timestamp

    # Log the current search and store the timestamp
    timestamp = logword(word, part_of_speech)

    # Function to count how many times a word was searched
    def count_word_occurrences(word, filename="past_words.txt"):
        count = 0
        try:
            # Open the log file for reading
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    # Split each line by "|"
                    parts = line.strip().split("|")
                    
                    # Check if the word matches (case-insensitive)
                    if len(parts) >= 1:
                        logged_word = parts[0]
                        if logged_word.lower() == word.lower():
                            count += 1
        except FileNotFoundError:
            # If the file does not exist, return 0
            return 0
        return count
        

    # Count how many times the word was searched
    count = count_word_occurrences(word)

    # Print the search count with correct grammar
    if count != 1:
        print(f"The word '{word}' has been searched {count} times\n")
    else:
        print(f"The word '{word}' has been searched {count} time")

    # Print when the search was logged
    print(f"This search was logged on {timestamp}\n")
