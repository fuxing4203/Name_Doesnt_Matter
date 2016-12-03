from Document import Document
class TextFilter:
    def __init__(self, D):
        #D is an object created by initializing Document
        self.wordlist = []
        self.D = D
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
                #ord 48 - 57: 1-9
                #ord 65 - 90: Capital Letters
                #ord 97 - 122: lower case letters
                if (ord(self.wordlist[i][ch]) >= 48 and ord(self.wordlist[i][ch]) <= 57) or \
                   (ord(self.wordlist[i][ch]) >= 65 and ord(self.wordlist[i][ch]) <= 90) or \
                   (ord(self.wordlist[i][ch]) >= 97 and ord(self.wordlist[i][ch]) <= 122):
                    word += self.wordlist[i][ch]
                else:
                    word += ' '
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

    def apply(self, stringList):
        print(stringList)
        '''
        apply methods and piece back words into a text
        return the text
        '''
        #apply the methods
        for i in range(len(stringList)):
            if stringList[i] == 'NWS':
                #normalize whilespace
                self.nSpace()
            if stringList[i] == 'NC':
                #normalize case
                self.nCase()
            if stringList[i] == 'SNC':
                #strip null characters
                self.sNullChar()
            if stringList[i] == 'SN':
                #strip number
                self.sNumber()
            if stringList[i] == 'FW':
                #filter words
                self.nWords()
        for i in range(len(self.wordlist)):
            self.text += self.wordlist[i] + ' '
        filename = self.D.filename[:-4] + 'M' + '.txt'
        file = open(filename, 'wt',encoding = 'UTF-8')
        print('did2')
        file.write(self.text)
        file.close()

        
