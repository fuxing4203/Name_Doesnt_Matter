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
    charInfo = [] #['Author','Genre','Year','Topic']
    attr = ['None']
    DT = DecisionTree()
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
        elif len(GUI.fileObj) != len(GUI.fileName):
            lengthD = len(GUI.fileName) - len(GUI.fileObj)
            for i in range(lengthD)[::-1]:
                GUI.fileObj.append(Document(GUI.fileName[-(1 + i)]))
                GUI.fileObj[-1].generateWhole()
    def filters(self):
        self.varnws = IntVar()
        self.varnc = IntVar()
        self.varsnc = IntVar()
        self.varsn = IntVar()
        self.varfw = IntVar()
        self.filters = ['NWS','NC','SNC','SN','FW']
        nws = Checkbutton(self.filterframe, text = 'Normalize White Space',variable = self.varnws, onvalue = 1, offvalue = 0)
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
        if GUI.fileObj == []:
            for thefile in GUI.fileName:
                GUI.fileObj.append(Document(thefile))
            for D in GUI.fileObj:
                D.generateWhole()
        elif len(GUI.fileObj) != len(GUI.fileName):
            lengthD = len(GUI.fileName) - len(GUI.fileObj)
            for i in range(lengthD)[::-1]:
                GUI.fileObj.append(Document(GUI.fileName[-(1 + i)]))
                GUI.fileObj[-1].generateWhole()
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
        dtB = Button(text = 'ID3', command = self.dtF)
        pcaB = Button(text = 'PCA', command = self.pcaF)
        dtB.grid(row = 1, column = 0, columnspan = 1, sticky = W+E+S+N)
        pcaB.grid(row = 1, column = 1, columnspan = 1, sticky = W)
        self.dtF()
    #decision tree
    def dtF(self):
        self.forget(2)
        trainB = Button(text = 'Train', command = self.trainF)
        evaluationB = Button(text = 'Evaluation', command = self.evaluationF)
        trainB.grid(row = 2, column = 0, columnspan = 1, sticky = W+E+S+N)
        evaluationB.grid(row = 3, column = 0, columnspan = 1, sticky = W+E+S+N)
        self.trainF()
    def trainF(self):
        labelframe1 = LabelFrame(self.root, text = 'Train with desired infos')
        labelframe1.grid(row = 2, rowspan = 100, column = 1, columnspan = 9, sticky = W+E+N+S)
        self.labelframe1of1 = LabelFrame(self.root, labelframe1, text = 'Select classifier')
        self.labelframe1of1.grid(row = 3, rowspan = 4, column = 1, columnspan = 2, sticky =N)
        self.labelframe2of1 = LabelFrame(self.root, labelframe1, text = 'Select the files')
        self.labelframe2of1.grid(row = 3, rowspan = 100 , column = 3, columnspan = 5, sticky = W+N+S+E)
        labelframe3of1 = LabelFrame(self.root, labelframe1, text = 'State')
        labelframe3of1.grid(row = 4,  column = 8, sticky = W+E+N+S)
        self.sfiles = []
        self.filesi()
        self.var = StringVar()
        self.var.set('None')
        self.selection= StringVar()
        self.selection_text = "You selected:\n" + str(self.var.get())
        self.selection.set(self.selection_text)
        R1 = Radiobutton(self.labelframe1of1, text="Genre", variable=self.var, value='Genre',command=self.sel)
        R1.grid(sticky = W)
        R2 = Radiobutton(self.labelframe1of1, text="Year", variable=self.var, value='Year',command=self.sel)
        R2.grid(sticky = W)
        R3 = Radiobutton(self.labelframe1of1, text="Topic", variable=self.var, value='Topic',command=self.sel)
        R3.grid(sticky = W)
        R4 = Radiobutton(self.labelframe1of1, text="Author", variable=self.var, value='Author',command=self.sel)
        R4.grid(sticky = W)
        label  = Label(self.labelframe1of1, textvariable = self.selection)
        label.grid(sticky = W+E)
        self.svar = StringVar()
        self.svar_text = "Haven't\ntrained"
        self.svar.set(self.svar_text)
        applyB = Button(text = 'Apply', command = self.apply(self.var.get(), self.sfiles))
        applyB.grid(row = 3, column = 8, columnspan = 1, sticky = W+E+N+S)
        statelabel = Label(labelframe3of1, textvariable = self.svar)
        statelabel.grid()
    def filesi(self):
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(self.labelframe2of1, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            self.sfiles.append(var)
    def apply(self, classifer, files):
        self.attr = ['Author','Genre','Year','Topic']
        indexc = GUI.attr.index(classifer)
        self.odlist = [classifer]
        self.tdlist = [[i[indexc]] for i in GUI.charInfo]
        for i in range(len(GUI.attr)):
            if GUI.attr[i] != classifer:
                self.odlist += [GUI.attr]
                for j in self.tdlist:
                    j+= [GUI.charInfo[i]]
        print([self.odlist, self.tdlist])
        GUI.DT.train(GUI.DT.root, self.tdlist, self.odlist)
        print('did')
        if self.tdlist != []:
            self.svar_text = 'trained'
        else:
            self.svar_text = "Haven't\ntrained"
        self.svar.set(self.svar_text)
    def sel(self):
        self.selection_text = "You selected:\n" + str(self.var.get())
        self.selection.set(self.selection_text)
    def setk(self):
        if self.svar.get() != 'trained':
            self.odlist = ['Author','Genre','Year','Topic']
        self.firstk.set(self.odlist[1])
        self.secondk.set(self.odlist[2])
        self.thirdk.set(self.odlist[3])

    def evaluationF(self):

        self.twolist = []
        self.labelframe2 = LabelFrame(self.root, text = 'Evaluate with part of the informations')
        self.labelframe2.grid(row = 2, rowspan = 100, column = 1, columnspan = 100, sticky = W+E+N+S)
        self.firstk = StringVar()
        self.secondk = StringVar()
        self.thirdk = StringVar()
        self.setk()
        self.entered_1 = ''
        self.entered_2 = ''
        self.entered_3 = ''
        inputframe1 = LabelFrame(self.labelframe2, text = 'Input known infos')
        inputframe1.grid(row = 3, rowspan = 4, column = 2, columnspan = 4, sticky = W+N+E+S)
        vcmdf = self.root.register(self.validate1)
        vcmds = self.root.register(self.validate2)
        vcmdt = self.root.register(self.validate3)
        labelf = Label(inputframe1, textvariable = self.firstk)
        labelf.grid(row = 4, column = 2, columnspan = 1)
        labels = Label(inputframe1, textvariable = self.secondk)
        labels.grid(row = 5, column = 2, columnspan = 1)
        labelt = Label(inputframe1, textvariable = self.thirdk)
        labelt.grid(row = 6, column = 2, columnspan = 1)
        entryf = Entry(inputframe1, validate="key", validatecommand=(vcmdf, '%P'))
        entryf.grid(row = 4, column = 3, columnspan = 2, sticky = W)
        entrys = Entry(inputframe1, validate="key", validatecommand=(vcmds, '%P'))
        entrys.grid(row = 5, column = 3, columnspan = 2, sticky = W)
        entrys = Entry(inputframe1, validate="key", validatecommand=(vcmds, '%P'))
        entrys.grid(row = 6, column = 3, columnspan = 2, sticky = W)
        infoaddB = Button(inputframe1, text = 'Add', command = lambda: self.add(self.entered_1, self.entered_2, self.entered_3))
        infoaddB.grid(row = 7, column = 2, columnspan = 1, sticky = N)
        inforemoveB = Button(inputframe1, text = 'Remove', command =lambda:  self.remove(self.entered_1, self.entered_2,self.entered_3))
        inforemoveB.grid(row = 7, column = 3, columnspan = 1, sticky = N)
        self.inputedframe1 = LabelFrame(self.labelframe2, text = 'Inputed known info')
        self.inputedframe1.grid(row = 8, rowspan = 100, column = 2, columnspan = 4, sticky = W+N+E+S)
        predictionB = Button(self.labelframe2, text = 'Predict', command = self.predict)
        predictionB.grid(row = 3, column = 8, columnspan = 4, sticky = N+W+E)
        self.predictionframe = LabelFrame(self.labelframe2, text = 'Prediction')
        self.predictionframe.grid(row = 4, column = 6, columnspan = 80, sticky = W)
    def validate1(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_1 = ''
            return True
        try:
            self.entered_1 = new_text
            return True
        except ValueError:
            return False
    def validate3(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_3 = ''
            return True
        try:
            self.entered_3 = new_text
            return True
        except ValueError:
            return False
    def validate2(self, new_text):
        '''
        test the validity of the filename inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_2 = ''
            return True
        try:
            self.entered_2 = new_text
            return True
        except ValueError:
            return False
    def predict(self):
        self.twolist = self.DT.eval(self.twolist)
        labelist2= []
        for i in range(len(self.twolist)):
            labelist2+= [Label(self.predictionframe, text = 'Info-'+str(i) +' - '
                               + str(self.twolist[i][0]) + '('+self.odlist[0]+')')]
            labelist2[i].grid(column = 6, columnspan = 2, sticky= W)
    def add(self, f, s,t):
        if f!= '' and s!= '' and t!= '':
            self.twolist += [[None, f, s, t]]
        if self.twolist != []:
            self.labelist = []
            for i in range(len(self.twolist)):
                self.labelist+=[Label(self.inputedframe1, text = 'Info-'+str(i) + ': \n        ' +
                      self.odlist[1] + ': ' + str(self.twolist[i][1]) + ' '+ self.odlist[2] +
                      ': ' + str(self.twolist[i][2]) + ' ' + self.odlist[3] + ': ' + str(self.twolist[i][3]))]
                self.labelist[i].grid(column = 3, columnspan = 4, sticky = W)
    #pca
    def pcaF(self):
        self.forget(2)
        pcaframe = LabelFrame(self.root)
        pcaframe.grid(columnspan = 5, sticky = E+W+S+N)
        nL = Label(bottomNframe, text = 'Please enter N for BottomN')
        vcmd = self.root.register(self.validate)
        n = Entry(bottomNframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(bottomNframe, text = 'Enter', command = lambda: self.getResultBottom(n))
        nL.grid()
        n.grid()
        upB.grid()
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
        elif len(GUI.charInfo) != len(GUI.fileName):
            for i in range(len(GUI.fileName) - len(GUI.charInfo)):
                GUI.charInfo.append([None, None, None])
        self.genreF()
        self.printInputs()
    def printInputs(self):
        inputframe = LabelFrame(self.root, text = 'Inputs')
        inputframe.grid(row = 2, column = 2, sticky = W+E+N+S, columnspan = 3)
        Label(inputframe, text = ' ').grid(row = 2, column = 3)
        Label(inputframe, text = 'Genre').grid(row = 2, column = 4)
        Label(inputframe, text = 'Year').grid(row = 2, column = 5)
        Label(inputframe, text = 'Topics').grid(row = 2, column = 6)
        for i in range(len(GUI.charInfo)):
            Label(inputframe, text = GUI.fileName[i]).grid(row = i + 3, column = 3)
            Label(inputframe, text = GUI.charInfo[i][0]).grid(row = i + 3, column = 4)
            Label(inputframe, text = GUI.charInfo[i][1]).grid(row = i + 3, column = 5)
            Label(inputframe, text = GUI.charInfo[i][2]).grid(row = i + 3, column = 6)
    def genreF(self):
        self.forget(2)
        self.printInputs()
        genreFrame = LabelFrame(self.root, text = 'Genre')
        genreFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
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
        self.printInputs()
        yearFrame = LabelFrame(self.root, text = 'Year')
        yearFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
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
        self.printInputs()
        topicsFrame = LabelFrame(self.root, text = 'Topics')
        topicsFrame.grid(row = 2, column = 0, sticky = W+E+N+S, columnspan = 2)
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
        if GUI.charInfo == []:
            for i in range(len(GUI.fileName)):
                GUI.charInfo.append([None, None, None])
        elif len(GUI.charInfo) != len(GUI.fileName):
            for i in range(len(GUI.fileName) - len(GUI.charInfo)):
                GUI.charInfo.append([None, None, None])
        for i in range(len(variables)):
            if variables[i].get() == 1:
                GUI.charInfo[i][infoType] = info.get()
        self.printInputs()

class statsF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        topNB = Button(text = 'TopN', command = self.topNF)
        bottomNB = Button(text = 'BottomN', command = self.bottomNF)
        printStatsB = Button(text = 'Display Statistics', command = self.printStatsF)
        printStatsB.grid(row = 1, column = 0)
        topNB.grid(row = 1, column = 1)
        bottomNB.grid(row = 1, column = 2)
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
        upB = Button(topNframe, text = 'Enter', command = lambda: self.getResultTop(n))
        nL.grid()
        n.grid()
        upB.grid()
    def bottomNF(self):
        self.forget(2)
        bottomNframe = LabelFrame(self.root, text = 'BottomN')
        bottomNframe.grid(columnspan = 5, sticky = E+W+S+N)
        nL = Label(bottomNframe, text = 'Please enter N for BottomN')
        vcmd = self.root.register(self.validate)
        n = Entry(bottomNframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(bottomNframe, text = 'Enter', command = lambda: self.getResultBottom(n))
        nL.grid()
        n.grid()
        upB.grid()
    def getResultTop(self, n):
        self.N = int(n.get())
        for m in range(len(GUI.fileObj)):
            worddict = BasicStats.createFreqMap(GUI.fileObj[m].wordlist)
            [maxlistn, maxlists, minlistn, minlists] = BasicStats.HTopNBottomN(worddict, self.N)
            MatPlotPloter().barGraphfortop(maxlists[1:], maxlistn[1:], GUI.fileName[m])
    def getResultBottom(self, n):
        self.N = int(n.get())
        for m in range(len(GUI.fileObj)):
            worddict = BasicStats.createFreqMap(GUI.fileObj[m].wordlist)
            [maxlistn, maxlists, minlistn, minlists] = BasicStats.HTopNBottomN(worddict, self.N)
            MatPlotPloter().barGraphfortop(minlists[1:], minlistn[1:], GUI.fileName[m])

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
