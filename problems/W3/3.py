lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    l = []
    s = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        l.append(i)
    
    for j in lettersGuessed:
        if j in alphabets:
            l.remove(j)
    
    for k in l:
        s = s + k
    
    return s
        
    
            
print(getAvailableLetters(lettersGuessed))