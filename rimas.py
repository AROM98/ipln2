#!python3
#!/usr/local/bin
# encoding: utf-8

import os
import subprocess, sys
from getopt import getopt
import pandas as pd

os.system("date")

ops,args = getopt(sys.argv[1:],"pn: ")
ops = dict(ops)

def rima_palavra():
    #pipe = subprocess.Popen(["perl", "coisa2"], stdout=sys.stdin)
    #os.system("./coisa2")
    print("digite uma palavra:")
    output = subprocess.check_output("./coisa2", shell=True)
    print('agora vou imprimir output:')
    print(output)

def rima_poema():
    return
####  limpar output   -  importante

# comparar com palavras da "wordlist-rimas.txt"

# fazer reguex para encontrar silaba tónica e silaba final

# usar vogal da tónica e ultima silaba.

# palavras que riamam têm estes 2 campos iguais

# resolver casos com apenas 1 silaba




if '-n' in ops:
    print('nome do ficheiro do poema = ', ops['-n'])
elif '-p' in ops:
    rima_palavra()
else:
    print('no no no, plz indicar -p para palavra ou -n para poema!')