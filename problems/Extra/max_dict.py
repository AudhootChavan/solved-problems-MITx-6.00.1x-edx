animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'],  'd': ['donkey', 'dog', 'dingo'],  'e': ['edonkey', 'edog', 'edingo', 'edonkey', 'edog', 'edingo']}


def biggest(aDict):
    l = []
    stuff = []
    value = aDict.values()
    for j in value:
        stuff.append(j)
    for i in value:
        l.append(len(i))
    
    index = l.index(max(l))
    print ("'" + str(stuff[index][0][0]) + "'")
    return 
    


biggest(animals)

