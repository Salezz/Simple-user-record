from Menu.Interface import *
from Menu.arquive import *
from time import sleep

file = "record.txt"

if not fileExist(file):
    createFile(file)

while True:
    answer = menu(["See user´s", "Register user", "Exit system"])
    if answer == 1:
        # Option to list file content!
        ReadFile(file)
    elif answer == 2:
        head("NEW RECORD")
        name = str(input("Name: "))
        age = readInt("Age: ")
        register(file, name, age)

    elif answer == 3:
        head("Closing system!")
        break
    else:
        head("\033[31mERROR, inform a valid answer.\033[m")
    sleep(1.5)