secretWord = 'pie' 
lettersGuessed = ['a', 'c', 'b', 'm', 'z', 'w', 'r', 'j', 'v', 'l']


def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            continue
        else:
            return False
            
    return True
    
            
print(isWordGuessed(secretWord, lettersGuessed))