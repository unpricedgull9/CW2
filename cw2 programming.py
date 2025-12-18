import requests
import json
import datetime

word = input("Enter the word you would like definitions for\n").strip()
url = f"https://dictionary-api-7hmy.onrender.com/define?word={word}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        data = data[0]
except requests.exceptions.HTTPError:
    print(f"HTTP Error {response.status_code}: Word may not be found.")
    exit()
except requests.exceptions.RequestException:
    print("Couldn't connect to the dictionary API")
    exit()

def extract_word_data(data):
    definition = data.get("definition", "No definition available.")
    part_of_speech = data.get("partOfSpeech", "N/A")
    return definition, part_of_speech

definition, part_of_speech = extract_word_data(data)

if not definition or len(definition) < 5:
    definition = "No complete definition available from API."

num_chars = len(definition)

num_words = len(definition.split())

print(f"\nFor the word '{word}' we have found:\n")
print(f"Definition: {definition}")
print(f"Part of Speech: {part_of_speech}\n")

print(f"The definition is {num_chars} characters long")
print(f"The definition is {num_words} words long\n")

def logword(word, part_of_speech, filename="past_words.txt"):
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y at %H:%M")
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(f"{word}|{part_of_speech}|{timestamp}\n")
    return timestamp

timestamp = logword(word, part_of_speech)

def count_word_occurrences(word, filename="past_words.txt"):
    count = 0
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) >= 1:
                    logged_word = parts[0]
                    if logged_word.lower() == word.lower():
                        count += 1
    except FileNotFoundError:
        return 0
    return count

count = count_word_occurrences(word)
if count != 1:
    print(f"The word '{word}' has been searched {count} times\n")
else:
    print(f"The word '{word}' has been searched {count} time")
    
print(f"This search was logged on {timestamp}\n")
