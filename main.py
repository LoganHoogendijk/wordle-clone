import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

answer = random.choice(words)
print(answer)

#🟩🟨🟥⬛
tries = 6
while tries > 0:
    j = 0
    guess = input("Guess a word: ")
    if guess == answer:
        print("🟩 🟩 🟩 🟩 🟩")
        print("You have won.")
        break
    elif len(guess) == 5:
        tries-=1
        print("You have", tries, "tries left")
        boxes = {i: '⬛' for i in range(5)}
        for i in guess:
            if i == answer[j]:
                boxes[j] = '🟩'
            elif i in answer:
                boxes[j] = '🟨'
            j+=1
        print(' '.join(boxes.values()))
    else:
        print("Please enter a 5 letter word")





