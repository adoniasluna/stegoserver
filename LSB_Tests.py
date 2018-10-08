import unittest
import LSB


class TestImageMethods(unittest.TestCase):

    def test_insert_message(self):
        blue_values = [0 for i in range(40)]
        expected_values = [0 for i in range(31)] + [1, 0, 1, 0, 0, 0, 0, 0, 1]
        msg = 'A'
        self.assertEqual(LSB.insert_message(blue_values, msg), expected_values)

    def test_extract_message(self):
        blue_values = [0 for i in range(40)]
        message_blue_values = LSB.insert_message(blue_values, 'A')
        message = LSB.extract_message(message_blue_values)
        self.assertEqual(message, 'A')


if __name__ == '__main__':
    unittest.main()