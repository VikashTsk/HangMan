# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()     #all word to load
letters_guessed = []        #empty list to start saving all the letters guessed
Warning_Flag = 4            #Warnings for Unexpected User input....
Unique_word = 0             #to check input is unique or not
No_of_guesses_available = 6 #Total No. of Guessed given to user    
    
    
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    Letters_matched = False
    for w in letters_guessed:
        for s in secret_word:
           
            if s== w:
                Letters_matched = True
                break
            else:
                Letters_matched = False
        
    return Letters_matched



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    list_guessed_word = []
    Letters_matched = False
    for s  in secret_word:
       for w in letters_guessed:
           if s == w:
               Letters_matched = True
               break
           elif s!= w:
               Letters_matched = False
                     
       if Letters_matched == True:
           list_guessed_word.append(s)
       else :
           list_guessed_word.append("_")
     
    guessed_word = ' '.join(list_guessed_word) #converting list to string
            

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return guessed_word

def repeated_guess(letters_guessed , UserInput):
    Not_Repeated_guess_flag = True
    for l in letters_guessed:
        if l == UserInput:
            Not_Repeated_guess_flag = False
            
    return Not_Repeated_guess_flag
    #To check the repeated inout from user.......



def User_input():
    global Warning_Flag
    global No_of_guesses_available
    correct_input_flag = True
    while correct_input_flag:
        user_input= input("Please Guess a letter ")
        
        if(len(user_input)==1 and user_input.isalpha() and repeated_guess(letters_guessed , user_input)):
            user_input.lower()
            correct_input_flag = False
        elif user_input== "*":
            Guessed_word= get_guessed_word(secret_word , letters_guessed)
            show_possible_matches(Guessed_word)
        else:
            if (Warning_Flag <= 0 and No_of_guesses_available > 0):
                No_of_guesses_available -=1
                print("Now you are left with", No_of_guesses_available , "guesses left")
            elif No_of_guesses_available <= 0:
                break
            else:
                print("Error !!! Please enter alphabet...")
                Warning_Flag -= 1
                print("You lose one warning....Now out of 3 warning you have left warning is ", Warning_Flag)
    return user_input
            

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    Letters_matched = True
    available_guess_letters = string.ascii_lowercase     
    list_available_letters = list(available_guess_letters) # converts string to list
    for s in available_guess_letters:
       for w in letters_guessed:
           if s == w:
               Letters_matched = True
               break
           elif s!= w:
               Letters_matched = False
                      
       if Letters_matched == True:
           list_available_letters.remove(s) #removes the guess if it has been guessed
    
    available_letters_to_guess = "".join(list_available_letters) # list is converted to string again
       
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return available_letters_to_guess
   
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    No_of_letters_in_secret_word = len(secret_word)  #TO find the no. of letters we have in guessed word
    global No_of_guesses_available  #Initially total guesses provided
    global Warning_Flag #Warnings for Unexpected User input....
    Unique_word = 0
    
    print("Hello!!! Welcome to the game HANGMAN...")
    #print(secret_word)
    print("I am thinking of word that is", No_of_letters_in_secret_word , "letters long")
    while No_of_guesses_available > 0:
        print("You have", No_of_guesses_available , "guesses left")
        print("****************************************")
        print("All Available Letters ", get_available_letters(letters_guessed))
        print("Round -", 7 - No_of_guesses_available)
        #user_input = User_input()
        
        
        correct_input_flag = True
        while correct_input_flag:
            user_input= input("Please Guess a letter ")
            
            if(len(user_input)==1 and user_input.isalpha() and repeated_guess(letters_guessed , user_input)):
                user_input.lower()
                correct_input_flag = False    
            else:
                if (Warning_Flag <= 0 and No_of_guesses_available > 0):
                    No_of_guesses_available -=1
                    print("Now you are left with", No_of_guesses_available , "guesses left")
                elif No_of_guesses_available <= 0:
                    break
                else:
                    print("Error !!! Please enter alphabet...")
                    Warning_Flag -= 1
                    print("You lose one warning....Now out of 3 warning you have left warning is ", Warning_Flag)
           
        letters_guessed.append(user_input)
           #User_input()
           #letters_guessed.append(User_input()) #User input is added to letters guessed
        
        #To know wheter The selected letter is right or wrong this if else block
        if is_word_guessed(secret_word , letters_guessed)== False:
            print("Sorry!! WRONG Guess !!! Thats not in my word...")
            Is_Vowel = False    #This is used to check user has given vowel or not
            vowel = ['a','e','i','o','u']
            for s in vowel:
                if s == user_input:
                    Is_Vowel = True   #if it is vowel then set to true
                    break
            
            if Is_Vowel == True:
                No_of_guesses_available -= 2 #if Vowel then loose to 2 guess
            else :
                No_of_guesses_available -= 1 #if Not vowel then 1 guess lose
           
        elif is_word_guessed(secret_word , letters_guessed)== True:
            Unique_word += 1
            print("Good Guess !!!")
        
        
        print(get_guessed_word(secret_word , letters_guessed))
        
        #to know whther word is complettely guessed
        Guessed_word= get_guessed_word(secret_word , letters_guessed)
        Word_Found = True  
        for u in Guessed_word:
            if u == "_":
                Word_Found = False
                break
        #if already the word is completly guessed..........
        if Word_Found == True :
            print("Congaratulatonsss!!! You Won !!!")
            MyScore = No_of_guesses_available * Unique_word 
            print("Correctly guessed the word \t" , secret_word)
            print("Your Score is ", MyScore)
            break
               
    if is_word_guessed(secret_word,letters_guessed) == False:
            print("OOPssss!!! You Lose !!!")
            print("The secret word was" , secret_word)
            
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    #Guessed_word= get_guessed_word(secret_word , letters_guessed)
    My_word= my_word.split(" ")
    match_status = False
    if len(My_word)==len(other_word):
        for i in range(len(other_word)):
            if My_word[i].isalpha():
                if My_word[i]==other_word[i]:
                    match_status = True
                else:
                    match_status = False
                    break
    
    return match_status
    # FILL IN YOUR CODE HERE AND DELETE "pass"
   



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for w in wordlist:
        if match_with_gaps(my_word , w)==True:
            print(w)
    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global No_of_guesses_available
    global Warning_Flag #Warnings for Unexpected User input....
    Unique_word = 0
    print("Welcome to the game of HANGMAN !!!")
    print("I am thinking of word that is ", len(secret_word) , "letters long")
    while No_of_guesses_available > 0:
        print("-------------------------------------")
        print("you have ",No_of_guesses_available , "guess left")
        print("All Available Letters ", get_available_letters(letters_guessed))
        
        user_input = User_input()
        letters_guessed.append(user_input)
        
        
        
        if is_word_guessed(secret_word , letters_guessed)== False:
            print("Sorry!! WRONG Guess !!! Thats not in my word...")
            Is_Vowel = False    #This is used to check user has given vowel or not
            vowel = ['a','e','i','o','u']
            for s in vowel:
                if s == user_input:
                    Is_Vowel = True   #if it is vowel then set to true
                    break
            
            if Is_Vowel == True:
                No_of_guesses_available -= 2 #if Vowel then loose to 2 guess
            else :
                No_of_guesses_available -= 1 #if Not vowel then 1 guess lose
           
        elif is_word_guessed(secret_word , letters_guessed)== True:
            Unique_word += 1
            print("Good Guess !!!")
        
        
        print(get_guessed_word(secret_word , letters_guessed))
        
        
        #to know whther word is complettely guessed
        Guessed_word= get_guessed_word(secret_word , letters_guessed)
        Word_Found = True  
        for u in Guessed_word:
            if u == "_":
                Word_Found = False
                break
        #if already the word is completly guessed..........
        if Word_Found == True :
            print("Congaratulatonsss!!! You Won !!!")
            MyScore = No_of_guesses_available * Unique_word 
            print("Correctly guessed the word \t" , secret_word)
            print("Your Score is ", MyScore)
            break
               
    if is_word_guessed(secret_word,letters_guessed) == False:
            print("OOPssss!!! You Lose !!!")
            print("The secret word was" , secret_word)
        
        
                
    
    
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
 