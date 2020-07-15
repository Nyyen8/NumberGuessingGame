"""
Program: GuessGameInterface.py
Author: Paul Elsea
Last Modified: 07/14/2020

Program to display a GUI for a number guessing game.
"""

import tkinter as tk
from tkinter import messagebox as mb
import random
from NumberGuessingGame.Classes import NumberGuesser as ng

'''chose_start function:
Called with startButton. Call restart_game function.
Returns: N/A.'''
def chose_start():
    restart_game()

'''restart_game function:
Modifies existing game object and updates it with a new random number. Resets all buttons to be in normal state again.
Returns: N/A.'''
def restart_game():
    newNum = random.randrange(1, 13)
    global newGameObj
    newGameObj._guessedList.clear()
    guessPromptLabel.config(text = 'Please pick a number from 1 to 12')
    guessesLabel.config(text='')
    newGameObj = ng.NumberGuesser(newNum)
    oneButton['state'] = tk.NORMAL
    twoButton['state'] = tk.NORMAL
    threeButton['state'] = tk.NORMAL
    fourButton['state'] = tk.NORMAL
    fiveButton['state'] = tk.NORMAL
    sixButton['state'] = tk.NORMAL
    sevenButton['state'] = tk.NORMAL
    eightButton['state'] = tk.NORMAL
    nineButton['state'] = tk.NORMAL
    tenButton['state'] = tk.NORMAL
    elevenButton['state'] = tk.NORMAL
    twelveButton['state'] = tk.NORMAL


'''chose_* functions:
Call test_guess function with integer chosen by the button that called it.
Returns: N/A.'''
def chose_one():
    test_guess(1, oneButton)

def chose_two():
    test_guess(2, twoButton)

def chose_three():
    test_guess(3, threeButton)

def chose_four():
    test_guess(4, fourButton)

def chose_five():
    test_guess(5, fiveButton)

def chose_six():
    test_guess(6, sixButton)

def chose_seven():
    test_guess(7, sevenButton)

def chose_eight():
    test_guess(8, eightButton)

def chose_nine():
    test_guess(9, nineButton)

def chose_ten():
    test_guess(10, tenButton)

def chose_eleven():
    test_guess(11, elevenButton)

def chose_twelve():
    test_guess(12, twelveButton)


'''test_guess function:
:guess argument: integer user chose using calling button, required: int
:button argument: button calling function, required: button object
Returns: Disables button if guess was incorrect, or displays message box where user can decided to reset the game
or quit.'''
def test_guess(guess, button):
    if newGameObj.make_guess(guess):
        if mb.askyesno(title='You Won!', message='Go again?'):
            restart_game()
        else:
            quit()
    else:
        button['state'] = tk.DISABLED
        guessPromptLabel.config(text='You have guessed:')
        guessesLabel.config(text=str(newGameObj._guessedList))

'''Defining gui object'''
GuessGameInterface = tk.Tk()
GuessGameInterface.title('Guess My Number')

'''Defining random number'''
currentNum = random.randrange(1, 13)

'''Defining game object with random number'''
newGameObj = ng.NumberGuesser(currentNum)

'''Defining start/reset button'''
startButton = tk.Button(GuessGameInterface, text='Start new game.', width=25, command=chose_start)\
    .grid(row=0, column=1)

'''Defining buttons for each guess'''
oneButton = tk.Button(GuessGameInterface, text='1', width=25, command=chose_one, state=tk.NORMAL)
oneButton.grid(row=3, column=0)
twoButton = tk.Button(GuessGameInterface, text='2', width=25, command=chose_two, state=tk.NORMAL)
twoButton.grid(row=3, column=1)
threeButton = tk.Button(GuessGameInterface, text='3', width=25, command=chose_three, state=tk.NORMAL)
threeButton.grid(row=3, column=2)
fourButton = tk.Button(GuessGameInterface, text='4', width=25, command=chose_four, state=tk.NORMAL)
fourButton.grid(row=4, column=0)
fiveButton = tk.Button(GuessGameInterface, text='5', width=25, command=chose_five, state=tk.NORMAL)
fiveButton.grid(row=4, column=1)
sixButton = tk.Button(GuessGameInterface, text='6', width=25, command=chose_six, state=tk.NORMAL)
sixButton.grid(row=4, column=2)
sevenButton = tk.Button(GuessGameInterface, text='7', width=25, command=chose_seven, state=tk.NORMAL)
sevenButton.grid(row=5, column=0)
eightButton = tk.Button(GuessGameInterface, text='8', width=25, command=chose_eight, state=tk.NORMAL)
eightButton.grid(row=5, column=1)
nineButton = tk.Button(GuessGameInterface, text='9', width=25, command=chose_nine, state=tk.NORMAL)
nineButton.grid(row=5, column=2)
tenButton = tk.Button(GuessGameInterface, text='10', width=25, command=chose_ten, state=tk.NORMAL)
tenButton.grid(row=6, column=0)
elevenButton = tk.Button(GuessGameInterface, text='11', width=25, command=chose_eleven, state=tk.NORMAL)
elevenButton.grid(row=6, column=1)
twelveButton = tk.Button(GuessGameInterface, text='12', width=25, command=chose_twelve, state=tk.NORMAL)
twelveButton.grid(row=6, column=2)

'''Defining guess_prompt label'''
guessPromptLabel = tk.Label(GuessGameInterface, text='Please pick a number from 1 to 12')
guessPromptLabel.grid(row=1, column=1)

'''Defining guesses label'''
guessesLabel = tk.Label(GuessGameInterface, text='')
guessesLabel.grid(row=2, column=1)

'''Defining button to exit program'''
exitButton = tk.Button(GuessGameInterface, text='Exit', width=25, command=GuessGameInterface.destroy).\
    grid(row=7, column=1)

'''Loop to wait for input'''
GuessGameInterface.mainloop()