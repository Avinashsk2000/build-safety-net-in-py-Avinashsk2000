import unittest
from soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        """Test handling of empty input."""
        self.assertEqual(generate_soundex(""), "0000")

    def test_single_character(self):
        """Test handling of single character input."""
        self.assertEqual(generate_soundex("A"), "A000")

    def test_basic_name(self):
        """Test a basic name with no repeated or adjacent codes."""
        self.assertEqual(generate_soundex("Smith"), "S530")

    def test_repeated_consonant_codes(self):
        """Test handling of adjacent characters with the same code."""
        self.assertEqual(generate_soundex("Pfister"), "P236")

    def test_vowels_ignored(self):
        """Test that vowels and non-mapped characters are ignored."""
        self.assertEqual(generate_soundex("Ashcraft"), "A261")

    def test_case_insensitivity(self):
        """Test that the function is case-insensitive."""
        self.assertEqual(generate_soundex("Robert"), generate_soundex("robert"))

    def test_padding_to_four_digits(self):
        """Test that the output is always padded to four digits."""
        self.assertEqual(generate_soundex("R"), "R000")

    def test_trimming_to_four_digits(self):
        """Test that the output is trimmed to four digits."""
        self.assertEqual(generate_soundex("Rubinstein"), "R152")

    def test_non_alphabetic_characters(self):
        """Test that non-alphabetic characters are ignored."""
        self.assertEqual(generate_soundex("A!@#$"), "A000")

    def test_names_with_spaces(self):
        """Test names with spaces."""
        self.assertEqual(generate_soundex("John Smith"), "J525")
        self.assertEqual(generate_soundex("John  Smith"), "J525")  # Multiple spaces

    def test_numbers_in_name(self):
        """Test names with numbers."""
        self.assertEqual(generate_soundex("R2D2"), "R320")

if __name__ == '__main__':
    unittest.main()
