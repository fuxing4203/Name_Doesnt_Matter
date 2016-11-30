from Document import Document
from Sentence import Sentence
from DocumentStream import DocumentStream
from copy import deepcopy
from sllist import *
from Heap import *


class BasicStats:

    @staticmethod
    def createFreqMap(wlist):
        '''
        create a frequency map of a list of words by using dictionary
        if word already in dictionary, frequency + 1
        else create another tag if the words is not empty
        '''
        '''
        O will be length of the wlist = n
        '''
        b = wlist
        adict = {}
        for word in b:
            if word.lower() in adict:
                adict[word.lower()] += 1
            elif word.lower() not in adict and word != '':
                adict[word.lower()] = 1
        return adict
    @staticmethod
    def slinkFreq(wlist):
        '''
        O will be O(n^2)
        '''    
        b = wlist
        allist = sllist()
        for word in b:
            a = allist.head

            while True:
                if a == None:
                    
                    allist.head = ListNode([word,1])
                    break
                elif a.next == None:
                    if a.data[0] == word:
                        a.data[1] += 1
                    else:
                        a.next = ListNode([word,1])
                    break
                elif a.data[0] == word:
                    a.data[1] += 1
                    break
                a = a.next
            
                
        return allist

        
    @staticmethod
    def maxl(kdict):
        '''
        helper function of topN
        find the key with the largest value in a dictionary
        '''
        b = 0
        s = ''
        for i in kdict:
            if kdict[i] > b:
                b = kdict[i]
                s = i
        return s
                
                
    def topN(bdict, n):
        '''
        input a dictionary and the inquired number n for analysis,
        analyze the dictionary, find the n words of highest frequency 
        returns the dictionary of top n word and its frequency         
        '''
        '''
        O will be length of bdict times n = m * n
        '''
        cdict = {}
        ddict = deepcopy(bdict)
        for i in range(n):

            cdict[BasicStats.maxl(ddict)] = ddict[BasicStats.maxl(ddict)]
            ddict[BasicStats.maxl(ddict)] = 1
        return cdict

    def LTopN(sslist, n):
        #linked list
        a = sllist()
        b = sslist.head
        small = 0
        if b == None:
            return a
        while b.next != None:
            k = a.head
            if a.size < n:
                if k == None:
                    a.head = ListNode(b.data)
                    small = b.data[1]
                    
                elif a.size == 1:
                    if b.data[1] > small:
                        a.head = ListNode(b.data)
                        a.head.next = k
                    else:
                        a.head.next = ListNode(b.data)
                        small = a.head.next[1]
                    
                else:                   
                    while k.next != None and k.next.data[1] > b.data[1]:
                        k = k.next
                    nextnode = k.next
                    if nextnode == 0:
                        small = b.data[1]
                    k.next = ListNode(b.data)
                    k.next.next = nextnode
                a.size += 1
            else:
                if b.data[1] > small:
                    k = a.head
                    c = None
                    n = None
                    p = None
                    while k.next != None:
                        if k.next.data[1] < b.data[1]:
                            c = k
                            n = k.next
                        p = k
                        k = k.next
                    c.next = ListNode(b.data)
                    c.next.next = n
                    p.next = None
                    small = p.data[1]
            b = b.next
        return a
                                               
                
                 
    def minl(kdict):
        '''
        helper function of topN
        find the key with the largest value in a dictionary
        '''
        b = 0
        s = ''
        for i in kdict:
            if kdict[i] < b:
                b = kdict[i]
                s = i
        return s
                
                
    def BottomN(bdict, n):
        '''
        input a dictionary and the inquired number n for analysis,
        analyze the dictionary, find the n words of highest frequency 
        returns the dictionary of top n word and its frequency         
        '''
        '''
        O will be length of bdict times n = m * n
        if we want to put bottomn and topn together and have a faster runtime, 
        we can use the state method.
        '''
        cdict = {}
        ddict = deepcopy(bdict)
        for i in range(n):

            cdict[BasicStats.minl(ddict)] = ddict[BasicStats.minl(ddict)]
            ddict[BasicStats.minl(ddict)] = 1
        return cdict
        
    
    def HTopNBottomN(adict, n):
        maxlistn = [0]
        maxlists = [0]
        minlistn = [0]
        minlists = [0]
        for i in adict:
            if len(maxlistn) < n + 1:
                Heapsort.HheapAdd(maxlistn,maxlists, adict[i], i)
                Heapsort.LheapAdd(minlistn, minlists, adict[i], i)
            else:
                if adict[i] > maxlistn[1]:
                    maxlistn[1] = adict[i]
                    maxlists[1] = i
                    Heapsort.lfixdown(maxlistn, maxlists, 1)
                elif adict[i] < minlistn[1]:
                    minlistn[1] = adict[i]
                    minlists[1] = i
                    Heapsort.hfixdown(minlistn, minlists, 1)
        return [maxlistn, maxlists,minlistn, minlists]

'''
def parentindexforbaseone(heap, rootindex):
    #for base one
    return rootindex //2

def leftchildforbase1(heap, rootindex):
    if rootindex*2 >= len(heap):
        return -1
    return rootindex*2

def rightchildforbase1(heap, rootindex):
    if rootindex*2 + 1 >= len(heap):
        return -1
    return rootindex*2 + 1


def HfixUp(heapn,heaps, index):
    #for base 1
    k = index
    if heapn[k] > heapn[k//2]:
        return
    else:
        if k == 1:
            return
        a = heapn[k]
        heapn[k] = heapn[k//2]
        heapn[k//2] = a
        b = heaps[k]
        heaps[k] = heaps[k//2]
        heaps[k//2] = b       

        HfixUp(heapn,heaps,k//2)
    
def HheapAdd(heapn,heaps, root, word):
    heapn += [root]
    heaps += [word]

    HfixUp(heapn,heaps,len(heapn)-1)

def lfixdown(heapn,heaps, rootindex):
    loc = rootindex
    lc = leftchildforbase1(heapn, loc)
    rc = rightchildforbase1(heapn, loc)
    a = heapn[loc]
    b = heaps[loc]
    if lc == -1 and rc == -1:
        return
    elif lc == -1:
        if heapn[loc] > heapn[rc]:
            heapn[loc] = heapn[rc]
            heapn[rc] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b           
            lfixdown(heapn,heaps, rc)
    elif rc == -1:
        if heapn[loc] > heapn[lc]:
            heapn[loc] = heapn[lc]
            heapn[lc] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b
            lfixdown(heapn,heaps, lc)
    else:
        alist = [heapn[lc],heapn[rc]]
        way = [lc,rc][alist.index(min(alist))]
        if heapn[way] < heapn[loc]:
            heapn[loc] = heapn[way]
            heapn[way] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b
            lfixdown(heapn,heaps, way)

def hfixdown(heapn,heaps, rootindex):
    loc = rootindex
    lc = leftchildforbase1(heapn, loc)
    rc = rightchildforbase1(heapn, loc)
    a = heapn[loc]
    b = heaps[loc]
    if lc == -1 and rc == -1:
        return
    elif lc == -1:
        if heapn[loc] < heapn[rc]:
            heapn[loc] = heapn[rc]
            heapn[rc] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b           
            hfixdown(heapn,heaps, rc)
    elif rc == -1:
        if heapn[loc] < heapn[lc]:
            heapn[loc] = heapn[lc]
            heapn[lc] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b
            hfixdown(heapn,heaps, lc)
    else:
        alist = [heapn[lc],heapn[rc]]
        way = [lc,rc][alist.index(max(alist))]
        if heapn[way] > heapn[loc]:
            heapn[loc] = heapn[way]
            heapn[way] = a
            heaps[loc] = heaps[rc]
            heaps[rc] = b
            hfixdown(heapn,heaps, way)

def LfixUp(heapn,heaps, index):
    #for base 1
    k = index
    if heapn[k] < heapn[k//2]:
        return
    else:
        if k == 1:
            return
        a = heapn[k]
        heapn[k] = heapn[k//2]
        heapn[k//2] = a
        b = heaps[k]
        heaps[k] = heaps[k//2]
        heaps[k//2] = b       

        LfixUp(heapn,heaps,index//2)
    
def LheapAdd(heapn,heaps, root, word):
    heapn += [root]
    heaps += [word]
    LfixUp(heapn,heaps,len(heapn)-1)
'''
