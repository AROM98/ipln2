#!python3
#!/usr/local/bin
# encoding: utf-8

import os
import subprocess, sys
from getopt import getopt
import pandas as pd

os.system("date")

ops,args = getopt(sys.argv[1:],"n: ")
ops = dict(ops)



#pipe = subprocess.Popen(["perl", "coisa2"], stdout=sys.stdin)

#os.system("./coisa2")
output = subprocess.check_output("./coisa2", shell=True)
print('agora vou imprimir output:')
print(output)




