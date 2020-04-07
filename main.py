#!/usr/bin/python3

# Importing modules to show png image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image

####################
#   Main file      #
####################

imageName = input("File name : ")

img = Image.open('example_files/{}'.format(imageName))
img.show()
