#!/usr/bin/python3

# Function that finds tEXt chunk
def findText (hexArray):
    position = hexArray.find("74494d45")

    if position!=-1:
        print("\n6. tEXt found")

        print("\n######################")
        print("# Reading tEXt chunk #")
        print("######################")

        position += 8

        ##############################################################
        # Each tEXt chunk contains a keyword and a text string,      #
        # in the format:                                             #
        #                                                            #
        # Keyword 	1-79 bytes (character string)                    #
        # Null separator 	1 byte (null character)                  #
        # Text string 	0 or more bytes (character string)           #
        ##############################################################

        i = 0
        j = 0

        while i !=1 :
            tmp = hexArray[position:position+2]
            tmpDecimal = int(tmp,16)
            position+=2
            j+=1

            if tmpDecimal == 0 :
                print("found")
                i=1
                print(j)

        #tmp = hexArray[position:position+(2*j)]
        #tmpName = str(tmp)
        #print(tmpName)
        #x=bytes.fromhex(tmp).decode('utf-8')
        #print(x)

    else:
        print("\n6. tEXt not found")
