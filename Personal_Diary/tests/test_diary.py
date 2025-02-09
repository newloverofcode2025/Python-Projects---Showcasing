# tests/test_diary.py

import unittest
import os
import json
from diary import load_entries, save_entries

class TestDiary(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file for testing."""
        self.test_file = "data/test_entries.json"
        self.entries = [{"title": "Test Title", "content": "Test Content"}]
        save_entries(self.entries)

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_entries(self):
        """Test loading entries from the JSON file."""
        loaded_entries = load_entries()
        self.assertEqual(loaded_entries, self.entries)

    def test_save_entries(self):
        """Test saving entries to the JSON file."""
        new_entries = [{"title": "New Title", "content": "New Content"}]
        save_entries(new_entries)
        with open("data/diary_entries.json", "r") as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, new_entries)

if __name__ == "__main__":
    unittest.main()