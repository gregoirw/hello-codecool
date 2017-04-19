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
    print("\nYes!", trial, "is in the word!")
    score+=1
    new = ""
    return score

def score_count_minus(trial, bad):
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

def if_lost(maxbad,bad, time, start):
    Ender = int(time.time())
    dif = int((Ender - start))
    print(hangman[0])
    print("You lost!")
    print("It took you", dif, "sec")
    y = open("scores.txt", "r")
    print(y)

def guessing_after_first_shot(time,start):
    Ender = int(time.time())
    dif = int((Ender - start))
    k = bad - 5
    return k
def congrats_for_quick_answer(score):
    Ender = int(time.time())
    dif = int((Ender - start))
    print('''You quessed so fast! \nYou quessed right\nThe capital is ''', capital, '''\nCongratulations!
    \n It took you''', dif, '''sec \n ''')

    score += 20
def name_and_score_saving():
    now1 = date.today()
    Ender = int(time.time())
    dif = int((Ender - start))

    name = input("What's your name?")

    score1 = str(("%s |" % name, now1, "| time:", dif, "| score:", score, "| guessed word:", capital))
    print("%s |" % name, str(now1), "| time:", dif, "| score:", score, "| guessed word:", capital)

    with open("scores.txt", "a") as text_file:
        text_file.write(score1 + "\n")
    a = open("scores.txt", "r")
    print(a.read())

def playing_again(country, capital, bad, maxbad, withdash, usedwords):
    a = random.randint(1, 183)

    with open("countries_and_capitals.txt", "r") as file: #otwieramy plik
        biglist = [line.strip().upper() for line in file] # robimy plik "linijnym"

    one = biglist[a]

    countrywithcapital = one.split(' | ')

    country = countrywithcapital[0]
    capital = countrywithcapital[1]
    bad = 5
    maxbad = 0
    withdash = "-" * len(capital)
    usedwords = []
    return country, capital, bad, maxbad, withdash, usedwords

while (bad != maxbad) and (withdash != capital):
    import random

    welcome_tekst(withdash, usedwords, bad)
    trial = trial_input(usedwords)

    if (trial in capital) and len(trial) < 2:
        score = score_count_plus(trial,capital,score)
        withdash=dashes(capital, trial, withdash)
    else:
        if len(trial) < 2:
            bad = score_count_minus(trial, bad)
    if bad == maxbad:
        if_lost(maxbad, bad, time, start)
    if bad == 1:
        print("This is capital of ", country)
    if capital == withdash or trial == capital:
        k = guessing_after_first_shot(time, start)
        if k == 0:
            congrats_for_quick_answer(score)
            name_and_score_saving()
            answer = input("Would you like play again?")
            if answer == "yes":
                country, capital, bad, maxbad, withdash, usedwords = playing_again(country, capital, bad, maxbad, withdash, usedwords)
            else:
                break
        else:
            print('''\nYou quessed right\n The capital is ''',capital, ''' Congratulations!\n
It took you''', dif, '''sec\n''')
            name_and_score_saving()
            answer = input("Would you like play again?")
            if answer == "yes":
                country, capital, bad, maxbad, withdash, usedwords = playing_again(country, capital, bad, maxbad, withdash, usedwords)
            else:
                break
