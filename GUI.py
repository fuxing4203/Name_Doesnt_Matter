from tkinter import *
class GUI:
    #for now text filters and upload are finished
    #charInfo is half way finished
    fileName = []
    filters = []
    charInfo = [] #[[position of filename, genre, year]]
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
        nws = Button(labelframe, text = 'Nomralize White Space', command = lambda: GUI.filters.append('NWS'))
        nc = Button(labelframe, text = 'Normalize Cases', command = lambda: GUI.filters.append('NC'))
        snc = Button(labelframe, text = 'Strip Null Characters', command = lambda: GUI.filters.append('SNC'))
        sn = Button(labelframe, text = 'Strip Numbers', command = lambda: GUI.filters.append('SN'))
        fw = Button(labelframe, text = 'Strip Null Characters', command = lambda: GUI.filters.append('SNC'))
        fw = Button(labelframe, text = 'Filter Words', command = lambda: GUI.filters.append('FW'))
        nws.grid(sticky = 'W')
        nc.grid(sticky = 'W')
        snc.grid(sticky = 'W')
        sn.grid(sticky = 'W')
        fw.grid(sticky = 'W')


class predictF(GUI):
    def __init__(self):
        super().__init__(root)
        self.forget()
        labelframe = LabelFrame(self.root)
        labelframe.grid(columnspan = 100)
        left = Label(labelframe, text='Predictions')
        left.pack()

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
        fileNameL = Label(genreFrame, text = 'Please enter the file name.')
        fileName = Entry(genreFrame, validate="key", validatecommand=(vcmd, '%P'))
        genreL = Label(genreFrame, text = 'Please enter the genre.')
        genre = Entry(genreFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(genreFrame, text = 'Add', command = lambda: self.getResult(fileName, genre))
        fileNameL.grid()
        fileName.grid()
        genreL.grid()
        genre.grid()
        upB.grid()

    def yearF(self):
        self.forget(2)
        yearFrame = LabelFrame(self.root, text = 'Year')
        yearFrame.grid(columnspan = 100)
        vcmd = self.root.register(self.validate)
        fileNameL = Label(yearFrame, text = 'Please enter the file name.')
        fileName = Entry(yearFrame, validate="key", validatecommand=(vcmd, '%P'))
        yearL = Label(yearFrame, text = 'Please enter the year.')
        year = Entry(yearFrame, validate="key", validatecommand=(vcmd, '%P'))
        upB = Button(yearFrame, text = 'Add', command = lambda: self.getResult(fileName, year, 2))
        fileNameL.grid()
        fileName.grid()
        yearL.grid()
        year.grid()
        upB.grid()

    def getResult(self, fileName, info, infoType = 1):
        if self.findFilenamePos(fileName):
            pos = GUI.fileName.index(fileName.get())
            updated = False
            for item in GUI.charInfo:
                if item[0] == pos:
                    item[infoType] = info.get()
                    updated = True
                    break
            if not updated:
                if infoType == 1:
                    GUI.charInfo.append([pos, info.get(), None])
                else:
                    GUI.charInfo.append([pos, None, info.get()])

    def findFilenamePos(self, fileName):
        try:
            pos = GUI.fileName.index(fileName.get())
            return True
        except ValueError:
            print('Invalid file name entered.')
            return False

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
        fileNameL.grid()
        fileName.grid(columnspan = 10)
        upB.grid()
        self.printFileNames()

    def printFileNames(self):
        self.forget(2)
        for item in GUI.fileName:
            Label(root, text = item).grid()

    def getResult(self, fileName):
        GUI.fileName.append(fileName.get())
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
