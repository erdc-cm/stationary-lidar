import numpy as np
import scipy as sp
import scipy.io
import h5py


def readLinescanData(laserdatFilename):
    """
    This function reads a laserdat.mat file and imports it into python as a _______________

    """
    return h5py.File(laserdatFilename,'r')


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

