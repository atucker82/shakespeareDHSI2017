import unittest

class singlewordreptests(unittest.TestCase):
    def test_single_rep_word_twice_returns_just_that_word(self):
        test_input = "When I woke up this morning, it was a beautiful morning"
        expected_output = {
            'morning': 2,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_single_rep_word_returns_three_times_just_that_word(self):
        test_input = "Romeo, Romeo, wherefore are thou Romeo?"
        expected_ouput = {
            'Romeo', 3,
        }
        actual_output = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)

    def test_phrase_without_repetition_returns_no_repetition(self):
        test_input = "Give me a phrase where there is no repetition"
        expected_output = {}
        actual_ouput = count_repetitions(test_input)
        self.assertEqual(expected_output, actual_output)


