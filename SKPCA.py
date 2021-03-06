####################################################################################################################################################################
# Name: Ryan Pencak
# Class: SKPCA
# Summary: This class contains the PCA function. It is initialized with pca_h, ncomp, labels, and X. It has methods to train the PCA and evaluate using PCA.
####################################################################################################################################################################


import pandas as pd
import numpy as np
from sklearn import decomposition


class SKPCA:


    # Initializes the SKPCA object
    # Precondition: None
    # Postcondition: Initializes the SKPCA object with a pca_h, ncomp, labels, and X
    
    def __init__(self):
        self.pca_h = None
        self.ncomp = 0
        self.labels = None
        self.X = None


    # Trains the PCA tree
    # Precondition: 2D List data, list of labels where sample came from, ncomp variable
    # Postcondition: Trains the PCA
    
    def train(self, data, labels, ncomp):
        """Data is a 2d data list.
           Each row in the 2dlist is sample (all samples probably of a word)
           The first column is the label idenity the sample ("A")
           labels are where the sample came frome, such as from JamesJoyce sisters
        """
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
    
    
    # Evalutates the PCA
    # Precondition: Takes in C to be evaluated
    # Postcondition: Uses the built in transform function to evaluate the PCA
    
    def evaluate(C):
        D = C.transform()
        

    # Converts data to ordinal format
    # Precondition: Takes in list of data
    # Postcondition: Returns a list of converted data
    
    def ordinal():
        pass
