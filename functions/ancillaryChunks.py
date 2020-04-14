#!/usr/bin/python3

# Importing files from current directory
import sys
import os
sys.path.append(os.path.abspath("/"))
from findTime import *
from findGamma import *

# Function that finds ancillaryChunks
def findAncillary (hexArray):

    # Finding tIME chunk function
    findTime(hexArray)

    # Finding gAMA chunk function
    findGamma(hexArray)
