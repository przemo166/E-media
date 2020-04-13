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
        print("\nPLTE found")
        position += 8

        print("\n######################")
        print("# Reading PLTE chunk #")
        print("######################")

    else:
        print("\nPLTE not found")
