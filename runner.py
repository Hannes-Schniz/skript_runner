import os
from os import walk
import pathlib

path = str(pathlib.Path(__file__).parent.resolve()) + '\\skripts'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

while(True):
    key = 0
    dictionary = {}
    for skript in f:
        b = {str(key) : skript}
        dictionary.update(b)
        print(skript + ' -> ' + str(key) + '\n')
        key = key + 1
        
    run_skript = dictionary[input("choose skript to run: ")]

    os.system(path + '\\' + run_skript)

    print('\n--------------------------------\n Thank chuuuu~ ^~^ \n--------------------------------\n')
    