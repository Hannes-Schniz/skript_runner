import os
from os import walk
import pathlib

path = str(pathlib.Path(__file__).parent.resolve()) + '\\skripts'

f = []
while(True):
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break

    key = 0
    dictionary = {}
    for skript in f:
        b = {skript : key}
        dictionary.update(b)
        print('for: ' + skript + ' type ' + str(key) + '\n')
        key = key + 1

    run_skript = input("choose skript to run: ")

    os.system(path + '\\' + skript)

    print('Thank chuuuu~ ^~^')
    