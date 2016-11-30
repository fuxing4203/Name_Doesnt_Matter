from Document import Document
from DocumentStream import DocumentStream
from Sentence import Sentence
from DocumentStreamError import DocumentStreamError
from CommandLinePlotter import CommandLinePlotter
from BasicStats import BasicStats
import time
from Heap import *

def main():
    filename = input('Please input a filename:    ')
    fileA = Document(filename)
    title = fileA.generateWhole()
    wordlist = fileA.wordlist
    o = 'The time required to do top 50 using dictionary: \n'
    
    
    worddict = BasicStats.createFreqMap(wordlist)
    n = 50
    a = time.time()
    topdict = BasicStats.topN(worddict,int(n))
    b = time.time()
    o += str(b-a) + '\n'

    o+= 'The time required to do top 50 using heap: \n'
    c = time.time()

    k = BasicStats.HTopNBottomN(worddict, int(n))
    d = time.time()
    o += str(d - c) + '\n'

    o += '\nMax 50\n'
    for i in range(1,51):
        o += str(k[1][i]) + ' ' + str(k[0][i]) + '\n'

    o += '\nMin 50\n'    
    for i in range(1,51):
        o += str(k[3][i]) + ' ' + str(k[2][i]) + '\n'
       
        
    lista = [[],[]]
    for i in topdict:
        lista[0] += [i] #words
        lista[1] += [topdict[i]] #frequency
    graph = CommandLinePlotter.Scatter2D(lista[1])
    timefile= open('Top50TIMEFILE'+'-'+filename,'wt', encoding = 'UTF-8')
    for j in o:
        timefile.write(j)
    timefile.close()
        
    
    
if __name__ == '__main__':
    main()
    
    
