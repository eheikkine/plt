import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        input_phrase = "Hello world"
        self.assertEqual("Hello world", input_phrase)
