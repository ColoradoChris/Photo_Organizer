#! python3

#This program will walk through my photo folders and files and organize them by month and year.

import os, shutil, PIL, re
from PIL import Image

photoRegEx = re.compile(r".JPG$")

#Move to photo directory if not already there.
currentDirectory = os.getcwd()

if currentDirectory != r"E:\Pictures\Pictures\Pictures":
    os.chdir(r"E:\Pictures\Pictures\Pictures")
    currentDirectory = os.getcwd()

#Walk through the photos in each of the folders in the directory.
for folderName, subfolders, files in os.walk(currentDirectory):
    print(folderName)

    for filename in files:
        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(folderName + "\\" + filename))
            creationDate = photo._getexif()
            creationDate = creationDate.get(36867, None) #Permission Error needs to be handled.

            if creationDate is not None: #Sort by Year if creationDate exists

                if creationDate[0:4] == "2016":
                    print("%s is from 2016 - copying to the 2016 folder." % (filename))

                    if not os.path.exists(r"E:\Pictures\2016_Photos"):
                        os.mkdir(r"E:\Pictures\2016_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"E:\Pictures\2016_Photos")

                elif creationDate[0:4] == "2015":
                    print("%s is from 2015 - copying to the 2015 folder." % (filename))

                    if not os.path.exists(r"E:\Pictures\2015_Photos"):
                        os.mkdir(r"E:\Pictures\2015_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"E:\Pictures\2015_Photos")

                elif creationDate[0:4] == "2017":
                    print("%s is from 2017 - copying to the 2017 folder." % (filename))

                    if not os.path.exists(r"E:\Pictures\2017_Photos"):
                        os.mkdir(r"E:\Pictures\2017_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"E:\Pictures\2017_Photos")

            else:
                print("%s does not have a creation date - moving to the No Data File." % (filename))

                if not os.path.exists(r"E:\Pictures\NoData_Photos"):
                    os.mkdir(r"E:\Pictures\NoData_Photos")

                shutil.copy(os.path.abspath(folderName + "\\" + filename), r"E:\Pictures\NoData_Photos")

                continue

#TODO Create Month Folders

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i in range(len(months)):
    if not os.path.exists("E:\\Pictures\\2017_Photos\\" + months[i]):
        os.mkdir("E:\\Pictures\\2017_Photos\\" + months[i])

    if not os.path.exists("E:\\Pictures\\2016_Photos\\" + months[i]):
        os.mkdir("E:\\Pictures\\2016_Photos\\" + months[i])

    if not os.path.exists("E:\\Pictures\\2015_Photos\\" + months[i]):
        os.mkdir("E:\\Pictures\\2015_Photos\\" + months[i])

#TODO Move the photos in each of the Year folders to their appropriate Month Folders

for folderName, subfolders, files in os.walk("E:\\Pictures\\2017_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(filename))
            creationDate = photo._getexif()[36867]
            creationDate = creationDate[5:7]
            shutil.move(os.path.abspath(filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))

for folderName, subfolders, files in os.walk("E:\\Pictures\\2016_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(filename))
            creationDate = photo._getexif()[36867]
            creationDate = creationDate[5:7]
            shutil.move(os.path.abspath(filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))

for folderName, subfolders, files in os.walk("E:\\Pictures\\2015_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(filename))
            creationDate = photo._getexif()[36867]
            creationDate = creationDate[5:7]
            shutil.move(os.path.abspath(filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))
