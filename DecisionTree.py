
from copy import deepcopy
import math

class DTNode:

    def __init__(self, key = None):
        self.key = key
        self.children = None

class DecisionTree:

    def __init__(self, root = None):
        self.root = root
        self.odlist = None

    def train(self, root, tdlist, odlist, maxd = None):
        if root == self.root:
            self.odlist = odlist
        classifier = odlist[0]
        classifierd = self.catagorizediff(tdlist, 0)
        igc = self.igcaculate(classifierd)[0]
        if maxd == 0:
            return
        igdict = {}
        iginfo = {}
        for i in range(1,len(odlist)):
            if odlist[i] != None:
                iginfo[odlist[i]] = {}
                igdict[odlist[i]] = 0
                for j in tdlist:
                    if j!= None:
                        if j[i] != None:
                            if j[i] not in iginfo[odlist[i]]:
                                iginfo[odlist[i]][j[i]] = [j[0]]
                            elif j[i] in iginfo[odlist[i]]:
                                iginfo[odlist[i]][j[i]] += [j[0]]
                for k in iginfo[odlist[i]]:
                    iginfo[odlist[i]][k] = self.igcaculate(self.catagorizediff(iginfo[odlist[i]][k]))
                    igdict[odlist[i]] -= (iginfo[odlist[i]][k][1]/len(tdlist))*iginfo[odlist[i]][k][0]
                igdict[odlist[i]] = igc + igdict[odlist[i]]
                if root == self.root and igdict[odlist[i]] == igc*len(tdlist):
                    odlist[i] = None
                    
            
        maxc = None
        maxcn = None

        if igdict == {} and iginfo == {}:
            return None
        for l in igdict:
            if maxcn == None:
                maxcn = igdict[l]
            if igdict[l] >= maxcn:
                maxcn = igdict[l]
                maxc = l
        childrendict = {}
        g = odlist.index(maxc)
        for h in iginfo[maxc]:
            if iginfo[maxc][h][2] == None:
                ctdlist = deepcopy(tdlist)
                codlist = deepcopy(odlist)
                for u in iginfo[maxc]:
                    if u!= h:
                        for o in range(len(ctdlist)):
                            if ctdlist[o]!= None:
                                if ctdlist[o][g] == u:
                                    ctdlist[o] = None
                codlist[g] = None
                childrendict[h] = self.train(DTNode(h),ctdlist, codlist)
            else:
                childrendict[h] = DTNode(iginfo[maxc][h][2])
        if root == None:
            self.root = DTNode(maxc)
            self.root.children = childrendict
        else:
            root.key = maxc
            root.children = childrendict
            return root

        
                        
                        
            
        

    def catagorizediff(self, tdlist, columnnum = None):
        ddiff = {}
        for i in tdlist:
            if i != None:
                if columnnum != None:
                    attr = i[columnnum]
                else:
                    attr = i
                if attr in ddiff:
                    ddiff[attr] += 1
                else:
                    ddiff[attr] = 1
        return ddiff

       
    
    def igcaculate(self,diction):
        total = 0
        for i in diction:           
            total += diction[i]
        ig = 0
        for j in diction:
            if diction[j] > 0:
                ig -= (diction[j]/total)*math.log(diction[j]/total, 2)
                g = j

        if ig != 0.0:
            
            if float(ig) == float(-math.log(1/total, 2)):
                g = [i for i in diction]
            else:
                g = None
            
        return ig, total, g
    


    def eval(self, tdlist):
        for i in range(len(tdlist)):
            root = self.root
            while root.children!= None:
                
                root = root.children[tdlist[i][self.odlist.index(root.key)]]
            tdlist[i][0] = root.key
        return tdlist

