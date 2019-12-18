from getword import Word

def getrandword():
    word = Word('words.txt')
    return word.randFromDB()