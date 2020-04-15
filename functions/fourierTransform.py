#!/usr/bin/python3

# Imported libraries to load image and make a Fourier transformation
import cv2
import numpy as  np

# A Fourier transform function
def fourierTransform (imageName):

    img = cv2.imread('created_files//{}'.format(imageName), cv2.IMREAD_GRAYSCALE)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)
    img_and_magnitude = np.concatenate((img, magnitude_spectrum), axis=1)

    cv2.imshow('example_files/{}'.format(imageName), img_and_magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
