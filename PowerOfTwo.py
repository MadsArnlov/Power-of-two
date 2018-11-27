# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:52:06 2018

@author: arnlo
"""
import sys
import numpy as np
import time

amount_of_time = 60


def easy():
    start = time.time()
    infile = open("Record.txt", "r")
    record = eval(infile.read())
    infile.close()

    correct = 0
    k = 2
    a = 2
    b = 2
    x = 0

    while x is not None:
        PowerOfTwo = a**b
        current_time = time.time() - start
        if current_time <= amount_of_time:
            s = input("What is {}*{} = ".format(k, a))
            if s is not "":
                x = eval(s)
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    correct += 1
                    b += 1
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if correct > record:
                        with open("Record.txt", "w") as output:
                            output.write("{}".format(correct))
                        print("You broke your record! Your new record is {}, and the old record was {}.".format(correct, record))
                    userInput = input("Do you want to play again? (Y/N) = ").upper()
                    if userInput == "N":
                        break
                    elif userInput == "Y":
                        difficulty()
                        break
                    else:
                        break
            k = PowerOfTwo
        else:
            print("You have run out of time! You got {} correct answers in {:.2f} seconds".format(correct - 1, current_time))
            break


def medium():
    start = time.time()
    infile = open("Record.txt", "r")
    record = eval(infile.read())
    infile.close()

    correct = 0
    k = 2
    a = 2
    b = 2
    x = 0

    while x is not None:
        PowerOfTwo = a**b
        current_time = time.time() - start
        if current_time <= amount_of_time:
            s = input("What is {}*{} = ".format(PowerOfTwo/2, a))
            if s is not "":
                x = eval(s)
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    correct += 1
                    b += 2
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if correct > record:
                        with open("Record.txt", "w") as output:
                            output.write("{}".format(correct))
                        print("You broke your record! Your new record is {}, and the old record was {}.".format(correct, record))
                    userInput = input("Do you want to play again? (Y/N) = ").upper()
                    if userInput == "N":
                        break
                    elif userInput == "Y":
                        difficulty()
                        break
                    else:
                        break
            k = PowerOfTwo
        else:
            print("You have run out of time! You got {} correct answers in {:.2f} seconds".format(correct - 1, current_time))
            break


def hard():
    start = time.time()
    infile = open("Record.txt", "r")
    record = eval(infile.read())
    infile.close()

    correct = 0
    k = 2
    a = 2
    b = 2
    x = 0

    while x is not None:
        PowerOfTwo = a**b
        current_time = time.time() - start
        if current_time <= amount_of_time:
            s = input("What is {:.0f}*{} = ".format(PowerOfTwo/2, a))
            if s is not "":
                x = eval(s)
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    correct += 1
                    b += 4
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if correct > record:
                        with open("Record.txt", "w") as output:
                            output.write("{}".format(correct))
                        print("You broke your record! Your new record is {}, and the old record was {}.".format(correct, record))
                    userInput = input("Do you want to play again? (Y/N) = ").upper()
                    if userInput == "N":
                        break
                    elif userInput == "Y":
                        difficulty()
                        break
                    else:
                        break
            k = PowerOfTwo
        else:
            print("You have run out of time! You got {} correct answers in {:.2f} seconds".format(correct - 1, current_time))
            break


def difficulty():
    difficulty = input("What difficulty do  you want to play? easy/medium/hard = ").upper()
    if difficulty == "EASY":
        easy()
    elif difficulty == "MEDIUM":
        medium()
    elif difficulty == "HARD":
        hard()


difficulty()

#if len(sys.argv) == 2:
#    if sys.argv[1] == "easy":
#        easy()
#    elif sys.argv[1] == "medium":
#        medium()
#    elif sys.argv[1] == "hard":
#        hard()