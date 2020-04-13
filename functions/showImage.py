#!/usr/bin/python3

# Importing modules to show .png image
import cv2

# Function that shows our image
def showImage(imageName):
    img = cv2.imread('example_files/{}'.format(imageName))
    cv2.imshow('Our image',img)
