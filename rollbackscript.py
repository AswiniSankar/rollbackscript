from ast import arg
import os
import sys

# get the files
file_list=os.listdir()

changesetfile = sys.argv[1]
inputtext = "rollback"
with open(changesetfile, "r") as fp:
    # access each line
    for line in fp:
      
        if inputtext in line:
            print(line)