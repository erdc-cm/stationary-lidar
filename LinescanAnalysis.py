import numpy as np
import scipy as sp
import scipy.io


def readLinescanData(laserdatFilename):
    """
    This function reads a laserdat.mat file and imports it into python as a _______________

    """
    return sp.io.loadmat(laserdatFilename)


class LinescanAnalysis:

    def __init__(self):
        """
        This constructor makes a LinescanAnalysis Object
        """
        self.scanData=readLinescanData()
        self.ptdat=self.createPtdat()
        self.runup=self.getRunupLine()

    def createPtdat(self):
        """
        This function creates organizes ptDat from scanData and pre-filters it
        """
        return


    def getRunupline(self):
        """
        This function finds the runup line from ptdat
        """


        pass

