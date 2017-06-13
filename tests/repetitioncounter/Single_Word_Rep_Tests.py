import unittest

import src.repetitioncounter.count_repetitions


class singlewordreptests(unittest.TestCase):
    def test_single_rep_word_twice_returns_just_that_word(self):
        test_input = [
            "When", "woke", "this", "morning", "beautiful", "morning",
            ]
        expected_output = {
            'morning': 2,
        }
        actual_output = src.repetitioncounter.count_repetitions.count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_single_rep_word_returns_three_times_just_that_word(self):
        test_input = [
            "Romeo", "Romeo", "wherefore", "are", "thou", "Romeo",
        ]
        expected_output = {
            "Romeo": 3,
        }
        actual_output = src.repetitioncounter.count_repetitions.count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_phrase_without_repetition_returns_no_repetition(self):
        test_input = "Give me a phrase where there is no repetition".split(' ')
        expected_output = {}
        actual_output = src.repetitioncounter.count_repetitions.count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()



