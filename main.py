#!/usr/bin/python3

# Importing files from directory /functions
import sys
import os
sys.path.append(os.path.abspath("/home/przemek/Pulpit/E-media_repo/E-media/functions"))
from analizeIHDR import *
from bytesArray import *
from showImage import *

####################
#   Main file      #
####################

# A variable for our image name
imageName = input("File name : ")

bytesArray = imageConvert(imageName)
#showImage(imageName)
#print(bytesArray)
analizeIHDR(bytesArray)
