from Document import *

class TextFilter:
    def __init__(self, doc, plist):
        self.doc = doc
        self.plist = plist

    # Get sl from doc, iterate through and check number of spaces to replace with 1 space
    def normalizeWhitespace(self):
        sl2 = []
        for sentence in sl:
            for ch in sentence.data:
                if ch != " ":
                    sl2.append(ch)
                if ch == " ":
                    while (ch == " "):
                        ch += 1
                    sl2.append(" ")

        return sl2

    def normalizeCase(self):
        #get sl
        #walk through sl, get string inside sl
        #buld second string, run over sl and add to lower version
        tempDoc = ""

        for ch in doc:
            tempDoc += ch.lower()

        doc = tempDoc

        return doc

    def stripNullCharacters(self):
        printable = (x for x in doc if 31 < ord(x) < 127)
        return printable

    def stripNumbers(self):
        printable = (x for x in doc if 0 < ord(x) < 48 and 57 < ord(x) < 128)

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

        doc.normalizeWhitespace()
        doc.normalizeCase()
        doc.stripNullCharacters()
        doc.stripNumbers()
