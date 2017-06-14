import unittest

from src.repetitioncounter.count_repetitions import count_repetitions,tokenize

class MultiWordPhraseRepTests(unittest.TestCase):

    def test_repetition_when_first_instance_is_later_in_the_sentence(self):
        test_input = tokenize("He looked out at the beautiful morning and said \"what a beautiful morning!\"")
        expected_output = {"beautiful morning" : 2,
                           "beautiful" : 2,
                           "morning" : 2,}
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_repetition_when_seperated_by_more_than_one_word(self):
        test_input = tokenize("To be or not to be, that is the question")
        expected_output = {"to be" : 2,
                           "to" : 2,
                           "be" : 2,}
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_that_a_phrase_that_is_repeated_immediately_is_reported(self):
        test_input = tokenize("Oh yes, oh yes, what a beautiful morning")
        expected_output = {"oh yes" : 2,
                           "oh" : 2,
                           "yes" : 2,}
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    #test that a complete phrase that is nothing but rep is reported
    def test_complete_phrase_is_rep_is_reported(self):
        test_input = tokenize("Oh yes oh yes")
        expected_output = {"oh yes": 2,
                            "oh": 2,
                            "yes": 2,
                           }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    #returns proper hyphenated punctuation
    def test__rep_words_part_of_longer_phrases_reported(self):
        test_input = tokenize("To-morrow yes to-morrow yes I love you to-morrow")
        expected_output = {"to-morrow yes" : 2,
                           "to-morrow" : 3,
                           "yes" : 2,
                           }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    #test rep of more than two words
    def test_two_plus_phrases(self):
        test_input = tokenize("I love you I love you")
        expected_output = {"i love you" : 2,
                           "i" : 2,
                           "love" : 2,
                           "you" : 2,
                           "love you" : 2,
                           "i love" : 2,
                            }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    #Test words with hyphens are not equivalient words without hyphens
    def test_hyphens_are_not_equivalent(self):
        test_input = tokenize("To-morrow yes tomorrow yes to-morrow creeps past the break of day")
        expected_output = {"to-morrow" : 2,
                          "yes" : 2,
                          }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)
