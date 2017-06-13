import unittest

from src.repetitioncounter.count_repetitions import tokenize


class Tokenizertest(unittest.TestCase):

    def test_tokenizer_splits_on_spaces_and_lowercase(self):
        test_input = "The quick brown fox"
        expected_output = ["the", "quick", "brown", "fox",]
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)

    # disregard punctation
    def test_tokenizer_unwanted_punct(self):
        test_input = "Romeo, Romeo, wherefore are thou Romeo?"
        expected_output = ["romeo", "romeo", "wherefore", "are", "thou", "romeo"]
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)

    # keep dashes and apostrophes within words
    def test_tokenizer_dashes_apostrophes(self):
        test_input = "Let's meet face-to-face"
        expected_output = ["let's", "meet", "face-to-face",]
        actual_output = tokenize(test_input)
        self.assertEqual(expected_output, actual_output)


