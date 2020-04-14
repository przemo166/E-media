#!/usr/bin/python3

# Function that finds IEND chunk
def findIEND (hexArray):
    position = hexArray.find("49454e44")

    # The find() method returns the index
    # of first occurrence of the substring (if found).
    # If not found, it returns -1

    if position!=-1:
        print("\nIEND found")

        print("\n######################")
        print("# Reading IEND chunk #")
        print("######################")

        ##############################################################
        # The IEND chunk marks the end of the PNG datastream.        #
        # The chunk's data field is empty.                           #
        ##############################################################

        chunkLenght = hexArray[(position-8):position]
        chunkLenghtDecimal = int(chunkLenght,16)
        position+=8

        var = "\nChunk lenght : " +str(chunkLenghtDecimal) + "\n"
        print(var)

    else:
        print("\nIEND not found")
