import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

answer = random.choice(words)
answer = 'snail'

#🟩🟨🟥⬛
tries = 6
finalboxes = []
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
        boxes = {i: '⬛' for i in range(5)}
        for i in guess:
            if i == answer[j]:
                boxes[j] = '🟩'
            elif i in answer:
                boxes[j] = '🟨'
            j+=1
        finalboxes.append(' '.join(boxes.values()))
        print(' '.join(boxes.values()))
        print("You have", tries, "tries left")
    else:
        print("Please enter a 5 letter word")
    





