from tkinter import *
from os import *
from os.path import *
from Document import *
from DocumentStream import *
from Sentence import *
from DecisionTree import *
from BasicStats import *
from TextFilter import *
from MatPlotPloter import *

class GUI:
    fileName = []
    fileObj = []
    filters = [] #[[filters]]
    charInfo = [] #[[genre, year, topics]]
    def __init__(self, root):
        self.root = root
        self.uploadB = Button(text = 'Upload', command = upLoadF)
        self.chrInfoB = Button(text = 'Characteristic Info', command = charInfoF)
        self.textFiltersB = Button(text = 'Text Filters', command = textFiltersF)
        self.statsB = Button(text = 'Statistics', command = statsF)
        self.predictB = Button(text = 'Predictions', command = predictF)
        self.uploadB.grid(row = 0, column = 0)
        self.chrInfoB.grid(row = 0, column = 1)
        self.textFiltersB.grid(row = 0, column = 2)
        self.statsB.grid(row = 0, column = 3)
        self.predictB.grid(row = 0, column = 4)
        welcome = Label(root, text = 'Welcome!\nPlease press upload button to upload the file.')
        welcome.grid(columnspan = 5)

    def forget(self, row = 1):
        for label in root.grid_slaves():
            if int(label.grid_info()["row"]) >= row:
                label.grid_forget()
    def validate(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_filename = ''
            return True
        try:
            self.entered_filename = new_text
            return True
        except ValueError:
            return False

class textFiltersF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        self.variables = []
        self.fileFrame = LabelFrame(root, text = 'Files')
        self.files()
        self.fileFrame.grid(row = 2, column = 0, columnspan = 2, sticky = W+E+N+S)
        self.filterframe = LabelFrame(root, text = 'Text Filters, Check to Apply')
        self.filters()
        self.filterframe.grid(row = 2, column = 2, columnspan = 2,sticky = N)
        self.stateFrame = LabelFrame(root, text = 'State')
        self.state()
        self.stateFrame.grid(row = 2,column = 4, columnspan = 1, sticky = W+E+N+S)
        if GUI.fileObj == []:
            for thefile in GUI.fileName:
                GUI.fileObj.append(Document(thefile))
            for D in GUI.fileObj:
                D.generateWhole()

    def filters(self):
        self.varnws = IntVar()
        self.varnc = IntVar()
        self.varsnc = IntVar()
        self.varsn = IntVar()
        self.varfw = IntVar()
        self.filters = ['NWS','NC','SNC','SN','FW']
        nws = Checkbutton(self.filterframe, text = 'Nomralize White Space',variable = self.varnws, onvalue = 1, offvalue = 0)
        nc = Checkbutton(self.filterframe, text = 'Normalize Cases',variable = self.varnc, onvalue = 1, offvalue = 0)
        snc = Checkbutton(self.filterframe, text = 'Strip Null Characters',variable = self.varsnc, onvalue = 1, offvalue = 0)
        sn = Checkbutton(self.filterframe, text = 'Strip Numbers',variable = self.varsn, onvalue = 1, offvalue = 0)
        fw = Checkbutton(self.filterframe, text = 'Filter Words',variable = self.varfw, onvalue = 1, offvalue = 0)
        ap = Button(self.filterframe, text = 'Apply filters',command = lambda: self.applyfilters(self.variables,[self.varnws, self.varnc, self.varsnc, self.varsn, self.varfw]))
        nws.grid(sticky = 'W')
        nc.grid(sticky = 'W')
        snc.grid(sticky = 'W')
        sn.grid(sticky = 'W')
        fw.grid(sticky = 'W')
        ap.grid(sticky = 'E')

    def state(self):
        self.sti_text = StringVar()
        self.sti = "Haven't applied anything"
        self.sti_text.set(self.sti)
        stil = Label(self.stateFrame, textvariable = self.sti_text)
        stil.grid(columnspan= 2 , sticky = W+E+N+S)

    def files(self):
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(self.fileFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            self.variables.append(var)
        if GUI.fileName == []:
            welcome = Label(self.fileFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid()

    def applyfilters(self, variables, filterscs):
        empty = True
        for i in range(len(variables)):
            if variables[i].get() == 1:
                dofil = TextFilter(GUI.fileObj[i])
                dofil.apply([self.filters[j] for j in range(len(filterscs)) if filterscs[j].get() == 1], GUI.fileObj[i])
                empty = False
        if empty == True:
            self.sti= 'Nothing applied'
        else:
            self.sti= 'Successfully applied'
        self.sti_text.set(self.sti)

class predictF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(columnspan = 100)
        left = Label(labelframe, text='Predictions')
        left.pack()
        print(GUI.filters)

class charInfoF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root, text = 'Characteristic Info')
        labelframe.grid(columnspan = 100)
        genreB = Button(text = 'Genre', command = self.genreF)
        yearB = Button(text = 'Year', command = self.yearF)
        topicsB = Button(text = 'Topics', command = self.topicsF)
        genreB.grid(row = 1, column = 0)
        yearB.grid(row = 1, column = 1)
        topicsB.grid(row = 1, column = 2)
        if GUI.charInfo == []:
            for i in range(len(GUI.fileName)):
                GUI.charInfo.append([None, None, None])
        self.genreF()

    def genreF(self):
        self.forget(2)
        genreFrame = LabelFrame(self.root, text = 'Genre')
        genreFrame.grid(columnspan = 100)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(genreFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(genreFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        genreL = Label(genreFrame, text = 'Please enter the genre.')
        genre = Entry(genreFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(genreFrame, text = 'Add', command = lambda: self.getResult(variables, genre))
        genreL.grid()
        genre.grid()
        upB.grid()

    def yearF(self):
        self.forget(2)
        yearFrame = LabelFrame(self.root, text = 'Year')
        yearFrame.grid(columnspan = 100)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(yearFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(yearFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        yearL = Label(yearFrame, text = 'Please enter the year.')
        year = Entry(yearFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(yearFrame, text = 'Add', command = lambda: self.getResult(variables, year, 1))
        yearL.grid()
        year.grid()
        upB.grid()

    def topicsF(self):
        self.forget(2)
        topicsFrame = LabelFrame(self.root, text = 'Topics')
        topicsFrame.grid(columnspan = 100)
        vcmd = self.root.register(self.validate)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(topicsFrame, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        if GUI.fileName == []:
            welcome = Label(topicsFrame, text = 'Welcome!\nPlease press upload button to upload the file.')
            welcome.grid(columnspan = 5)
        topicsL = Label(topicsFrame, text = 'Please enter the year.')
        topics = Entry(topicsFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(topicsFrame, text = 'Add', command = lambda: self.getResult(variables, topics, 2))
        topicsL.grid()
        topics.grid()
        upB.grid()

    def getResult(self, variables, info, infoType = 0):
        for i in range(len(variables)):
            if variables[i].get() == 1:
                GUI.charInfo[i][infoType] = info.get()
        print(GUI.charInfo)


class statsF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        topNB = Button(text = 'TopN', command = self.topNF)
        printStatsB = Button(text = 'Display Statistics', command = self.printStatsF)
        printStatsB.grid(row = 1, column = 0)
        topNB.grid(row = 1, column = 1)
        self.printStatsF()
    def printStatsF(self):
        self.forget(2)
        statsframe = LabelFrame(self.root)
        statsframe.grid(columnspan = 5, sticky = E+W+S+N)
        attr = ['genre', 'year', 'topics', 'author', 'word count', 'line count', 'char count']
        Label(statsframe, text = ' ').grid(row = 2, column = 1)
        for i in range(len(GUI.fileName)):
            Label(statsframe, text = GUI.fileName[i]).grid(row = 2, column = i + 2)
        for i in range(len(attr)):
            Label(statsframe, text = attr[i]).grid(row = i + 3, column = 1)
            if i >= 0  and i <= 2:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.charInfo[m][i]).grid(row = i + 3, column = m + 2)
            elif i == 3:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].DS.getauthor(GUI.fileName[m])).grid(row = i + 3, column = m + 2)
            elif i == 4:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getWordCount()).grid(row = i + 3, column = m + 2)
            elif i == 5:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getLineCount()).grid(row = i + 3, column = m + 2)
            elif i == 6:
                for m in range(len(GUI.fileObj)):
                    Label(statsframe, text = GUI.fileObj[m].getCharCount()).grid(row = i + 3, column = m + 2)

    def topNF(self):
        self.forget(2)
        topNframe = LabelFrame(self.root, text = 'TopN')
        topNframe.grid(columnspan = 5, sticky = E+W+S+N)
        nL = Label(topNframe, text = 'Please enter N for TopN')
        vcmd = self.root.register(self.validate)
        n = Entry(topNframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(topNframe, text = 'Enter', command = lambda: self.getResult(n))
        nL.grid()
        n.grid()
        upB.grid()
    def getResult(self, n):
        self.N = int(n.get())
        for m in range(len(GUI.fileObj)):
            worddict = BasicStats.createFreqMap(GUI.fileObj[m].wordlist)
            topdict = BasicStats.topN(worddict, self.N)
            lista = [[],[]]
            for i in topdict:
                lista[0] += [i] #words
                lista[1] += [topdict[i]] #frequency
            MatPlotPloter().barGraphfortop(lista[0], lista[1], GUI.fileName[m])
class upLoadF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(rowspan = 5, column = 0, columnspan = 2, sticky = N)
        fileNameL = Label(labelframe, text = 'Please enter the file name.')
        vcmd = self.root.register(self.validate)
        fileName = Entry(labelframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(labelframe, text = 'Upload', command = lambda: self.getResult(fileName))
        removeB = Button(labelframe, text = 'Remove', command = lambda: self.removeResult(fileName))
        fileNameL.grid(row=1,column = 0, columnspan = 2)
        fileName.grid(row=2,column = 0 ,columnspan = 2)
        upB.grid(row = 3,sticky = W+E)
        removeB.grid(row = 4, sticky = W+E)
        self.printFileNames()

    def printFileNames(self):
        self.forget(2)
        Label(self.root, text = 'Uploaded Files').grid(row = 1, column = 2, columnspan = 3, sticky = N)
        rown = 2
        for item in GUI.fileName:
            Label(self.root, text = item).grid(row= rown, column = 2, columnspan = 3, sticky = N)
            rown+= 1

    def getResult(self, fileName):
        GUI.fileName.append(fileName.get())
        self.printFileNames()

    def removeResult(self, fileName):
        index = GUI.fileName.index(fileName.get())
        GUI.fileName.pop(index)
        if GUI.filters != []:
            GUI.filters.pop(index)
        if GUI.charInfo != []:
            GUI.charInfo.pop(index)
        if GUI.fileObj != []:
            GUI.fileObj.pop(index)
        self.printFileNames()




root = Tk()
gui = GUI(root)
root.mainloop()
