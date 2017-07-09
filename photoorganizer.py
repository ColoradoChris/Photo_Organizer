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
            print(filename)
        #photo_files = Image.open(files)
        #photo._getexif()[36867]

#TODO Sort photos by creation date (Month/Year)

#TODO Move the photos to the appropriate Month/Year Folders -- Create those folders if necessary.
