from Document import Document
from BasicStats import BasicStats
class PCA:
    def __init__(self, LoDM, n):
        #LoDM for list of document names
        #n is the number of words considered
        self.processedList = [[None] + LoDM]
        fileA = Document(LoDM[0])
        fileA.generateWhole()
        wordlist = fileA.wordlist
        worddict = BasicStats.topN(BasicStats.createFreqMap(wordlist), n)
        self.wordlist = []
        for i in worddict:
            self.wordlist.append(i)
        print(self.wordlist)
        self.dictList = []
        for item in LoDM:
            file = Document(item)
            file.generateWhole()
            wordlist = file.wordlist
            freqMap = BasicStats.createFreqMap(wordlist)
            self.dictList.append(BasicStats.topN(freqMap, len(freqMap)))
        print('finished creating dict')
        self.wordCount = []
        for item in self.dictList:
            count = 0
            for i in item:
                count += item[i]
            self.wordCount.append(count)
        print('finished counting')
        for w in self.wordlist:
            listofProb = []
            for i in range(len(self.dictList)):
                if w in self.dictList[i]:
                    listofProb.append(item[w]/self.wordCount[i])
                else:
                    listofProb.append(0)
            self.processedList.append([w].extend(listofProb))
        return self.processedList
