#!/usr/bin/python3

# Imported libraries
from PIL import Image
from PIL.ExifTags import TAGS

# Function that finds exif's but it is from PIL library
def findEXIF (imageName):

    print("\n######################")
    print("# Finding ExifTags #")
    print("######################")

    image = Image.open('created_files/{}'.format(imageName))

    print("\nExif's that has been found :")

    for tag, value in image.info.items():

        key = TAGS.get(tag, tag)
        print(key + " " + str(value))
