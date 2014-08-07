import numpy as np


def readLinescanData():
    return np.empty((10,10))


class LinescanAnalysis:

    def __init__(self):
        #This constructor makes a LinescanAnalysis Object
        self.scanData=readLinescanData()
        self.ptdat=self.createPtdat()
        self.runup=self.getRunupLine()

    def createPtdat(self):
        #This function creates organizes ptDat from scanData and pre-filters it
        return 


    def getRunupline(self):
        #This function finds the runup line from ptdat


        pass

