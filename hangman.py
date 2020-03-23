from person import array
from randomwordgenerator import randomwordgenerator
from random import choice


def get_word(): return randomwordgenerator.generate_random_words(n=1)


def play_game(word):

    lives = 6
    index = 0
    
    notLost = True
    dashes = ["-" for _ in range(len(word))]
    print("Welcome to Hangman - Terminal Edition!!!")
    print("---------------------------------------------")
    print(f"LIVES LEFT: {lives}")
    print(array[6-lives])
    print('\n')

    while lives > 1:
        print(index)
        
        print(f"LIVES:{lives}")
        
        letter = input(f"GUESS A LETTER: {''.join(dashes)} ")
        print(f"{len(letter)} is the length of your input")
        if len(letter) > 1 or len(letter) == 0:
            print("Not a valid letter.")
            print(f"LIVES LEFT: {lives}")

            print(array[6-lives])
            print('\n')
       
        print(len(letter))
        if letter.upper() not in word and len(letter) == 1:
            index += 1
            lives -= 1
            print("---------------------------------------------")
            print("Incorrect letter.")
            print(f"LIVES LEFT: {lives}")

            print(array[6-lives])
            print('\n')
      
        elif letter.upper() in word and len(letter) == 1:
            print("---------------------------------------------")
            print("Correct letter!")
            print(f"LIVES LEFT: {lives}")
            print(array[6-lives])
            print('\n')
            print(word.index(letter.upper()))
            dashes[word.index(letter.upper())] = letter.upper()
            print(word.count(letter.upper()))

            if dashes[word.index(letter.upper())] == letter.upper() and word.count(letter.upper()) > 1:
                mod_string = ''.join([word[i] for i in range(
                    len(word)) if i != word.index(letter.upper())])
                for i in range(word.count(letter.upper())):    
                    if letter.upper() in mod_string:
                        print("---------------------------------------------")
                        print("Correct letter!")
                        print(f"LIVES LEFT: {lives}")
                        print(array[6-lives])
                        print('\n')
                        print(word.index(letter.upper()))
                        dashes[mod_string.index(
                            letter.upper())+1] = letter.upper()
                        print(word.count(letter.upper()))

                    else:
                        index += 1
                        lives -= 1
                        print("---------------------------------------------")
                        print("Incorrect letter.")
                        print(f"LIVES LEFT: {lives}")
                        print(array[6-lives])
                        print('\n')
        if ''.join(dashes) == word:
            print("\n Congratulations! You guessed the word!")
            break
        elif lives == 1:
            print(f"You lost! The word was {word}. Maybe next time.")
            
    print(''.join(dashes))

def play():
    word = get_word().upper()
    play_game(word)

    while input("Would you like to play again? (Y/N) > ").lower() == "y":
        word = get_word().upper()
        play_game(word)        
play()
