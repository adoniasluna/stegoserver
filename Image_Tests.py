import unittest
import ImageOperations as imgop


class TestImageMethods(unittest.TestCase):

    def test_blue_values(self):
        blue_values = imgop.extracting_blue('screen.png')
        self.assertEqual(imgop.extracting_blue('screen.png'), blue_values)

    def test_write_new_image(self):
        blue_values = imgop.extracting_blue('screen.png')
        imgop.write_image('screen.png', blue_values)
        img1 = imgop.extracting_blue('encodedscreen.png')
        self.assertEqual(blue_values, img1)


if __name__ == '__main__':
    unittest.main()