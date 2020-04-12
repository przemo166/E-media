#!/usr/bin/python3

# Imported enum type
from enum import Enum

# Function that analizes the IHDR chunk
def analizeIHDR (hexArray):
    position = hexArray.find("49484452")
    position += 8

    width = hexArray[position:position+8]
    widthDecimal = int(width,16)
    position+=8

    print("\nReading IHDR chunk")

    ########################################################
    # Width and height give the image dimensions in pixels #
    # First 8 bytes of this chunk                          #
    ########################################################
    var = "Width : " + str(widthDecimal)
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

    class colorType (Enum):
        GREYSCALE = 0
        TRUECOLOUR = 2
        INDEXED_COLOUR = 3
        GREYSCALE_WITH_ALPHA = 4
        TRUECOLOUR_WITH_ALPHA = 6

    colourType = hexArray[position:position+2]
    colourTypeDecimal = int(colourType,16)
    position+=2

    tmpInt = colourTypeDecimal

    var = "Colour type : " + str(colorType(tmpInt))
    print(var)



    
