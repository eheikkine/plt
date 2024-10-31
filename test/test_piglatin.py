import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        input_phrase = "Hello world"
        self.assertEqual("Hello world", input_phrase)

    def test_input_empty_string(self):
        translator = PigLatin("")
        self.assertEqual("nil", translator.translate())

    def test_word_starting_with_vowel_and_ends_y(self):
        translator = PigLatin("any")
        self.assertEqual("anynay", translator.translate())

    def test_word_starting_with_vowel_and_ends_vowel(self):
        translator = PigLatin("apple")
        self.assertEqual("appleyay", translator.translate())

    def test_word_starting_with_vowel_and_ends_consonant(self):
        translator = PigLatin("ask")
        self.assertEqual("askay", translator.translate())


