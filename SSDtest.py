#! python3

#This program will walk through my photo folders and files and organize them by month and year.

import os, shutil, PIL, re, time
from PIL import Image

start_time = time.time()

photoRegEx = re.compile(r".JPG$")

#Move to photo directory if not already there.
currentDirectory = os.getcwd()

if currentDirectory != r"C:\Users\ckansas\Pictures":
    os.chdir(r"C:\Users\ckansas\Pictures")
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
                    print("Copying %s to the 2016 folder." % (filename))

                    if not os.path.exists(r"C:\Users\ckansas\Pictures\2016_Photos"):
                        os.mkdir(r"C:\Users\ckansas\Pictures\2016_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"C:\Users\ckansas\Pictures\2016_Photos")

                elif creationDate[0:4] == "2015":
                    print("Copying %s to the 2015 folder." % (filename))

                    if not os.path.exists(r"C:\Users\ckansas\Pictures\2015_Photos"):
                        os.mkdir(r"C:\Users\ckansas\Pictures\2015_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"C:\Users\ckansas\Pictures\2015_Photos")

                elif creationDate[0:4] == "2017":
                    print("Copying %s to the 2017 folder." % (filename))

                    if not os.path.exists(r"C:\Users\ckansas\Pictures\2017_Photos"):
                        os.mkdir(r"C:\Users\ckansas\Pictures\2017_Photos")

                    shutil.copy(os.path.abspath(folderName + "\\" + filename), r"C:\Users\ckansas\Pictures\2017_Photos")

            else:
                print("%s does not have a creation date - moving to the No Data File." % (filename))

                if not os.path.exists(r"C:\Users\ckansas\Pictures\NoData_Photos"):
                    os.mkdir(r"C:\Users\ckansas\Pictures\NoData_Photos")

                shutil.copy(os.path.abspath(folderName + "\\" + filename), r"C:\Users\ckansas\Pictures\NoData_Photos")

                continue

#Create Month Folders

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for i in range(len(months)):
    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + months[i])

    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + months[i])

    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + months[i])

#Move the photos in each of the Year folders to their appropriate Month Folders

for folderName, subfolders, files in os.walk("C:\\Users\\ckansas\\Pictures\\2017_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(folderName + "\\" + filename))
            creationDate = photo._getexif()[36867]
            photo.close()
            creationDate = creationDate[5:7]
            shutil.copy(os.path.abspath(folderName + "\\" + filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))

            if os.path.exists("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + filename):
                os.unlink("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + filename)
            else:
                continue

            print("Moved %s to %s of %s" % (filename, months[int(creationDate) - 1], folderName))

print("Completed moving files in 2017_Photos Folder.")

for folderName, subfolders, files in os.walk("C:\\Users\\ckansas\\Pictures\\2016_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(folderName + "\\" + filename))
            creationDate = photo._getexif()[36867]
            photo.close()
            creationDate = creationDate[5:7]
            shutil.copy(os.path.abspath(folderName + "\\" + filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))

            if os.path.exists("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + filename):
                os.unlink("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + filename)
            else:
                continue

            print("Moved %s to %s of %s" % (filename, months[int(creationDate) - 1], folderName))

print("Completed moving files in 2016_Photos Folder.")

for folderName, subfolders, files in os.walk("C:\\Users\\ckansas\\Pictures\\2015_Photos"):

    for filename in files:

        if photoRegEx.search(filename) != None:
            photo = Image.open(os.path.abspath(folderName + "\\" + filename))
            creationDate = photo._getexif()[36867]
            photo.close()
            creationDate = creationDate[5:7]
            shutil.copy(os.path.abspath(folderName + "\\" + filename), os.path.abspath(folderName + "\\" + months[int(creationDate) - 1]))

            if os.path.exists("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + filename):
                os.unlink("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + filename)
            else:
                continue

            print("Moved %s to %s of %s" % (filename, months[int(creationDate) - 1], folderName))

print("Completed moving files in 2015_Photos Folder.")
print("The program took %s seconds to finish." % (time.time() - start_time))
