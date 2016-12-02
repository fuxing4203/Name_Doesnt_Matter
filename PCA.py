from Document import Document
from BasicStats import BasicStats
class PCA:
    def __init__(self, LoDM, n):
        #LoDM for list of document names
        #n is the number of words considered
        self.LoDM = LoDM
        self.n = n

    def processData(self):
        fileA = Document(self.LoDM[0])
        fileA.generateWhole()
        wordlist = fileA.wordlist
        worddict = BasicStats.topN(BasicStats.createFreqMap(wordlist), self.n)
        self.wordlist = []
        for i in worddict:
            self.wordlist.append(i)
        self.processedList = [[None] + self.wordlist]
        self.dictList = []
        for item in self.LoDM:
            theFile = Document(item)
            theFile.generateWhole()
            wordlist = theFile.wordlist
            freqMap = BasicStats.createFreqMap(wordlist)
            self.dictList.append(freqMap)
        self.wordCount = []
        for item in self.dictList:
            count = 0
            for i in item:
                count += item[i]
            self.wordCount.append(count)
        for i in range(len(self.LoDM)):
            listofProb = []
            for w in self.wordlist:
                if w in self.dictList[i]:
                    listofProb.append(item[w]/self.wordCount[i])
                else:
                    listofProb.append(0)
            result = [self.LoDM[i]]
            result.extend(listofProb)
            print(result)
            self.processedList.append(result)
        return self.processedList

#a = PCA(['GrimmFairyTales.txt','Ulysses.txt'],10)
