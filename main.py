#!/usr/bin/env python
import os
import re

task = {}
s = []
# x = " "		## ✔

def check():
    pass 

def read():
    f = open("dictionary.txt", "r")
    content = f.read()
    f.close()
    for i in content.split("\n"):
        task[i] = i
    print(task)

def print_header():
    os.system("clear")
    print("#"*90)
    print("#"*40 + "TO-DO-List" + "#"*40)
    print("#"*90)
    print("1.   Add a new Task")
    print("2.   Remove a Task")
    print("3.   Exit the program and save the entries\n") 

    for key, value in task.items():
        print("-->  " + key)

def exit():
    os.system("exit")

def save():
    tosave = re.findall("'(.*?)'", str(task))
    for i in tosave:
    	if i not in s:
    	    s.append(i)	    
    f = open("dictionary.txt", "w")
    for i in s[:-1]:
    	f.write(i + "\n")
    f.write(s[-1])
    f.close()

def options():
    try:
        choose = int(input("\nChoose your option: "))
        if choose == 1:
            print_header()
            task_name = input("\nWhat is the task, you want to add? \n")
            task[task_name] = task_name
            print_header()
            options()
            check()
        elif choose == 2:
            print_header()
            task_name = input("\nWhat is the task, you want to remove? \n")
            try:
                del task[task_name]
                tosave = re.findall("'(.*?)'", str(task))
                for i in tosave:
    	            if i not in s:
    	                s.append(i)	    
                f = open("dictionary.txt", "w")
                for i in s[:-1]:
    	            f.write(i + "\n")
                f.write(s[-1])
                print_header()
                options()
            except KeyError:
                print_header()
                print("\nNot an option! Try again!")
                input("Press enter to continue...")
                print_header()
                options()
        elif choose == 3:
            print_header()
            save()
            exit()
        else:
            print_header()
            print("\nNot an option! Try again!")
            input("Press enter to continue...")
            print_header()
            options()
    except ValueError:
        print_header()
        print("\nNot one of the options! Try again!")
        input("Press enter to continue...")
        print_header()
        options()


if __name__ == "__main__":
    read()
    print_header()
    options()
