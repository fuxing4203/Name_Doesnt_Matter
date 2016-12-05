"""This file contains the starting block for PCA in scikit
    You will need to add functions/methods to convert data into needed format,
    See treedemo.py
"""

import pandas as pd
import numpy as np
from sklearn import decomposition
from PCA import *
class SKPCA:
    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None

    def train(self, labels, labelsObj, ncomp):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
        a = PCA(labels, labelsObj, ncomp)
        (data, self.wordlist) = a.processData()
        self.ncomp = ncomp
        self.labels = labels
        #Strip the first column
        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.pca_h = decomposition.PCA(ncomp)
        self.pca_h.fit(x)
        self.X = self.pca_h.transform(x)

    def evaluation(self, labels, labelsObj):
        data = []
        for i in range(len(labelsObj)):
            prob = [None]
            wc = labelsObj[i].getWordCount()
            freqMap = BasicStats.createFreqMap(labelsObj[i].wordlist)
            for w in self.wordlist:
                if w in freqMap:
                    prob.append(freqMap[w]/wc)
                else:
                    prob.append(0)
            data.append(prob)
        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        Y = self.pca_h.transform(x)
        distance = []
        index = []
        for m in range(len(Y)):
            dm = []
            for i in range(len(self.X)):
                d = ((self.X[i][0] - Y[m][0]) ** 2 + (self.X[i][1] - Y[m][1]) ** 2) ** 0.5
                dm.append(d)
            index.append(dm.index(min(dm)))
            distance.append(dm)
        result = [self.labels[i] for i in index]
        return (result, self.X, Y)

'''
for x in range(1000):
    a = SKPCA()
    a.train(['GrimmFairyTales.txt', 'Ulysses.txt'], 10)
    print(a.X)
    data = [[None, 0.01008221175522577, 0.04656427769730342, 0.14273380466793933, 0.02001093598610938, 0.035561140796024675, 0.01730571836957877, 0.06195140201260516, 0.06767840526462209, 0.047609911456884396, 0.0790268890956707]]
    if a.evaluation(data) != 'GrimmFairyTales.txt':
        print('x:', x)
        raise Exception
'''
