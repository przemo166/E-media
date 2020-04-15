#!/usr/bin/python3

# Importing modules to show .png image
import cv2

# Function that shows our image
def showImage(imageName):
    img = cv2.imread('created_files/{}'.format(imageName))
    cv2.imshow('created_files/{}'.format(imageName),img)
