from Document import Document
from BasicStats import BasicStats
class PCA:
    def __init__(self, LoDM, LoDMObj, n):
        #LoDM for list of document names
        #n is the number of words considered
        self.LoDM = LoDM
        self.LoDMObj = LoDMObj
        self.n = n

    def processData(self):
        fileA = Document(self.LoDM[0])
        fileA.generateWhole()
        wordlist = fileA.wordlist
        words = BasicStats.HTopNBottomN(BasicStats.createFreqMap(wordlist), self.n)
        self.wordlist = words[1][1:]
        self.processedList = []
        self.dictList = []
        self.wordCount = []
        for item in self.LoDMObj:
            freqMap = BasicStats.createFreqMap(item.wordlist)
            self.dictList.append(freqMap)
            self.wordCount.append(item.getWordCount())
        for i in range(len(self.LoDM)):
            listofProb = []
            for w in self.wordlist:
                if w in self.dictList[i]:
                    listofProb.append(self.dictList[i][w]/self.wordCount[i])
                else:
                    listofProb.append(0)
            result = [self.LoDM[i]]
            result.extend(listofProb)
            self.processedList.append(result)
        return (self.processedList, self.wordlist)
'''
m = ['GrimmFairyTales.txt','Ulysses.txt']
c = [Document(item) for item in m]
for item in c:
    item.generateWhole()
a = PCA(m, c,3)
a.processData()
'''
