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
        '''
        labels are filenames
        labelsObj are file objects
        return the result filename, X and Y for plotting
        '''
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
