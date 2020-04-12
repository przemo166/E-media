#!/usr/bin/python3

# Imported libraries to load image and make a Fourier transformation
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# A Fourier transform function
def fourierTransform (imageName):

        image = Image.open('example_files/{}'.format(imageName))
        imageData = np.asarray(image)
        fourier = np.fft.fft2(imageData)
        fourier = np.fft.fftshift(fourier)
        fourier=abs(fourier)
        fourier=np.log10(fourier)
        lowest=np.nanmin(fourier[np.isfinite(fourier)])
        highest=np.nanmax(fourier[np.isfinite(fourier)])
        orginalRange=highest-lowest
        normFourier= (fourier-lowest)/orginalRange*255
        normFourierImage = Image.fromarray(normFourier)

        fig = plt.figure()
        ax1 = fig.add_subplot(111)
        ax1.imshow(normFourierImage)
        ax1.title.set_text("Fourier transform")
        plt.show()
