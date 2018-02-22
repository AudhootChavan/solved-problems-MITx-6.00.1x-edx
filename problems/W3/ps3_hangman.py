#
#import random
#
#WORDLIST_FILENAME = "C:/Users/Audhoot/Downloads/words.txt"
#
#def loadWords():
#    print("Loading word list from file...")
#    inFile = open(WORDLIST_FILENAME, 'r')
#    line = inFile.readline()
#    wordlist = line.split()
#    print("  ", len(wordlist), "words loaded.")
#    return wordlist
#
#def chooseWord(wordlist):
#    return random.choice(wordlist)
#
#
#wordlist = loadWords()

secretWord = 'sea'
test = []

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
    return True
   

def getGuessedWord(secretWord, lettersGuessed):
    l = []
    s = ''
    
    for i in secretWord:
        if i in lettersGuessed:
            l.append(i)
        else:
            l.append('_')
            
    for j in l:
        if j == '_':
            s = s + j
            s = s + ' '
        else:
            s = s + j
    
    return s
   

def getAvailableLetters(lettersGuessed):
    global test
    l = []
    s = ''
    
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        l.append(i)
    
    for j in lettersGuessed:
        if j in alphabets:
            if j not in l:
                break
            l.remove(j)
            test.append(j)
    
    for k in l:
        s = s + k
    return s
        
  

def hangman(secretWord):
    global test
    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print( '-------------')
    while guesses > 0:
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        letter = input('Please guess a letter: ')
        lettersGuessed.append(letter)
        if letter in secretWord:
            if letter in test:
                print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
                print( '-------------')
                continue
            else:
                print('Good Guess: ' + getGuessedWord(secretWord, lettersGuessed))
      
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed) )
            guesses = guesses - 1
        print( '-------------')
        
        if isWordGuessed(secretWord, lettersGuessed):
            return 'Congratulations, you won!'
            
            
        
    if guesses == 0:
        return 'Sorry, you ran out of guesses. The word was ' + secretWord + '.' 
       
        
    
    

print(hangman(secretWord))
    



    

    

