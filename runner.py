import os
from os import walk
import pathlib

path = ''

slashes = ''

foreword = ''

if (os.name == 'nt'):
    path = str(pathlib.Path(__file__).parent.resolve()) + '\\skripts\\windows'
    slashes = '\\'
elif (os.name == 'posix'):
    path = os.getcwd() + '/skripts/unix'
    slashes = '/'
    foreword = 'python3 '
else:
    print('OS not supported')
    exit

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

while (True):
    key = 0
    dictionary = {}
    for skript in f:
        b = {str(key): skript}
        dictionary.update(b)
        print(skript + ' -> ' + str(key) + '\n')
        key = key + 1

    run_skript = dictionary[input("choose skript to run: ")]

    os.system(foreword + path + slashes + run_skript)

    print('\n--------------------------------\n Thank chuuuu~ ^~^ \n--------------------------------\n')
