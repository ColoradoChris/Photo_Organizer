#! python3

#This program will walk through my photo folders and files and organize them by month and year.

import os, shutil, PIL

#TODO Move to photo directory if not already there.
currentDirectory = os.getcwd()

if currentDirectory != r"E:\Pictures\Pictures\Pictures":
    os.chdir(r"E:\Pictures\Pictures\Pictures")
    currentDirectory = os.getcwd()


#TODO Walk through the photos in each of the folders in the directory.

#TODO Sort photos by creation date (Month/Year)

#TODO Move the photos to the appropriate Month/Year Folders -- Create those folders if necessary.
