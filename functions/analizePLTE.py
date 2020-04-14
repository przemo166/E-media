#!/usr/bin/python3

# Imported enum type
from enum import Enum

# Function that analizes the PLTE chunk
def analizePLTE (hexArray):
    position = hexArray.find("504c5445")

    # The find() method returns the index
    # of first occurrence of the substring (if found).
    # If not found, it returns -1

    if position!=-1:
        print("\n2. PLTE found")

        print("\n######################")
        print("# Reading PLTE chunk #")
        print("######################")

        #############################################################
        # The PLTE chunk contains from 1 to 256 palette entries,    #
        # each a three-byte series of the form:                     #
        #                                                           #
        # Red:   1 byte (0 = black, 255 = red)                      #
        # Green: 1 byte (0 = black, 255 = green)                    #
        # Blue:  1 byte (0 = black, 255 = blue)                     #
        #                                                           #
        # The number of entries is determined from the chunk        #
        # length. A chunk length not divisible by 3 is an error.    #
        #############################################################

        chunkLenght = hexArray[(position-8):position]
        chunkLenghtDecimal = int(chunkLenght,16)
        position+=8

        i = 0

        print("\n")

        f = open("data/data_PLTE_chunk.txt", "w")

        while i < chunkLenghtDecimal/3:

            tmpRed = hexArray[position:position+2]
            tmpRedDecimal = int(tmpRed,16)
            position+=2

            tmpGreen = hexArray[position:position+2]
            tmpGreenDecimal = int(tmpGreen,16)
            position+=2

            tmpBlue = hexArray[position:position+2]
            tmpBlueDecimal = int(tmpBlue,16)
            position+=2

            var = "Palete entry " + str(i) + " " + "| Red : " + str(tmpRedDecimal) + " Green : " + str(tmpGreenDecimal) + " Blue : " + str(tmpBlueDecimal) + " |"
            f.write( var + "\n"  )

            i+=1

        f.close()

        print("Entries saved in a .txt file in /data directory\n")

    else:
        print("\n2. PLTE not found")
