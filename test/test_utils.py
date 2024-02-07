import unittest
from intro_nlp import utils
class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual( utils.multiply(2,5), 10)

    def test_negative_multiply(self):
        self.assertEqual( utils.multiply(-2,-5), 10)


if __name__ == '__main__':
    unittest.main()
