import unittest
from translator import english_to_french, french_to_english

class TestTranslationFunctions(unittest.TestCase):

    # Test the English to French Function
    def test_english_to_french(self):
        self.assertEqual(
            english_to_french('Hello')['translations'][0]['translation'], 
            'Bonjour'
        )
        self.assertEqual(
            english_to_french('Goodbye')['translations'][0]['translation'],
            'Au revoir'
        )
    
    # Test the French to English Function
    def test_french_to_english(self):
        self.assertEqual(
            french_to_english('Bonjour')['translations'][0]['translation'],
            'Hello'
        )
        self.assertEqual(
            french_to_english('Au revoir')['translations'][0]['translation'],
            'Goodbye'
        )

if __name__ == '__main__':
    unittest.main()
