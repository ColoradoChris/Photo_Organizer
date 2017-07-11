#! python3

#This program will walk through my photo folders and files and organize them by month and year.

import os, shutil, PIL, re
from PIL import Image

photoRegEx = re.compile(r".JPG$")

#TODO Move to photo directory if not already there.
currentDirectory = os.getcwd()

if currentDirectory != r"E:\Pictures\Pictures\Pictures":
    os.chdir(r"E:\Pictures\Pictures\Pictures")
    currentDirectory = os.getcwd()

#TODO Walk through the photos in each of the folders in the directory.
for folderName, subfolders, files in os.walk(currentDirectory):
    print(folderName)
    for filename in files:
        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(folderName + "\\" + filename))
            creationDate = photo._getexif()
            creationDate = creationDate.get(36867, None) #Permission Error needs to be handled.
            if creationDate is not None:
                if creationDate[0:4] == "2016":
                    print("%s is from 2016" % (filename))
                elif creationDate[0:4] == "2015":
                    print("%s is from 2015" % (filename))
                elif creationDate[0:4] == "2017":
                    print("%s is from 2017" % (filename))
            else:
                print("%s does not have a creation date." % (filename))
                continue

#TODO Sort photos by creation date (Month/Year)

#TODO Move the photos to the appropriate Month/Year Folders -- Create those folders if necessary.
