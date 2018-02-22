secretWord = 'banana' 
lettersGuessed = ['a', 'c', 'b', 'm', 'z', 'w', 'r', 'j', 'v', 'l']


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
    
    

print(getGuessedWord(secretWord, lettersGuessed))

    