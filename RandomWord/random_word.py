import random
import os
import logging
from typing import Optional

logging.basicConfig(level=logging.DEBUG)

def get_random_word(file_path: str) -> Optional[str]:
    """Reads a file and returns a random word."""
    logging.debug(f"Checking if file exists: {file_path}")
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.readlines()
            logging.debug(f"Read {len(words)} lines from the file.")
            print(f"File content: {words}")  # Print file content for debugging
            words = [word.strip() for word in words if word.strip()]
            logging.debug(f"Filtered down to {len(words)} non-empty words.")
            if not words:
                logging.error("No words found in the file.")
                return None
            return random.choice(words)
    except OSError as e:
        logging.error(f"OS error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    file_path = "words.txt"
    logging.debug(f"Using file path: {file_path}")
    random_word = get_random_word(file_path)
    if random_word:
        print(f"Random word: {random_word}")
    else:
        print("No words found in the file.")