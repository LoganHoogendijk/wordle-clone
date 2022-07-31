import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

answer = random.choice(words)

tries = 6
guesses = {}
boxes = {}
finalboxes = []
finalguesses = []
while tries > 0:
    j = 0
    guess = input("\nGuess a word: ")
    if not guess.isalpha():
        print("Please only use letters")
    else:
        guess = guess.lower()
        if guess == answer:
            finalboxes.append('🟩 🟩 🟩 🟩 🟩')
            finalguesses.append(' '.join(answer))
            print("\nCongratulations! You won! 🎉\n")
            final = "\n".join("{} {}".format(x, y) for x, y in zip(finalboxes, finalguesses))
            print(final)
            break
        elif len(guess) == 5:
            tries -= 1
            for i in range(5):
                boxes[i] = '⬛'
                guesses[i] = '_'
            for x in guess:
                if x == answer[j]:
                    boxes[j] = '🟩'
                    guesses[j] = x
                elif x in answer and answer.count(x) >= guess.count(x):
                    boxes[j] = '🟨'
                    guesses[j] = x
                j += 1
            finalboxes.append(' '.join(boxes.values()))
            finalguesses.append(' '.join(guesses.values()))
            print(' '.join(boxes.values()))
            print('', '  '.join(guesses.values()))
            print("You have", tries, "tries left")
        else:
            print("Please enter a 5 letter word")
if tries == 0:
    print("\nYou lost! 🙁")
    final = "\n".join("{} {}".format(x, y) for x, y in zip(finalboxes, finalguesses))
    print(final)
    print("The correct word was:", answer)




