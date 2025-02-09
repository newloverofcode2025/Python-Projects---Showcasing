# diary.py

import os
import json

DATA_FILE = "data/diary_entries.json"

def load_entries():
    """Load diary entries from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_entries(entries):
    """Save diary entries to the JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as file:
        json.dump(entries, file, indent=4)

def add_entry():
    """Add a new diary entry."""
    title = input("Enter the title of the entry: ")
    content = input("Enter the content of the entry: ")
    entries = load_entries()
    entries.append({"title": title, "content": content})
    save_entries(entries)
    print("Entry added successfully!")

def view_entries():
    """View all diary entries."""
    entries = load_entries()
    if not entries:
        print("No entries found.")
        return
    for idx, entry in enumerate(entries, start=1):
        print(f"{idx}. Title: {entry['title']}")
        print(f"   Content: {entry['content']}\n")

def main():
    while True:
        print("\nPersonal Diary Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()