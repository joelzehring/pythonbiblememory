#### Bible Memory Game: Romans 3:23 ####
#### v 5 ####
# "For all have sinned and fall short
# of the glory of God. Romans 3:23"

import random

master_verse = ["For", "all", "have", "sinned", "and", "fall",
 "short", "of", "the", "glory", "of", "God", "Romans", "3:23"]
 
practice_verse = ["For", "all", "have", "sinned", "and", "fall",
 "short", "of", "the", "glory", "of", "God", "Romans", "3:23"]

position_verse = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]

def next_practice_verse (target_word):
    practice_verse [target_word] = "(---)"
    print ()
    print (practice_verse [0],practice_verse [1],
    	practice_verse [2],practice_verse [3],practice_verse [4],
    	practice_verse [5],practice_verse [6],practice_verse [7],
    	practice_verse [8],practice_verse [9],practice_verse [10],
    	practice_verse [11] + ".", practice_verse [12],
    	practice_verse [13])
    print ()
    
def player_answer (target_word):    
    wrong_answers = random.sample (master_verse, 3)
    options = [master_verse [target_word], wrong_answers [0], wrong_answers [1], wrong_answers [2]]
    random_option = random.sample(options,4)
    print ("What word is missing?")
    print ()
    print (random_option [0])
    print (random_option [1])
    print (random_option [2])
    print (random_option [3])
    answer = str(input ())
    if answer == master_verse [target_word]:
        print ()
        print ("You're right!")
        practice_verse [target_word] = "---"
        print ()
        print ()
        print ()
    else:
        print ()
        print ("You're wrong.")
        practice_verse [target_word] = master_verse [target_word]

def main ():
    level = 0
    target_list = random.sample (position_verse,14) #shuffle the words in the verse
    while level < 14:
        target_word = target_list [level]
        '''select the first word in the shuffled list
        '''
        next_practice_verse (target_word)
        '''display the verse with a new word hidden
        '''
        player_answer (target_word)
        '''display four words from the verse, 
           one word matching to the hidden word 
           and collect the user's response
           '''
        level += 1

main ()
