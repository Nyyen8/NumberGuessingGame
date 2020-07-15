"""
Program: NumberGuesser
Last Modified: 07/14/2020

Program define the NumberGuesser class.
"""

class NumberGuesser():
    '''NumberGuesser class constructor:
    :randomNum arg: random number, required: int
    :guessedList arg: empty list to be filled with user guesses, optional: list
    Returns: NumberGuesser object'''
    def __init__(self, randomNum, guessedList=[]):
        self._randomNum = randomNum
        self._guessedList = guessedList

    '''add_guess function
    Adds user guess to guessedList trait of the NumberGuesser object for this game.
    :user_guess arg: integer guess by user that is added to guess_list, required: int
    Returns: N/A'''
    def add_guess(self, userGuess):
        self._guessedList.append(userGuess)

    '''make guess function
    Checks user guess against random number.
    :user_guess: integer guess by user that is added to guess_list, required: int
    Returns: True if correct, False if not.'''
    def make_guess(self, userGuess):
        if userGuess == self._randomNum:
            return True
        else:
            self.add_guess(userGuess)
            return False


if __name__ == '__main__':
    pass