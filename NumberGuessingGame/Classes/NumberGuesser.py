"""
Program: NumberGuesser
Last Modified: 07/14/2020

Program define the NumberGuesser class.
"""

class NumberGuesser():
    '''NumberGuesser class constructor'''

    '''NumberGuesser class constructor:
    :guessed_list: empty list to be filled with user guesses, optional: list
    Returns: NumberGuesser object'''
    def __init__(self, randomNum, guessedList=[]):
        self._randomNum = randomNum
        self._guessedList = guessedList

    '''add_guess:
    :user_guess: integer guess by user that is added to guess_list, required: int
    Returns: N/A'''
    def add_guess(self, userGuess):
        self._guessedList.append(userGuess)

    def make_guess(self, userGuess):
        if userGuess == self._randomNum:
            return True
        else:
            self.add_guess(userGuess)
            return False

if __name__ == '__main__':
    pass