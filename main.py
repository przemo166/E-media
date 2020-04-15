#!/usr/bin/python3

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("functions"))
from bytesArray import *
from fourierTransform import *
from checkSignature import *
from analizePLTE import *
from analizeIHDR import *
from readIDAT import *
from findIEND import *
from ancillaryChunks import *
from anonimize import *
from saveNewPng import *
from check import *
from exifFinder import *

####################
#   Main file      #
####################

# A variable for our image name and new file
# (ananomized) name
imageName = input("File name : ")
newName = input("New file name : ")

# A variable to check if our file is png file
x = checkPng(imageName)

# Further actions (if we have a png file)
if x==True:

    print("Signature ok\n")
    # Converting our png image into variable
    hexArray = imageConvert(imageName)

    # Analizing critical chunks
    analizeIHDR(hexArray)
    analizePLTE(hexArray,imageName)
    readIDAT(hexArray,imageName)
    findIEND(hexArray)
    # end

    # Analizing ancillary chunks
    findAncillary(hexArray)
    # end

    # Chunk anonymisation
    terminalInfo()

    hexArray=chunkRemove(hexArray,"74455874")
    hexArray=chunkRemove(hexArray,"7A545874")
    hexArray=chunkRemove(hexArray,"74494d45")
    hexArray=chunkRemove(hexArray,"67414d41")
    # end

    # Saving a new png file (ananomized)
    savePngFile(hexArray,newName)
    # end

    # Checking if deleted chunks successfully
    checkAgain(hexArray)
    # end

    # Showing new image and fourier transform
    fourierTransform(newName)
    # end

    # Exif finding function
    findEXIF(newName)
    # end

# If our file is not png file we do nothing
else :
    print("Signature fail")
