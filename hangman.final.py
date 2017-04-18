import random
import time
import datetime
from datetime import date

a = random.randint(1, 183)

with open("countries_and_capitals.txt", "r") as file: #otwieramy plik
    biglist = [line.strip().upper() for line in file] # robimy plik "linijnym"

one = biglist[a] # jeden element duzej listy

countrywithcapital = one.split(' | ') #dzielimy elementy na przed "|" i po |

country = countrywithcapital[0] #panstwo
capital = countrywithcapital[1] #stolica

import random

print("Welcome to Hangman! It's capital quiz. Try to quess the capital below:")
print(capital)

hangman=['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 =========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''','''
    +---+
    |   |
    O   |
        |
        |
        |
 =========''']





score=0
maxbad = 0 #maksymalna illosc bledow
withdash = "-" * len(capital) # "dashes" naszego slowa
bad = 5 #proby
usedwords = [] #slowa ktore juz byli uzywane
start = int(time.time()) # czas zaczyna swoj start

def welcome_tekst(withdash, usedwords, bad):
    print("Capital :", withdash)
    print("You have entered the next valuables: ", usedwords)
    print("Your lifes:", bad)

def trial_input(usedwords):
    trial = input("Enter letter or word: ")
    trial = trial.upper()
    usedwords.append(trial)
    return trial

def score_count_plus(trial, capital, score):
    if (trial in capital) and len(trial) < 2: # <2 po to zeby rozpoznowal klikniecie liter po jedyncze
        print("\nYes!", trial, "is in the word!")
        score+=1
        new = ""
    return score

def score_count_minus(trial, bad):
    if len(trial) < 2:
        print("\n Sorry,", trial, "isn't in the word.")
        print(hangman[bad - 1])
        bad -= 1
    return bad

def dashes(capital, trial, withdash):
    new=""
    for i in range(len(capital)):
        if trial == capital[i]:     #jak piszemy dobra litere to ona sie dodaje w dashes, rowniez jak jest kilka takich liter w slowie oni sie otworza.
            new += trial
        else:
            new += withdash[i] #zostawiamy taki samy dash
    withdash = new
    return withdash

while (bad != maxbad) and (withdash != capital):
    import random

    welcome_tekst(withdash, usedwords, bad)
    trial = trial_input(usedwords)
    withdash = dashes(capital, trial, withdash)
    score = score_count_plus(trial,capital,score)
    bad = score_count_minus(trial, bad)




    #else:


    if bad == maxbad:
        Ender = int(time.time())
        dif = int((Ender - start))
        print("It took you", dif, "sec")
        print(hangman[0])
        print("You lost!")
        y = open("scores.txt", "r")
        print(y)
        break

    if bad == 1:
        print("This is capital of ", country)

        # print(countr[cities.index(capital)])   - jak bysmy mieli 2 listy

    if capital == withdash or trial == capital:
        Ender = int(time.time())
        dif = int((Ender - start))
        k = bad - 5
        if k == 0:
            print('''You quessed so fast! \nYou quessed right\nThe capital is ''', capital, '''\nCongratulations!
            \n It took you''', dif, '''sec \n ''')

            score += 20
            now1 = date.today()

            name = input("What's your name?")

            score1 = str(("%s |" % name, now1, "| time:", dif, "| score:", score, "| guessed word:", capital))
            print("%s |" % name, str(now1), "| time:", dif, "| score:", score, "| guessed word:", capital)

            with open("scores.txt", "a") as text_file:
                text_file.write(score1 + "\n")
            a = open("scores.txt", "r")
            print(a.read())

            print("Would you like play again?")
            a = input()
            if a == "yes":
                import random

                a = random.randint(1, 183)
                one = biglist[a]

                countrywithcapital = one.split(' | ')

                country = countrywithcapital[0]
                capital = countrywithcapital[1]
                bad = 5
                maxbad = 0
                withdash = "-" * len(capital)
                usedwords = []
            else: break

        else:
            print('''\nYou quessed right\n The capital is ''',capital, ''' Congratulations!\n
It took you''', dif, '''sec\n''')

            now1 = date.today()

            name = input("What's your name?")

            score1 = str(("%s |" % name, now1, "| time:", dif, "| score:", score, "| guessed word:", capital))
            print("%s |" % name, str(now1), "| time:", dif, "| score:", score, "| guessed word:", capital)

            with open("scores.txt", "a") as text_file:
                text_file.write(score1 + "\n")

            print("Would you like play again?")

            a = input()

            if a == "yes":
                import random

                a = random.randint(1, 183)
                one = biglist[a]

                countrywithcapital = one.split(' | ')

                country = countrywithcapital[0]
                capital = countrywithcapital[1]
                bad = 5
                maxbad = 0
                withdash = "-" * len(capital)
                usedwords = []
            else:
                break
