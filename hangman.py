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
