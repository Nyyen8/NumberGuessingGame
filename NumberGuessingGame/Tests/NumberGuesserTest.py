import unittest
from NumberGuessingGame.Classes import NumberGuesser as ng


class NumberGuesser_class_tests(unittest.TestCase):
    '''Function to construct test object'''
    def setUp(self):
        self.guessTestObject = ng.NumberGuesser(6)
        self.guessTestObjectFull = ng.NumberGuesser(6, [1,2,3])

    '''Function to delete test object'''
    def tearDown(self):
        del self.guessTestObject
        del self.guessTestObjectFull

    '''Test to ensure attribute is being properly applied, and optional attribute not required'''
    def test_object_created_required_attributes(self):
        self.assertEqual(self.guessTestObject._randomNum, 6)

    '''Test to ensure attribute is being properly applied and optional attribute also applied correctly'''
    def test_object_created_all_attributes(self):
        self.assertEqual(self.guessTestObjectFull._randomNum, 6)
        self.assertEqual(self.guessTestObjectFull._guessedList, [1,2,3])

    '''Test to ensure add_guess function working properly'''
    def test_add_guess_func(self):
        self.guessTestObject.add_guess(1)
        self.guessTestObject.add_guess(2)
        self.guessTestObject.add_guess(3)
        self.assertEqual(self.guessTestObjectFull._guessedList, [1, 2, 3])



if __name__ == '__main__':
    unittest.main()
