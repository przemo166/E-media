#!/usr/bin/python3

# Function that finds tEXt chunk
def findGamma (hexArray):
    position = hexArray.find("67414d41")

    if position!=-1:
        print("\n6. gAMA found")

        print("\n######################")
        print("# Reading gAMA chunk #")
        print("######################")


        #################################################################
        # The gAMA chunk specifies the relationship between the image   #
        # samples and the desired display output intensity.             #
        #################################################################

        position+=8

        gamma = hexArray[position:position+8]
        gammaDecimal = int(gamma,16)

        var = "\nImage gamma : " + str(gammaDecimal)
        print(var)

    else:
        print("\n6. gAMA not found")
