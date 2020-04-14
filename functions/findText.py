#!/usr/bin/python3

# Imported libraries
import codecs

# Function that finds tEXt chunk
def findText (hexArray):
    position = hexArray.find("74455874")

    if position != -1:
        print("\n7. tEXtfound")

        print("\n######################")
        print("# Reading tEXt chunk #")
        print("######################")

        length_pos = position - 8
        length_str = hexArray[length_pos:position]
        length = int(length_str, 16)
        position_data = position + 8
        chunk_data = codecs.decode(hexArray[position_data:position_data+ length*2], "hex").decode('utf-8')
        print("\ntEXt Content: \n " + chunk_data)

    else :
        print("\n7. tEXt not found")
