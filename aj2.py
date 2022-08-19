import os
import datetime
import colorama 
from art import * # optional

# initializing colorama
#c.init()

# datetime variable
now = datetime.datetime.today().strftime("%H:%M:%S %d-%m-%Y")


#print(c.Fore.LIGHTCYAN_EX)
#print(c.Back.WHITE)
#tprint("AWESOME JOURNAL", font="random") # displaying wonderful title
#print(c.Style.RESET_ALL)


# load the journal and print it
with open("journal.txt", "r") as file:
    the_whole_file = file.read()
print(the_whole_file)


# display current journal
new_entry = input("ENTER DIARY ENTRY HERE >>> ")

current_pwd = os.getcwd().replace("\\","/") # defining path variable for later if statement

if current_pwd.upper() in new_entry.upper(): # if weird path bug, dont save
    print("")
    pass
elif new_entry != "": # if entry is not empty, save entry
    with open("journal.txt", "a") as file:
        file.write(now + " - " + new_entry + "\n")
else:
    print("Empty string. NOT ADDING.") # if entry empty, dont save