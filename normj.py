#!python3
#!/usr/local/bin
# encoding: utf-8

import os
import sys
from getopt import getopt
import pandas as pd

os.system("date")

#os.system("poetry -i misc2.txt -o result.json")


ops,args = getopt(sys.argv[1:],"n: ")
ops = dict(ops)

command = "poetry -i "
resultc = " -o result.json"

if '-n' in ops:
    poema = ops['-n']
    tmp = command + ops['-n'] + resultc
    print(tmp)
    os.system(tmp)
    #print(ops['-n'])
    #print(poema)
    
    df = pd.read_json('result.json')
    #print(df.content)
    print(df.content[0][0][0])
else:
    print("fodeu!")