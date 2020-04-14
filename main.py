#!/usr/bin/python3

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("functions"))
from bytesArray import *
from showImage import *
from fourierTransform import *
from checkSignature import *
from analizePLTE import *
from analizeIHDR import *
from readIDAT import *

####################
#   Main file      #
####################

# A variable for our image name
imageName = input("File name : ")
# A variable to check if our file is png file
x = checkPng(imageName)

# Further actions (if we have a png file)
if x==True:
    print("Signature ok\n")
    hexArray = imageConvert(imageName)
    # Analizing critical chunks
    analizeIHDR(hexArray)
    analizePLTE(hexArray)
    readIDAT(hexArray)
    # end
    showImage(imageName)
    fourierTransform(imageName)

# If our file is not png file we do nothing
else :
    print("Signature fail")
