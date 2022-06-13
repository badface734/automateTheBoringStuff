import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):

        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)


if __name__ == '__main__':
    unittest.main()


    def test_divide(self):

# https://www.youtube.com/watch?v=6tNS--WetLI
# tutorial video followed to make this. v useful for the future