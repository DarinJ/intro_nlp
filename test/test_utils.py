import unittest
import utils
class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual( utils.multiply(2,5), 10)

if __name__ == '__main__':
    unittest.main()
