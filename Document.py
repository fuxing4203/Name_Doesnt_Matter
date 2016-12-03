import DocumentStream
from DocumentStream import DocumentStream
from Sentence import Sentence
class Document:
    def __init__(self,filename = ''):
        '''
        initiate variables
        '''
        self.filename = filename
        self.DS = DocumentStream()
        self.__Slist = self.DS.readWhole(self.filename)
        self.filename = filename
        self.wordlist = []
        self.__id = 0
        self.__wordcount = 0
        self.__linecount = 0
        self.__charcount = 0
    
    def getIndexSlist(self, index):
        '''
        get the sentence within self.__Slist with given the index
        '''
        return self.__Slist[index]
          
    def setIndexSlist(self, index, value):
        '''
        set a sentence within the self.__Slist to a given value
        '''
        assert index >=0 and index < len( self ), 'Put the right index'
        self.__Slist[index] = value
   
    def __len__(self):
        '''
        return length of self._Slist
        '''
        return len(self.__Slist)
        
    def wordcount(self, num ):
        self.__wordcount = num

    @property
    def wordcount(self):
        return self.__wordcount
        

    def linecount(self, num ):
        self.__linecount = num

    @property
    def linecount(self):
        return self.__linecount


    def charcount(self, num ):
        self.__charcount = num

    @property
    def charcount(self):
        return self.__charcount
    
    def generateWhole(self): 
        '''
        using text read from DocumentStream
        return the title information
        '''
        a = DocumentStream()
        self.__Slist = a.readWhole(self.filename)
        for i in range(len(self.__Slist)):
            
            sen = Sentence(self.__Slist[i])

            self.wordlist += sen.parseWords()
            
        firstsen = self.__Slist[0]
        fircopy = firstsen
        loc = 0
        firstlineword = []
        title = 'untitled'
        fircopy = fircopy.replace('"',' ')
        fircopy = fircopy.replace('-',' ')
        for i in fircopy:
            
            if i == '\n':
                i.replace('\n', ' ')               
                firstlineword += fircopy[0:loc].split()
                break
            loc += 1
        if False not in [k[0].isupper() for k in firstlineword]:
            title = firstsen[0:loc]
        return title
        '''
        filename = title
        fileout = open(filename,'wt',encoding = 'UTF-8')
        fileout.write(firstsen[loc:])
        for i in Slist[1:]:
            fileout.write(i)
        fileout.close
        '''

    def getWordCount(self):
        '''
        count how many words are there in a file by splitting with space
        '''
        for i in range(len(self.__Slist)):
            self.wordcount += len(i.split())
        return self.wordcount
        
    def getLineCount(self):
        '''
        count number of lines identified by "\n"
        '''
        for i in range(len(self.__Slist)):
            self.linecount += i.count('\n')
        return self.linecount
    
        
        

    
    
    

