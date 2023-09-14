import os
from os import walk
import datetime as dt
import shutil
from time import sleep

path = input("path: ")
modified = input("created Date:0 | modified Date:1 : ")

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

for name in f:
    if (modified == 0):
        time = dt.date.fromtimestamp(os.path.getctime(path + '\\' + name))
    else:
        time = dt.date.fromtimestamp(os.path.getmtime(path + '\\' + name))
    full_path = path + '\\' + str(time)
    if not (os.path.exists(full_path)):
        os.mkdir(full_path, 0o666)
    shutil.move(path + '\\' + name, full_path + '\\' + name)
    print('"' + name + '"->' + str(time))
    sleep(0.5)

