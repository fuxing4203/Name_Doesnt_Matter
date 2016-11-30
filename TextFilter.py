from Document import Document
class TextFilter:
    def __init__(self, D):
        #D is an object created by initializing Document
        self.wordlist = []
        self.text = ''
        for i in range(len(D)):
            #wordlist is derived from the sentence list of the document
            self.wordlist.extend(D.getIndexSlist(i).split())

    def nSpace(self):
        #nomalizes the white space
        '''
        we actually don't need to consider this
        since more than one space is considered as breaking the sentence
        '''
        pass


    def nCase(self):
        #make all letters lower case
        for i in range(len(self.wordlist)):
            self.wordlist[i] = self.wordlist[i].lower()

    def sNullChar(self):
        #remove characters not in ascii set
        for i in range(len(self.wordlist)):
            word = ''
            for ch in range(len(self.wordlist[i])):
                #ord 60 - 71: 1-9
                #ord 101 - 132: Capital Letters
                #ord 141 - 172: lower case letters
                if (ord(self.wordlist[i][ch]) >= 60 and ord(self.wordlist[i][ch]) <= 71) or \
                   (ord(self.wordlist[i][ch]) >= 101 and ord(self.wordlist[i][ch]) <= 132) or \
                   (ord(self.wordlist[i][ch]) >= 141 and ord(self.wordlist[i][ch]) <= 172):
                    word += a[i][ch]
            self.wordlist[i] = word

    def sNumber(self):
        #remove all numbers
        for i in range(len(self.wordlist)):
            word = ''
            for ch in range(len(self.wordlist[i])):
                if not (self.wordlist[i][ch] >= '0' and self.wordlist[i][ch] <= '9'):
                    word += self.wordlist[i][ch]
            self.wordlist[i] = word

    def nWords(self):
        '''
        remove all words provided in the file with given fileName
        '''
        words = []
        file = open('filterwords.txt', 'r')
        text = file.read()
        file.close()
        text = text.lower()
        text = text.replace('\t', ' ')
        text = text.replace('\n', ' ')
        words = text.split()
        for i in range(len(self.wordlist)):
            if self.wordlist[i] in words:
                self.pop(i)

    def apply(stringList):
        '''
        apply methods and piece back words into a text
        return the text
        '''
        #apply the methods
        for i in range(len(stringList)):
            if stringList[i] == 'NWS':
                #normalize whilespace
                nSpace(self)
            if stringList[i] == 'NC':
                #normalize case
                nCase(self)
            if stringList[i] == 'SNC':
                #strip null characters
                sNullChar(self)
            if stringList[i] == 'SN':
                #strip number
                sNumber(self)
            if stringList[i] == 'FW':
                #filter words
                nWords(self)
        for i in range(len(self.wordlist)):
            self.text += self.wordlist[i] + ' '
        filename = D.filename[:-4] + 'M' + '.txt'
        file = open(filename, 'w')
        file.write(self.text)
        file.close()

