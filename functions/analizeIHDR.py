#!/usr/bin/python3

# Imported enum type
from enum import Enum

# Function that analizes the IHDR chunk
def analizeIHDR (hexArray):
    position = hexArray.find("49484452")

    # The find() method returns the index
    # of first occurrence of the substring (if found).
    # If not found, it returns -1

    if position!=-1:
        print("1. IHDR found")
        position += 8

        width = hexArray[position:position+8]
        widthDecimal = int(width,16)
        position+=8

        print("\n######################")
        print("# Reading IHDR chunk #")
        print("######################")

        ########################################################
        # Width and height give the image dimensions in pixels #
        # First 8 bytes of this chunk                          #
        #########################################################
        var = "\nWidth : " + str(widthDecimal)
        print(var)

        height = hexArray[position:position+8]
        heightDecimal = int(height,16)
        position += 8

        var = "Height : " + str(heightDecimal)
        print(var)

        ########################################################
        # Next byte is bit depth                               #
        # integer giving the number of bits per sample         #
        # or per palette index (not per pixel)                 #
        ########################################################

        bitDepth = hexArray[position:position+2]
        bitDepthDecimal = int(bitDepth,16)
        position+=2

        var = "Bit depth : " + str(bitDepthDecimal)
        print(var)

        ########################################################
        # Next byte is colour type                             #
        # variants are saved in enum below                     #
        ########################################################

        class colourTypeEnum (Enum):
            GREYSCALE = 0
            TRUECOLOUR = 2
            INDEXED_COLOUR = 3
            GREYSCALE_WITH_ALPHA = 4
            TRUECOLOUR_WITH_ALPHA = 6

        colourType = hexArray[position:position+2]
        colourTypeDecimal = int(colourType,16)
        position+=2

        tmpInt = colourTypeDecimal

        var = "Colour type : " + str(colourTypeEnum(tmpInt).name)
        print(var)

        ########################################################
        # Next byte is compression method                      #
        # variants are saved in enum below                     #
        # All conforming PNG images shall be compressed with   #
        # method 0 (deflate/inflate compression with a         #
        # sliding window of at most 32768 bytes)               #
        ########################################################

        class compressionMethodEnum (Enum):
            DEFLATE_INFLATE = 0

        compressionMethod = hexArray[position:position+2]
        compressionMethodDecimal= int(compressionMethod,16)
        position+=2

        tmpInt = compressionMethodDecimal

        var = "Compression method : " + str(compressionMethodEnum(tmpInt).name)
        print(var)

        ########################################################
        # Next byte is filter method                           #
        # variants are saved in enum below                     #
        ########################################################

        class filterMethodEnum (Enum):
            NONE = 0
            SUB = 1
            UP = 2
            AVERAGE = 3
            PAETH = 4

        filterMethod = hexArray[position:position+2]
        filterMethodDecimal= int(filterMethod,16)
        position+=2

        tmpInt = filterMethodDecimal

        var = "Filter method : " + str(filterMethodEnum(tmpInt).name)
        print(var)

        ########################################################
        # Next byte is interlace method                        #
        # variants are saved in enum below                     #
        # method 0, the null method, method 1 = Adam7 method   #
        ########################################################

        class interlaceMethodEnum (Enum):
            NULL = 0
            ADAM7 = 1

        interlaceMethod = hexArray[position:position+2]
        interlaceMethodDecimal= int(interlaceMethod,16)

        tmpInt = interlaceMethodDecimal

        var = "Interlace method : " + str(interlaceMethodEnum(tmpInt).name)
        print(var)

    else:
        print("1. IHDR not found")
