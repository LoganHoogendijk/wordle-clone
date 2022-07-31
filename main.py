import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

guess = random.choice(words)
