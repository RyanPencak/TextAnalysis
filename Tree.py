####################################################################################################################################################################
# Name: Ryan Pencak
# Class: Decision Tree Node, Tree
# Summary: The Decision Tree Node class is the node for the tree class and is initialized with a left child, right child, an attribute, and a document count. The Tree class is a tree data structure for the program that uses the ID3 algorithm. It has methods train, evaluate, gain, and ID3.
####################################################################################################################################################################


import pandas as pd
import numpy as np


class DecisionTreeNode:
    
    
    # Initializes the Decision Tree Node
    # Precondition: None
    # Postcondition: Initializes class
    
    def __init__(self, attribute):
        self.left = None
        self.right = None
        self.attribute = attribute
        self.docCount = 0




class Tree:
    
    
    # Initializes a Tree object
    # Precondition: None
    # Postcondition: Initializes class
    
    def __init__(self):
        pass


    # Trains the tree
    # Precondition: 2D List of data, 1D list of column titles, maximum depth integer
    # Postcondition: Assigns root to ID3
    
    def train(self, data, titles, depth):
        root = None
        root = ID3(data, titles, depth)


    # Evaluates the tree and assigns the first column values
    # Precondition: 2D list of data
    # Postcondition: Tree assigns the first column values
    
    def eval(data):
        pass


    # Calculates the gain
    # Precondition: Variables X, T, and a list of attributes
    # Postcondition: Returns ID3 of data T
    
    def gain(X, T, attributes):
        ID3(T, attributes-X):


    # ID3 algorithm method
    # Precondition: List of data and input attributes
    # Postcondition: Computes the ID3 algorithm
    
    def ID3(data, attributes):
        if(data.isEmpty):
            return None

        if(data[0:,0].getAuthor() == data[1:,0].getAuthor()):
            return data[0,0].getAuthor()

        if(attributes.isEmpty):
            return DecisionTreeNode(data[0,0].getAuthor())
            
            
    # Converts data to ordinal format
    # Precondition: Takes in list of data
    # Postcondition: Returns a list of converted data
    
    def ordinal():
        pass
