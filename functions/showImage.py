#!/usr/bin/python3

# Importing modules to show .png image
from PIL import Image

# Function that shows our image
def showImage(imageName):
    img = Image.open('example_files/{}'.format(imageName))
    img.show(title="Image")
