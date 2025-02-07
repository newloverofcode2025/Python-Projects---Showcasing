from collections import Counter
import string
import sys
import logging

logging.basicConfig(level=logging.INFO)

def analyze_text(file_path):
    """Analyzes a text file for word count, character count, and most frequent words."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            logging.info("The file is empty.")
            return 0, 0, []

        # Remove punctuation and convert to lowercase
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translator).lower()

        # Word count
        words = cleaned_text.split()
        word_count = len(words)

        # Character count
        char_count = len(cleaned_text.replace(" ", ""))

        # Most frequent words
        word_freq = Counter(words)
        most_common_words = word_freq.most_common(5)

        return word_count, char_count, most_common_words
    except Exception as e:
        logging.error(f"Error analyzing text: {e}")
        raise RuntimeError(f"Error analyzing text: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_text.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = analyze_text(file_path)
    if result:
        word_count, char_count, most_common_words = result
        print(f"Word Count: {word_count}")
        print(f"Character Count: {char_count}")
        print("Most Frequent Words:")
        for word, freq in most_common_words:
            print(f"{word}: {freq}")