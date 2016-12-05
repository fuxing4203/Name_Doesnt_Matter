from DocumentStreamError import DocumentStreamError

class DocumentStream:
    def __init__(self):
        '''
        initiate self.text and self.slist(sentence list)
        '''
        self.text = ''
        self.slist = []
        self.firstline = ''

    def readfile(self, filename):
        '''
        read file to self.text if no error occurred
        or print Error Message
        '''
        result = DocumentStreamError.existFileName(filename)
        if result == "Pass":
            file = open(filename,'r')
            self.firstline = file.readline()
            self.text = file.read()
            file.close()
        else:
            print("Error occurred when openning file")

    def readWhole(self, filename):
        '''
        from self.text split the text into the a list of sentences
        identified by !.?; or more than one space
        '''
        DocumentStream.readfile(self, filename)
        charindex = -1
        strlist = ''
        for i in self.text:
            charindex += 1
            strlist += i
            if i in '!.?; ':
                if charindex == len(self.text) - 1:
                    self.slist.append(strlist)
                    break
                elif i == ' ':
                    if charindex == 0:
                        strlist = ''
                        continue
                    elif self.text[charindex + 1] != ' ' and self.text[charindex - 1] not in '!.?; ':
                        continue
                    elif self.text[charindex + 1] == ' ':
                        strlist = strlist[:-1]
                    elif self.text[charindex - 1] in '!.?;':
                        strlist = ''
                        continue
                if strlist != '':
                    self.slist.append(strlist)
                    strlist = ''
        return self.slist

    def writeWhole(self, filename):
        '''
        write the text one sentence per line into a file called
        out + filename
        '''
        text = ""
        for i in self.slist:
            text = text + i + "\n"
        result = DocumentStreamError.existFileName(filename)
        if result == "Pass":
            file = open("out" + filename,"w")
            file.write(text)
            file.close()

    def parsetitleauthor(self,filename):
        '''
        analyze and parse the name of the author and the book out
        input the filename
        out put a list [Bookname, authorname]
        '''
        info = self.firstline
        info.strip('The Project Gutenberg EBook of ')
        firstbooksecondauthor = info.split(',')
        return firstbooksecondauthor

    def getauthor(self, filename):
        #slice and return the proper author
        return self.parsetitleauthor(filename)[1][4:-1]
