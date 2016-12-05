from Document import Document
from DocumentStream import DocumentStream
from Sentence import Sentence
from DocumentStreamError import DocumentStreamError
from CommandLinePlotter import CommandLinePlotter
from BasicStats import BasicStats

def main():
    '''
    will return a plot of topN
    '''
    filename = input('Please input a filename:    ')
    fileA = Document(filename)
    title = fileA.generateWhole()
    wordlist = fileA.wordlist



    worddict = BasicStats.createFreqMap(wordlist)
    n = input('Please input the number of top words:    ')

    topdict = BasicStats.topN(worddict,int(n))
    lista = [[],[]]
    for i in topdict:
        lista[0] += [i] #words
        lista[1] += [topdict[i]] #frequency
    graph = CommandLinePlotter.Scatter2D(lista[1])


if __name__ == '__main__':
    main()
