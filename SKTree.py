####################################################################################################################################################################
# Name: Ryan Pencak
# Class: SKTree
# Summary: This class contains the SK Tree. It is initialized with a tree, labels, and a depth variable. It has methods to train the tree, evaluate using the tree, and also convert the data to dots.
####################################################################################################################################################################


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from skleran.tree import export_graphviz


class SKTree:


    # Initializes the SKTree object
    # Precondition: None
    # Postcondition: Initializes the class object with a tree, labels, and a depth
    
    def __init__(self):
        self.tree = None
        self.labels = None
        self.depth = None


    # Trains the SKTree
    # Precondition: 2D list of data, list of labels, and maximum depth of the tree
    # Postcondition: Trains the SKTree
    
    def train(self, data, labels, depth):
        """We assume that data is a 2D python list, the target in colum 0"""
        self.labels = labels
        self.depth = depth
        
        x = [None]*len(data)
        y = [None]*len(data)

        for row in range(len(data)):
            y[row] = data[row][0]
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t


        self.tree = DecisionTreeClassifier(criterion="entropy", max_depth=depth, random_state=0)
        self.tree = self.tree.fit(x,y)


    # Evaluates the SKTree
    # Precondition: 2D list of data
    # Postcondition: Evaluates the SKTree as y using predict
    
    def eval(self, data):
        """We assume that data is a 2D python list, with the target [0] == None"""

        x = [None]*len(data)
        for row in range(len(data)):
            t = []
            for col in range(1,len(data[row])):
                t += [data[row][col]]
            x[row] = t

        y = self.tree.predict(y)
        #Now you will have to get the values from y and move them to the targe column of data


    # Converts data to dots
    # Precondition: Takes in a valid filename
    # Postcondition: Assigns dot data
    
    def toDot(self, filename):
        dot_data = export_graphviz(self.tree, out_file=filename, feature_names=self.labels)
        
    
    # Converts data to ordinal format
    # Precondition: Takes in list of data
    # Postcondition: Returns a list of converted data
    
    def ordinal():
        pass
        
        
