import random

with open('wordsGuess.txt') as f:
    words = [line.rstrip() for line in f]

answer = random.choice(words)

with open('words.txt') as wordF:
    validWords = [line.rstrip() for line in wordF]


tries = 6
guesses = {}
boxes = {}
finalboxes = []
allguesses = []
wrongLetters = []
while tries > 0:
    j = 0
    guess = input("\nGuess a word: ")
    if guess in validWords:
        guess = guess.lower()
        if guess == answer:
            finalboxes.append('🟩 🟩 🟩 🟩 🟩')
            allguesses.append(' '.join(guess))
            print("\nCongratulations! You won! 🎉\n")
            final = "\n".join("{} {}".format(x, y) for x, y in zip(finalboxes, allguesses))
            print(final)
            break
        else:
            tries -= 1
            allguesses.append(' '.join(guess))
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
                else:
                    if x not in wrongLetters:
                        wrongLetters.append(x)
                j += 1
            finalboxes.append(' '.join(boxes.values()))
            print(' '.join(boxes.values()))
            print('', '  '.join(guesses.values()))

            print("These letters are not in the word: ", end='')
            for letter in sorted(wrongLetters):
                print(letter, '', end='')
            print("\nYou have", tries, "tries left")
    else:
        print("Please enter a valid 5 letter word")
if tries == 0:
    print("\nYou lost! 🙁")
    final = "\n".join("{} {}".format(x, y) for x, y in zip(finalboxes, allguesses))
    print(final)
    print("The correct word was:", answer)




