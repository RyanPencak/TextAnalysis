####################################################################################################################################################################
# Name: Ryan Pencak
# Class: UserGUI
# Summary: This class contains the user interface for the program and handles all the work that would normally be done in a main class. It has methods to initialize the GUI, validate, update, read the document, run PCA evaluation, run SK Tree evaluation, run ID3 evaluation, and filter.
####################################################################################################################################################################


from tkinter import *
import TextFilter
import Document
import DocumentStream
import Sentence
import BasicStats
import MatPlotPlotter
import Sentence
# import SKPCA
# import SKTree
# import Tree


class UserGUI:

    # Initializes the GUI class with a master root and creates all the buttons and text lines for the interface
    # Precondition: Takes in a root to launch the user GUI
    # Postcondition: Creates all the button and text lines for the user interface
    
    def __init__(self, master, numFiles):
        self.master = master
        self.numFiles = numFiles
        master.title("Text Analyzer")

        self.fileDictionary = {}
        self.docDictionary = {}
        self.yearDictionary = {}
        self.genreDictionary = {}
        self.filterDictionary = {}
        self.tFilterDictionary = {}
        self.trainDictionary = {}
        self.evalDictionary = {}
        self.wordListDictionary = {}
        self.topNDictionary = {}
        self.bottomNDictionary = {}
        self.pList = {}
        self.topWords = {}
        self.bottomWords = {}
                        
        self.label1 = Label(master, text = "Documents")
        self.label1.grid(row = 0, column = 0)
        
        self.label2 = Label(master, text = "Year")
        self.label2.grid(row = 0, column = 1)
        
        self.label3 = Label(master, text = "Genre")
        self.label3.grid(row = 0, column = 2)
        
        self.label4 = Label(master, text = "Text Filters")
        self.label4.grid(row = 0, column = 3)
        
        self.label5 = Label(master, text = "Train")
        self.label5.grid(row = 0, column = 4)
        
        self.label6 = Label(master, text = "Evaluate")
        self.label6.grid(row = 0, column = 5)
        
        self.label7 = Label(master, text = "Top 10 Words")
        self.label7.grid(row = 0, column = 6)
        
        self.label8 = Label(master, text = "Bottom 10 Words")
        self.label8.grid(row = 0, column = 7)
        
        self.label9 = Label(master, text = "Analyze")
        self.label9.grid(row = 0, column = 8)
                                
        i = 0
        
        while i < self.numFiles:
            self.fileDictionary[i] = StringVar()
            self.yearDictionary[i] = StringVar()
            self.genreDictionary[i] = StringVar()
            self.filterDictionary[i] = StringVar()
            self.trainDictionary[i] = IntVar()
            self.evalDictionary[i] = IntVar()
            self.topNDictionary[i] = IntVar()
            self.bottomNDictionary[i] = IntVar()
                        
            self.entry1 = Entry(master, textvariable = self.fileDictionary[i])
            self.entry1.grid(row = i+1, column = 0, sticky = W)
            
            self.entry2 = Entry(master, textvariable = self.yearDictionary[i])
            self.entry2.grid(row = i+1, column = 1, sticky = W)
            
            self.entry3 = Entry(master, textvariable = self.genreDictionary[i])
            self.entry3.grid(row = i+1, column = 2, sticky = W)
            
            self.entry4 = Entry(master, textvariable = self.filterDictionary[i])
            self.entry4.grid(row = i+1, column = 3, sticky = W)
            
            self.check1 = Checkbutton(master, cursor = 'arrow', activebackground = 'blue', variable = self.trainDictionary[i], onvalue = 1, offvalue = 0)
            self.check1.grid(row = i+1, column = 4)
            
            self.check2 = Checkbutton(master, cursor = 'arrow', activebackground = 'blue', variable = self.evalDictionary[i], onvalue = 1, offvalue = 0)
            self.check2.grid(row = i+1, column = 5)
            
            self.check3 = Checkbutton(master, cursor = 
            'arrow', activebackground = 'blue', variable = self.topNDictionary[i], onvalue = 1, offvalue = 0)
            self.check3.grid(row = i+1, column = 6)
            
            self.check4 = Checkbutton(master, cursor = 
            'arrow', activebackground = 'blue', variable = self.bottomNDictionary[i], onvalue = 1, offvalue = 0)
            self.check4.grid(row = i+1, column = 7)
            
            i += 1        
            
                               
        PCAButton = Button(master, text = "PCA", command = self.runPCA)
        PCAButton.grid(row = 1, column = 8)
        
        SKButton = Button(master, text = "SK Tree", command = self.runSK)
        SKButton.grid(row = 2, column = 8)
        
        ID3Button = Button(master, text = "ID3 Tree", command = self.runID3)
        ID3Button.grid(row = 3, column = 8)
    
        
    # Reads documents inputted in the GUI
    # Precondition: Takes in a fileName
    # Postcondition: Returns a list of sentences

    def readDocuments(self):
        i = 0
        while i < self.numFiles:
            self.docDictionary[i] = Document(self.fileDictionary[i])
            self.docDictionary[i].generateWhole()
            self.wordListDictionary[i] = self.docDictionary[i].getWordList()
            i += 1
        print("Read Documents.")
    
    
    # Updates year in documents
    # Precondition: Must be called after readDocuments so that the dictionary of document objects has been created
    # PostCondition: Updates the year attribute of the documents
    
    def updateYear(self):

        i = 0
        while i < self.numFiles:
            self.docDictionary[i].setYear(self.yearDictionary[i])
            i += 1
        print("Updated Year.")
    
    
    # Updates year in documents
    # Precondition: Must be called after readDocuments so that the dictionary of document objects has been created
    # PostCondition: Updates the genre attribute of the documents
        
    def updateGenre(self):

        i = 0
        while i < self.numFiles:
            self.docDictionary[i].setGenre(self.genreDictionary[i])
            i += 1
        print("Updated Genre.")
    
    
    # Filters document it is used on using a TextFilter object
    # Precondition: Must be called after readDocuments so that the dictionary of document objects has been created
    # Postcondition: 

    def applyFilters(self):

        i = 0
        while i < self.numFiles:
            self.tFilterDictionary[i] = TextFilter(self.docDictionary[i], self.pList[i])
            self.tFilterDictionary[i].apply()
            i += 1
        print("Applied Filters")
    
    
    # Creates the list of filters entered by the user
    # Precondition: None
    # Postcondition: Creates pList of filters entered by the user
        
    def createPList(self):
        i = 0
        while i < self.numFiles:
            self.pList[i] = self.filterDictionary[i].split(',')
    
    
    # Stores top 10 words for documents
    # Precondition: Must be called after readDocuments so that the dictionary of document objects has been created
    # Postcondition: Stores top 10 words in dictionary
    
    def top10Words(self):
        i = 0
        while i < self.numFiles:
            stats = BasicStats()
            self.topNDictionary[i] = stats.topN(self.wordListDictionary[i], 10)

    
    # Stores bottom 10 words for documents
    # Precondition: Must be called after readDocuments so that the dictionary of document objects has been created
    # Postcondition: 
    
    def bottom10Words(self):
        i = 0
        while i < self.numFiles:
            stats = BasicStats()
            self.bottomNDictionary[i] = stats.bottomN(self.wordListDictionary[i], 10)


    # Runs and evaluates with PCA
    # Precondition: None
    # Postcondition: Evaluates the documents with PCA

    def runPCA(self):
        
        print("Running PCA...")
        self.readDocuments()
        self.updateYear()
        self.updateGenre()
        self.createPList()
        self.applyFilters()
        self.pca = SKPCA()
        
        i = 0
        while i < self.numFiles:
            
            if(self.trainDictionary[i] == 1):
                pass
                #self.pca.train(self.wordListDictionary[i], self.genreDictionary[i])
                #self.pca.train(self.wordListDictionary[i], self.yearDictionary[i])
            elif(self.evalDictionary[i] == 1):
                pass
                #self.pca.evaluate(C)
            else:
                pass


    # Runs and evaluates with SK Tree
    # Precondition: None 
    # Postcondition: Evaluates documents with SK Tree

    def runSK(self):
        
        print("Running SKButton...")
        self.readDocuments()
        self.updateYear()
        self.updateGenre()
        self.createPList()
        self.applyFilters()
        self.sk = SKTree()
        
        i = 0
        while i < self.numFiles:
            
            if(self.trainDictionary[i] == 1):
                pass
                #self.sk.train(self.wordListDictionary[i], self.genreDictionary[i])
                #self.sk.train(self.wordListDictionary[i], self.yearDictionary[i])
            elif(self.evalDictionary[i] == 1):
                pass
                #self.sk.evaluate(C)
            else:
                pass
    
    
    # Runs and evaluates with ID3
    # Precondition: None
    # Postcondition: Evaluates documents with ID3

    def runID3(self):
        
        print("Running ID3...")
        self.readDocuments()
        self.updateYear()
        self.updateGenre()
        self.createPList()
        self.applyFilters()
        self.ID3 = Tree()
        i = 0
        while i < self.numFiles:
            
            if(self.trainDictionary[i] == 1):
                pass
                #self.ID3.train(self.wordListDictionary[i], self.genreDictionary[i])
                #self.ID3.train(self.wordListDictionary[i], self.yearDictionary[i])
            elif(self.evalDictionary[i] == 1):
                pass
                #self.ID3.evaluate(C)
            else:
                pass
