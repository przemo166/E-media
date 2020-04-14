#!/usr/bin/python3

# Function that reads what IDAT chunk contains
def readIDAT (hexArray):
    position = hexArray.find("49444154")

    # The find() method returns the index
    # of first occurrence of the substring (if found).
    # If not found, it returns -1

    if position!=-1:
        print("\n3. IDAT found")

        print("\n######################")
        print("# Reading IDAT chunk #")
        print("######################")

        ##############################################################
        # The IDAT chunk contains the actual image data which is the #
        # output stream of the compression algorithm                 #
        ##############################################################

        chunkLenght = hexArray[(position-8):position]
        chunkLenghtDecimal = int(chunkLenght,16)
        position+=8

        i = 0

        print("\n")

        f = open("data/data_IDAT_chunk.txt", "w")

        while i < chunkLenghtDecimal:

            tmpHex = hexArray[position:position+2]
            position+=2

            var = str(tmpHex) + " "
            f.write( var )

            i+=1

        f.close()

        print("Output saved in a .txt file in /data directory\n")

    else:
        print("\n3. IDAT not found")
