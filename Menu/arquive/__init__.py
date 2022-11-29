from Menu.Interface import *

def fileExist(name):
    try:
        a = open(name, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(name):
    try:
        a = open(name, "wt+")
        a.close()
    except:
        print("Have been an error on the file creation.")
    else:
        print(f"File {name} sucessfully created")

def ReadFile(name):
    try:
        a = open(name, "rt")
    except:
        print("Error, Could not read file!")
    else:
        head("USER´S RECORD")
        for line in a:
            data = line.split(";")
            data[1] = data[1].replace('\n', '')
            print(f"{data[0]:<30}{data[1]:>3} years")
    finally:
        a.close()

def register(file, name="unknow", age=0):
    try:
        a = open(file, "at")
    except:
        print("Have been an error in the open file!")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print("Have been an error on type data")
        else:
            print(f"{name} sucessfully registered in the record")
            a.close()