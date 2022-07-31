import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

answer = random.choice(words)
answer = 'snail'

#🟩🟨🟥⬛
tries = 6
finalboxes = []
boxes = {}
letterCount = {}
while tries > 0:
    j = 0
    guess = input("\nGuess a word: ")
    if guess == answer:
        finalboxes.append('🟩 🟩 🟩 🟩 🟩')
        print("Congratulations! You won!\n")
        for x in finalboxes:
            print(x)
        break
    elif len(guess) == 5:
        tries-=1
        for i in range(5):
            boxes[i] = '⬛'
        for x in guess:
            if x == answer[j]:
                boxes[j] = '🟩'
            elif x in answer and answer.count(x) >= guess.count(x):
                boxes[j] = '🟨'
            j+=1
        finalboxes.append(' '.join(boxes.values()))
        print(' '.join(boxes.values()))
        print("You have", tries, "tries left")
    else:
        print("Please enter a 5 letter word")
    




