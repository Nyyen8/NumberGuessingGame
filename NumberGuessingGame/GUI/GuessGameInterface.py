"""
Program: GuessGameInterface.py
Author: Paul Elsea
Last Modified: 07/14/2020

Program to display a GUI for a number guessing game.
"""

import tkinter
import random
from NumberGuessingGame.Classes import NumberGuesser as ng

def chose_start():
    newNum = random.randrange(1, 12)
    global newGameObj
    newGameObj = ng.NumberGuesser(newNum)

def chose_one():
    test_guess(1)

def chose_two():
    test_guess(2)

def chose_three():
    test_guess(3)

def chose_four():
    test_guess(4)

def chose_five():
    test_guess(5)

def chose_six():
    test_guess(6)

def chose_seven():
    test_guess(7)

def chose_eight():
    test_guess(8)

def chose_nine():
    test_guess(9)

def chose_ten():
    test_guess(10)

def chose_eleven():
    test_guess(11)

def chose_twelve():
    test_guess(12)

def test_guess(guess):
    if newGameObj.make_guess(guess):
        guessPromptLabel.config(text='Bingo!')
    else:
        guessPromptLabel.config(text='Sorry, try again.')

'''Defining gui object'''
GuessGameInterface = tkinter.Tk()
GuessGameInterface.title('Guess My Number')
currentNum = random.randrange(1, 12)
newGameObj = ng.NumberGuesser(currentNum)

'''Defining start/reset button'''
startButton = tkinter.Button(GuessGameInterface, text='Start new game.', width=25, command=chose_start)\
    .grid(row=0, column=1)

'''Defining buttons for each guess'''
oneButton = tkinter.Button(GuessGameInterface, text='1', width=25, command=chose_one).grid(row=2, column=0)
twoButton = tkinter.Button(GuessGameInterface, text='2', width=25, command=chose_two).grid(row=2, column=1)
threeButton = tkinter.Button(GuessGameInterface, text='3', width=25, command=chose_three).grid(row=2, column=2)
fourButton = tkinter.Button(GuessGameInterface, text='4', width=25, command=chose_four).grid(row=3, column=0)
fiveButton = tkinter.Button(GuessGameInterface, text='5', width=25, command=chose_five).grid(row=3, column=1)
sixButton = tkinter.Button(GuessGameInterface, text='6', width=25, command=chose_six).grid(row=3, column=2)
sevenButton = tkinter.Button(GuessGameInterface, text='7', width=25, command=chose_seven).grid(row=4, column=0)
eightButton = tkinter.Button(GuessGameInterface, text='8', width=25, command=chose_eight).grid(row=4, column=1)
nineButton = tkinter.Button(GuessGameInterface, text='9', width=25, command=chose_nine).grid(row=4, column=2)
tenButton = tkinter.Button(GuessGameInterface, text='10', width=25, command=chose_ten).grid(row=5, column=0)
elevenButton = tkinter.Button(GuessGameInterface, text='11', width=25, command=chose_eleven).grid(row=5, column=1)
twelveButton = tkinter.Button(GuessGameInterface, text='12', width=25, command=chose_twelve).grid(row=5, column=2)

'''Defining guess_prompt label'''
guessPromptLabel = tkinter.Label(GuessGameInterface, text='Please pick a number from 1 to 12.')
guessPromptLabel.grid(row=1, column=1)

'''Defining button to exit program'''
exitButton = tkinter.Button(GuessGameInterface, text='Exit', width=25, command=GuessGameInterface.destroy).\
    grid(row=6, column=1)

'''Loop to wait for input'''
GuessGameInterface.mainloop()