####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Text Filter
# Summary: The Text Filter class contains the filters that can be applied to text files. It is initialized with a doc and a list of filters. It includes methods (filters) that normalize white space, normalize case, strip null characters, strip numbers, and strip common words. It also has a method that will apply filters in the order that a user inputs them.
####################################################################################################################################################################


from Document import *


class TextFilter:
    
    
    # Initializes the TextFilter class
    # Precondition: Takes in a document and list of filters
    # Postcondition: Initializes the TextFilter object with a document, list of filters plist, and sentence list using generateWhole from document
    
    def __init__(self, doc, plist):
        self.doc = doc
        self.plist = plist
        self.sentenceList = doc.generateWhole


    # Gets sentenceList from doc, iterates through, and checks number of spaces in sentence list and replaces them with one space
    # Precondition: Called on a TextFilter object
    # Postcondition: Updates sentenceList with normalized white spaces
    
    def normalizeWhitespace(self):
        for sentence in self.sentenceList:
            tempList = []
            for ch in sentence.data:
                if ch != " ":
                    tempList.append(ch)
                if ch == " ":
                    while (ch == " "):
                        ch += 1
                    tempList.append(" ")

            self.sentenceList[sentence] = tempList


    # Normalizes the case in the sentenceList, making them all lower case
    # Precondition: Called on a TextFilter object
    # Postcondition: Updates sentenceList with normalized case (all lower case)
    
    def normalizeCase(self):
        tempList = []
        for sentence in self.sentenceList:
            tempList = []
            for ch in sentence.data:
                tempList.append(ch.lower())

            self.sentenceList[sentence] = tempList

        return self.sentenceList

        tempDoc = ""

        for ch in doc:
            tempDoc += ch.lower()

        doc = tempDoc


    # Strips the null characters from the sentenceList
    # Precondition: Called on a TextFilter object
    # Postcondition: Updates sentenceList of printable non null characters only
    
    def stripNullCharacters(self):
        printable = (x for x in doc if 31 < ord(x) < 127)
        self.sentenceList = printable


    # Strips the numbers from the sentenceList
    # Precondition: Called on a TextFilter object
    # Postcondition: Updates sentenceList without numbers
    
    def stripNumbers(self):
        printable = (x for x in doc if 0 < ord(x) < 48 and 57 < ord(x) < 128)
        self.sentenceList = printable


    # Strips common words from the sentenceList
    # Precondition: Called on a TextFilter object and there must be a filterwords.txt file in the program folder
    # Postcondition: Updates the sentenceList to have no numbers
    
    def stripCommonWords(self):
        filterWords = []
        with open(filterwords.txt) as f:
            for line in f:
                for word in line.split():
                    filterWords.append(word)

        for sentence in self.sentenceList:
            for docWord in sentence:
                for fWord in filterWords:
                    if docWord == fWord:
                        self.sentenceList.remove(docWord)
                        

    # Applies the filter in the order given in the pList
    # Precondition: Called on a TextFilter object
    # Postcondition: Applies each of the filters in pList to the document
    
    def apply(self):
        for i in plist:
            if i == "normalizeWhitespace":
                doc.normalizeWhitespace
            if i == "normalizeCase":
                doc.normalizeCase
            if i == "stripNullCharacters":
                doc.stripNullCharacters
            if i == "stripNumbers":
                doc.stripNumbers
            if i == "stripCommonWords":
                doc.stripCommonWords
