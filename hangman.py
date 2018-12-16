 #import random for choosing word
import random 
def chooseWord():
	 # my list of words
    word_list = ["ronnie","spiraling","stratosphere","ligma","wig","peppermint","furries","informatics","hello","nyoom","oatmeal","roddent"]
    return random.choice(word_list) #return a random selection from the list

def printObscured(obscured):
    for letter in obscured: #for each character in the obscured string
        print(letter+" ",end="") #print the character and a space
    print()    
    
def validInput(user_input):
    return len(user_input) == 1 and str.isalpha(user_input) #if the user input is of length 1 and is alphabetic


def main():
    word = chooseWord() #choose a word
    obscured = "_"*len(word) #create the obscured string based on the length of the word
    gameOver = False #game initially not over
    success = False #assume game was not successful
    guesses = 0 #intitially 0 guesses
    while not gameOver: #as long as the game is not over, enter loop
        guesses+=1 #increment guesses
        print("Current Board: ",end="")
        printObscured(obscured) #print the current board
        guess = input("Guess a letter: ").lower() #get the lowe case version of the user guess
        while 1: #loop until break
            if validInput(guess): #if the input is valid
                break #break loop
            guess = input("Enter a valid, single letter guess").lower() #request new input