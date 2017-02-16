"""Assignment 1: More practice with python concepts

1. Random Numbers

Generate a random number between 1 and 99 (including 1 and 99). Ask  the user to guess the number using Python's input console. Then tell them whether they guessed too  low, too high, or exactly right. 
Assumptions:

    Use built in functions to get python input 
    The game can run for ever until a user types “exit”
    Count how many guesses the user has taken, and when the game ends, print this out.

Further optimisation: 

    In order to be able to generate random numbers you have imported a "module". 
    After your first working draft try to organise better your code by creating your "own" module.



2. List Overlaps.
Take three lists, say for example these two: 

       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 98]

       b = [98, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

       c = [1, 2, 3, 3, 3, 4, 5, 98]

Write a program that returns a list that contains only the  elements that are common among all lists (without duplicates). Make  sure your program works on lists of different sizes. Test it also with random generated lists with numbers between 1 - 9.


3. Text to International Civil Aviation Organization (ICAO) alphabet 
ICAO assigns code words to the letters of the English alphabet  acrophonically (Alfa for A, Bravo for B, Charlie for C, etc.) so that critical  combinations of letters (and numbers) can be pronounced and understood  by those who transmit and receive voice messages by radio or telephone  regardless of their native language, especially when the safety of  navigation or persons is essential. A Python dictionary is given to you covering  one version of the ICAO alphabet.

Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken ICAO words. You need to import at least two libraries: os and time.  

Further optimisation:
On a mac, you have access to the system TTS (Text-To-Speech) as follows: os.system('say ' + msg), where msg  is the string to be spoken. (Under UNIX/Linux and Windows, something  similar might exist.) Apart from the text to be spoken, your procedure  also needs to accept two additional parameters: a float indicating the  length of the pause between each spoken ICAO word, and a float  indicating the length of the pause between each word spoken. """

#exercise 1. Write your code here
import random
import sys

guessesTaken = 0
print("EXERCISE 1 \n")
number = random.randint(1, 99)
print('number picked for test: ' , number)
print('to exit the game type: exit')

while guessesTaken > -1:
  print('pick a number between 1 and 99')
  guess = input()
  exit_game = 'exit'
  
  if guess == exit_game:
    sys.exit()
  guess = int(guess)

  guessesTaken = guessesTaken + 1

  if guess < number:
    print('Your guess is too low.') 

  if guess > number:
    print('Your guess is too high.')

  if guess == number:
    break

if guess == number:
  print('Good job you guessed the right number in ' , guessesTaken , ' guesses! \n')




#exercise 2. List comprehensions may be useful for this exercise. See below:
# x = [1, 2, 3]
# y = [5, 10, 15]
# xAndYProducts = [a*b for a in x for b in y]
print("EXERCISE 2 \n")
from collections import Counter
from itertools import chain
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 98]
b = [98, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = [1, 2, 3, 3, 3, 4, 5, 98]
list_count = [a,b,c]
list_random_gen=[random.randrange(2,10,1) for _ in range (random.randint(10,20))]

counts = Counter(chain.from_iterable(list_count))
print (counts, "\n")
counts_random_gen = Counter(list_random_gen)
print ("New random list: ", list_random_gen)
print (counts_random_gen, "\n")

#exercise 3
print("EXERCISE 3 \n")
import time, os
from string import punctuation

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
	 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
	 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
	 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
	 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
	 'z':'zulu'}

def icao(txt, icao_pause=1, word_pause=3):
    words = txt.split() 

    for word in words: 
        for char in word: 
            if char not in punctuation: 
                print(d[char.lower()])
                time.sleep(icao_pause) 
    time.sleep(word_pause) 
icao("hello")
