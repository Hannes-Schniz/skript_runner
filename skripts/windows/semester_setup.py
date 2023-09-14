import os
from time import sleep
courses = []
folders = ["Lecture", "Tutorium", "Papers"]
userInput = ""
print("when done type done")
while(userInput != "done"):
    userInput = input("Input lecture: ")
    courses.append(userInput)

path = input("path: ")
for course in courses:
    currPath = path + "/" + course
    os.makedirs(currPath)
    for folder in folders:
        os.makedirs(currPath + "/" + folder)
    sleep(0.5)