import requests
import json

word = input("Enter the word you would like definitions for\n").strip()
url = f"https://dictionary-api-7hmy.onrender.com/define?word={word}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Handle list response
    if isinstance(data, list) and len(data) > 0:
        data = data[0]  # take the first definition

except requests.exceptions.HTTPError:
    print(f"HTTP Error {response.status_code}: Word may not be found.")
    exit()
except requests.exceptions.RequestException:
    print("Couldn't connect to the dictionary API")
    exit()

def extract_word_data(data):
    """
    Extracts full definition and part of speech from API response.
    """
    definition = data.get("definition", "No definition available.")
    part_of_speech = data.get("partOfSpeech", "N/A")
    return definition, part_of_speech

definition, part_of_speech = extract_word_data(data)

if not definition or len(definition) < 5:
    definition = "No complete definition available from API."

print(f"\nFor the word '{word}' we have found:\n")
print(f"Definition: {definition}")
print(f"Part of Speech: {part_of_speech}")
