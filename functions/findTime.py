#!/usr/bin/python3

# Function that finds tIME chunk
def findTime (hexArray):
    position = hexArray.find("74494d45")

    if position!=-1:
        print("\n5. tIME found")

        ##############################################################
        # The tIME chunk gives the time of the last image            #
        # modification (not the time of initial image creation)      #
        ##############################################################

        print("\n######################")
        print("# Reading tIME chunk #")
        print("######################")

        position+=8

        year= hexArray[position:(position+4)]
        yearDecimal = int(year,16)
        position+=4

        month= hexArray[position:(position+2)]
        monthDecimal = int(month,16)
        position+=2

        day= hexArray[position:(position+2)]
        dayDecimal = int(day,16)
        position+=2

        hour= hexArray[position:(position+2)]
        hourDecimal = int(hour,16)
        position+=2

        minute= hexArray[position:(position+2)]
        minuteDecimal = int(minute,16)
        position+=2

        second= hexArray[position:(position+2)]
        secondDecimal = int(second,16)
        position+=2


        var = "\n Year : " + str(yearDecimal) + "\n Month : " + str(monthDecimal)
        var= var + "\n Day : " + str(dayDecimal)
        var= var + "\n Hour : " + str(hourDecimal)
        var= var + "\n Minute : " + str(minuteDecimal)
        var= var + "\n Second : " + str(secondDecimal)

        print(var)

    else:
        print("\n5. tIME not found")
