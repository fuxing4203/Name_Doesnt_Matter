from tkinter import *
class GUI:
    #for now text filters and upload are finished
    #charInfo is half way finished
    fileName = []
    filters = [] #[[filters]]
    charInfo = [] #[[genre, year]]
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

class textFiltersF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(root, text = 'Text Filters, Click to Apply')
        labelframe.grid(columnspan = 100)
        variables = []
        for i in range(len(GUI.fileName)):
            var = IntVar()
            Checkbutton(labelframe, text = GUI.fileName[i], variable = var, onvalue = 1, offvalue = 0).grid()
            variables.append(var)
        nws = Button(labelframe, text = 'Nomralize White Space', command = lambda: self.appendFilters(variables, 'NWS'))
        nc = Button(labelframe, text = 'Normalize Cases', command = lambda: self.appendFilters(variables, 'NC'))
        snc = Button(labelframe, text = 'Strip Null Characters', command = lambda: self.appendFilters(variables, 'SNC'))
        sn = Button(labelframe, text = 'Strip Numbers', command = lambda: self.appendFilters(variables, 'SN'))
        fw = Button(labelframe, text = 'Strip Null Characters', command = lambda: self.appendFilters(variables, 'SNC'))
        fw = Button(labelframe, text = 'Filter Words', command = lambda: self.appendFilters(variables, 'FW'))
        nws.grid(sticky = 'W')
        nc.grid(sticky = 'W')
        snc.grid(sticky = 'W')
        sn.grid(sticky = 'W')
        fw.grid(sticky = 'W')

    def appendFilters(self, variables, keyword):
        if GUI.filters == []:
            for i in range(len(GUI.fileName)):
                GUI.filters.append([])
        for i in range(len(variables)):
            if variables[i].get() == 1:
                GUI.filters[i].append(keyword)

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
        genreB.grid(row = 1, column = 0)
        yearB.grid(row = 1, column = 1)
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
        yearL = Label(yearFrame, text = 'Please enter the year.')
        year = Entry(yearFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(yearFrame, text = 'Add', command = lambda: self.getResult(variables, year, 2))
        yearL.grid()
        year.grid()
        upB.grid()

    def getResult(self, variables, info, infoType = 1):
        if GUI.charInfo == []:
            for i in range(len(GUI.fileName)):
                GUI.charInfo.append([None, None])
        for i in range(len(variables)):
            if variables[i].get() == 1:
                GUI.charInfo[i][infoType] = info.get()

    def validate(self, new_text):
        '''
        test the validity of the information inputed
        '''
        if not new_text: # the field is being cleared
            self.entered_key = ''
            return True

        try:
            self.entered_key = new_text
            return True
        except ValueError:
            return False

class statsF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(columnspan = 100)
        left = Label(labelframe, text='Statistics')
        left.pack()


class upLoadF(GUI):
    #main buttons
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(columnspan = 100)
        fileNameL = Label(labelframe, text = 'Please enter the file name.')
        vcmd = self.root.register(self.validate)
        fileName = Entry(labelframe, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(labelframe, text = 'Upload', command = lambda: self.getResult(fileName))
        removeB = Button(labelframe, text = 'Remove', command = lambda: self.removeResult(fileName))
        fileNameL.grid()
        fileName.grid(columnspan = 10)
        upB.grid()
        removeB.grid()
        self.printFileNames()

    def printFileNames(self):
        self.forget(2)
        Label(self.root, text = 'Uploaded Files').grid(columnspan = 3)
        for item in GUI.fileName:
            Label(self.root, text = item).grid()

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
        self.printFileNames()

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


root = Tk()
gui = GUI(root)
root.mainloop()
