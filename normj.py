#!python3
#!/usr/local/bin
import os
import sys
from getopt import getopt

os.system("date")

#os.system("poetry -i misc2.txt -o result.json")


ops,args = getopt(sys.argv[1:],"n: ")
ops = dict(ops)

command = "poetry -i "
resultc = " -o result.json"

if '-n' in ops:
    tmp = command + ops['-n'] + resultc
    print(tmp)
    os.system(tmp)
    print(ops['-n'])
    #print(args)
else:
    print("fodeu!")