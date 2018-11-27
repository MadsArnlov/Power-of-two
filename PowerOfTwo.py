# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:52:06 2018

@author: arnlo
"""

import numpy as np
import time

amount_of_time = 120


def easy():
    start = time.time()
    infile = np.genfromtxt("Record_easy.txt", delimiter=", ")
    record = infile[1]

    score = 0
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
                x = eval(s.split("*")[0])
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    score += 50
                    b += 1
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if score > record:
                        saving = np.array([user, score, "EASY"])
                        np.savetxt("Record_easy.txt", saving, fmt="%s", newline=", ")
                        print("You broke your record! The new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score, record))
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
            print("You have run out of time! You got {} Pharao points(PP) in {:.2f} seconds".format(score - 50, current_time))
            if score > record:
                saving = np.array([user, score, "EASY"])
                np.savetxt("Record_easy.txt", saving, fmt="%s", newline=", ")
                print("You broke your record! The new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score - 50, record))
            userInput = input("Do you want to play again? (Y/N) = ").upper()
            if userInput == "N":
                break
            elif userInput == "Y":
                difficulty()
                break
            else:
                break


def medium():
    start = time.time()
    infile = np.genfromtxt("Record_medium.txt", delimiter=", ")
    record = infile[1]

    score = 0
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
                x = eval(s.split("*")[0])
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    score += 100
                    b += 2
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if score > record:
                        saving = np.array([user, score, "MEDIUM"])
                        np.savetxt("Record_medium.txt", saving, fmt="%s", newline=", ")
                        print("You broke your record! The new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score, record))
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
            print("You have run out of time! You got {} Pharao points(PP) in {:.2f} seconds".format(score - 100, current_time))
            if score > record:
                saving = np.array([user, score, "MEDIUM"])
                np.savetxt("Record_medium.txt", saving, fmt="%s", newline=", ")
                print("You broke your record! The new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score - 100, record))
            userInput = input("Do you want to play again? (Y/N) = ").upper()
            if userInput == "N":
                break
            elif userInput == "Y":
                difficulty()
                break
            else:
                break


def hard():
    start = time.time()
    infile = np.genfromtxt("Record_hard.txt", delimiter=", ")
    record = infile[1]

    score = 0
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
                x = eval(s.split("*")[0])
            else:
                x = None
            if isinstance(x, int) or isinstance(x, float):
                if x == PowerOfTwo:
                    score += 300
                    b += 4
                    print("Correct!")
                else:
                    print("You made a mistake, {}*{} = {}, not {}.".format(k, a, PowerOfTwo, x))
                    if score > record:
                        saving = np.array([user, score, "HARD"])
                        np.savetxt("Record_hard.txt", saving, fmt="%s", newline=", ")
                        print("You broke your record! Your new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score, record))
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
            print("You have run out of time! You got {} Pharao points(PP) in {:.2f} seconds".format(score - 300, current_time))
            if score > record:
                saving = np.array([user, score, "HARD"])
                np.savetxt("Record_hard.txt", saving, fmt="%s", newline=", ")
                print("You broke your record! Your new record is {} Pharao points(PP), and the old record was {:.0f}.".format(score - 300, record))
            userInput = input("Do you want to play again? (Y/N) = ").upper()
            if userInput == "N":
                break
            elif userInput == "Y":
                difficulty()
                break
            else:
                break


def difficulty():
    difficulty = input("What difficulty do  you want to play? easy/medium/hard = ").upper()
    if difficulty == "EASY":
        easy()
    elif difficulty == "MEDIUM":
        medium()
    elif difficulty == "HARD":
        hard()

user = input("Username = ").upper()
difficulty()

#if len(sys.argv) == 2:
#    if sys.argv[1] == "easy":
#        easy()
#    elif sys.argv[1] == "medium":
#        medium()
#    elif sys.argv[1] == "hard":
#        hard()