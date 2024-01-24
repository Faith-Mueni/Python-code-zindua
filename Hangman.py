import random

def get_random_word_from_wordlist ():
    wordlist = []

    with open ("playwords.txt", r) as file:
        wordlist = file.read () .split ("\n")

        word = random.choice (wordlist)
        return word

def get_some_letters (word):
    letters = []
    temp = '_' * len(word)

    for char in list (word):
        if char not in letters:
            letters.append(char)

    character = random.choice (letters)

    for num, char in enumarate (list(word)):
        if char == character:
            templist = list (temp)
            templist [num] = char
            temp = ''.join (templist)

    return temp

def draw_hangman (chances):
    if chances == 6:
        print ("_______")
        print ("|  |")
        print ("|")
        print ("|")
        print ("|")

    elif chances == 5:
        print ("______")
        print ("|   |")
        print ("|   0")
        print ("|")
        print ("|")

    elif chances == 4:
        print ("______")
        print ("|   |")
        print ("|   0")
        print ("|   /")
        print ("|")
        print ("|")

    elif chances == 3:
        print ("_______")
        print ("|    |")
        print ("|    0")
        print ("|   /|")
        print ("|     ")

    elif chances == 2:
        print ("_______")
        print ("|    |")
        print ("|    0")
        print ("|   /|\ ")
        print ("|     ")

    elif chances == 1:
        print ("________")
        print ("|      |")
        print ("|      0")
        print ("|     /|\ ")
        print("|       /")

    elif chances ==0:
        print ("_________")
        print ("|       |")
        print ("|       0")
        print ("|      /|\ ")
        print ("|      /\ ")

def start_hangman_game ():
    word = get_random_word_from_wordlist ()
    temp = get_some_letters (word)
    chances = 7
    found = False

    while True:
        if chance == 0:
            print (f"better luck next time")
            break

        print ("=== Guess the word===")
        print (temp, end='')
        print (f"/t (word has {len (word)} letters) " )
        print (f"chances left: {chances}")
        character = input ("enter the character you think the word may have:")

        if len (character) > 1 or not character.isalpha ():
            print ("please enter a single alphabet only")
            continue

        else:
            for num, char in enumerate (list (word)):
                if char == character:
                    templist = list (temp)
                    templist[num] = char
                    temp = ''.join (templist)
                    found = True

            if found:
                found = False
            else:
                chances = 1
            if '_' not in temp:
                print (f"\nYou won! The word was: {word}")
                print (f"you got it in {7-chances}guess")
                break
            else:
                draw_hangman (chances)

            print ()











