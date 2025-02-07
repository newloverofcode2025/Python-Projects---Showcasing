import unittest
from analyze_text import analyze_text

class TestAnalyzeText(unittest.TestCase):
    def test_analyze_text(self):
        # Test with a sample text
        sample_text = "Hello world! Hello everyone."
        with open('sample.txt', 'w', encoding='utf-8') as f:
            f.write(sample_text)
        
        word_count, char_count, most_common_words = analyze_text('sample.txt')
        
        self.assertEqual(word_count, 4)
        self.assertEqual(char_count, 20)
        self.assertEqual(most_common_words, [('hello', 2), ('world', 1), ('everyone', 1)])
    
    def test_empty_file(self):
        # Test with an empty file
        with open('empty.txt', 'w', encoding='utf-8') as f:
            f.write('')
        
        word_count, char_count, most_common_words = analyze_text('empty.txt')
        
        self.assertEqual(word_count, 0)
        self.assertEqual(char_count, 0)
        self.assertEqual(most_common_words, [])

    def test_punctuation_only(self):
        # Test with a file containing only punctuation
        punctuation_text = "!@#$%^&*()"
        with open('punctuation.txt', 'w', encoding='utf-8') as f:
            f.write(punctuation_text)
        
        word_count, char_count, most_common_words = analyze_text('punctuation.txt')
        
        self.assertEqual(word_count, 0)
        self.assertEqual(char_count, 0)
        self.assertEqual(most_common_words, [])

    def test_mixed_case(self):
        # Test with a file containing mixed case words
        mixed_case_text = "Hello World! HELLO world!"
        with open('mixed_case.txt', 'w', encoding='utf-8') as f:
            f.write(mixed_case_text)
        
        word_count, char_count, most_common_words = analyze_text('mixed_case.txt')
        
        self.assertEqual(word_count, 4)
        self.assertEqual(char_count, 20)
        self.assertEqual(most_common_words, [('hello', 2), ('world', 2)])

    def test_numbers(self):
        # Test with a file containing numbers
        numbers_text = "123 456 123"
        with open('numbers.txt', 'w', encoding='utf-8') as f:
            f.write(numbers_text)
        
        word_count, char_count, most_common_words = analyze_text('numbers.txt')
        
        self.assertEqual(word_count, 3)
        self.assertEqual(char_count, 9)
        self.assertEqual(most_common_words, [('123', 2), ('456', 1)])

if __name__ == '__main__':
    unittest.main()