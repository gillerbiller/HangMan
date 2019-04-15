import random
word = ""
wordDict = {}
listOfUnderscores=[]
chances = 0
sequence_of_guessed_letters = []
def setup():
    global word
    global sequence_of_guessed_letters
    word = (random.choice(["pop", "under", "garden", "pie", "happy", "awkward"
    ,"bookkeeper"]))
    def key_value():
        for x in range(len((word))):
            if word[x] in wordDict.keys():
                wordDict[word[x]].append(x)
            else:
                wordDict[word[x]] = [x]
        return (wordDict)
    key_value()
    for i in range(len(word)):
        listOfUnderscores.append("_")

def play_game():
    global sequence_of_guessed_letters
    #Only use words that are 3 or more letters to ensure that legs are drawn
    while chances < len(word)+4:
        print(listOfUnderscores)
        potential_letter = input("Please choose a letter: ")
        sequence_of_guessed_letters.append(potential_letter)
        if potential_letter in wordDict.keys():
            win(potential_letter)
            did_we_win = ("_" not in listOfUnderscores)
            if did_we_win ==True:
                break
        else:
            lose()
def win(potential_letter):
    print("Hooray! That is a letter in the word!")
    global chances
    locations_of_potential_letter = wordDict[potential_letter]
    for location in locations_of_potential_letter:
        listOfUnderscores[location] = potential_letter
    chances = chances + 1

def lose():
    global chances
    bodyPart = listOfBodyParts[chances]
    print("Wrong! " + bodyPart + " drawn.")
    chances = chances + 1

listOfBodyParts = ["Head","Torso","Left Arm", "Right Arm", "Left Leg", "Right Leg",
"Left Hand", "Right Hand", "Left Foot", "Right Foot", "Left Eye", "Right Eye",
"Left Ear", "Right Ear", "Nose", "Mouth", "The Secret Bits", "BellyButton", "Hair",
"Left Fingers", "Right Fingers", "Left Toes", "Right Toes", "Left Eyebrow",
"Right Eyebrow"]

class HangmanGame(object):
    def __init__(self, win, word, sequence_of_guessed_letters):
        self.win =win
        self.word = word
        self.sequence_of_guessed_letters = sequence_of_guessed_letters

    def __str__(self):
        output= "This game "
        if self.win:
            output += "was won."
        else:
            output+= "was lost."
        output+= " The word we were trying to guess was "
        output += self.word +"."
        output+=" We guessed the following sequence of letters: "
        for letter in sequence_of_guessed_letters:
            output += " "+letter+","
        return output


def create_game_record():
    did_we_win = ("_" not in listOfUnderscores)

    game = HangmanGame(did_we_win, word, sequence_of_guessed_letters)
    print(game)

def game():
    setup()
    play_game()
    create_game_record()

game()
