import os
from os import walk
from tokenize import String

print("skript running")

path = input("please enter path: ")
new_name = input("input what to replace to: ")

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

counter = 0
for name in f:
    print("replacing file " + name)
    full_old_path = path + '//' + name
    full_new_path = path + '//' + new_name + '_' + str(counter) + '.' + name.split('.')[1]
    os.rename(full_old_path, full_new_path)
    counter = counter + 1 