import os

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

os.mkdir("C:\\Users\\ckansas\\Pictures\\2017_Photos")
os.mkdir("C:\\Users\\ckansas\\Pictures\\2016_Photos")
os.mkdir("C:\\Users\\ckansas\\Pictures\\2015_Photos")

for i in range(len(months)):
    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2017_Photos\\" + months[i])

    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2016_Photos\\" + months[i])

    if not os.path.exists("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + months[i]):
        os.mkdir("C:\\Users\\ckansas\\Pictures\\2015_Photos\\" + months[i])
