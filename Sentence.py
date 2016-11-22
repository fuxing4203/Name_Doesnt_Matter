class Sentence:

    def __init__(self, sen):
        '''
        initiate variables
        punctuation is the last letter in the element
        sen is the list of sentence created by DocumentStream
        '''
        self.wordcount = 0
        self.charcount = 0
        self.sen = sen
        self.puncutaion = sen[-1]

        
    def parseWords(self):
        '''
        wordlist is created by splitting the sentence with space
        self.wordcount is updated
        '''
        wordlist = self.sen[:-1].split()
        if "'" in wordlist:
            wordlist.remove("'")
        self.wordcount = len(wordlist)
        return wordlist

    def parseChar(self):
        '''
        extract every character from self.sen to a list
        counted by length and stored in self.charcount
        '''
        charlist = [i for i in self.sen]
        self.charcount = len(charcount)
        return charlist
                
