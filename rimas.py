#!python3
#!/usr/local/bin
# encoding: utf-8

import os
import subprocess, sys
from getopt import getopt
import pandas as pd
from re import *

os.system("date")

ops,args = getopt(sys.argv[1:],"pn: ")
ops = dict(ops)

def ler_pal_rima(coisa):
    for ficheiro in args:
        with open(ficheiro) as f :
            print('vou ler este ficheiro: ',ficheiro)
            txt = f.read()
            res = split(r'\n', txt)
            print('res len = ', len(res))
            fazer_coisas(res, coisa)

def fazer_coisas(t, pal):
    vogal_pal = search(r'[aeiouáãàâõôóòêéíú](?=\:)', pal).group(0)
    print('vogal_pal = ', vogal_pal)
    silaba_pal = search(r'(?<=\|)\w+(:*\w*)?$', pal).group(0)
    silaba_pal = sub(r':', '', silaba_pal)
    print('silaba_pal = ', silaba_pal)
    for palavra in t:
        #print("palavra = ", palavra)
        tmp = search(r'[aeiouáãàâõôóòêéíú](?=\:)', palavra)
        if tmp != None:
            vogal = tmp.group(0)
        else:
            vogal = ''
            #print(palavra,'----->',vogal)
        tmp = search(r'(?<=\|)\w+(:*\w*)?$', palavra)
        if tmp != None:
            silaba = tmp.group(0)
            silaba = sub(r':', '', silaba)
        else:
            silaba = ''
            #print(palavra,'----->',silaba)
        ## verificar se rima ou não
        if(vogal_pal == vogal and silaba_pal == silaba):
            ## supostamente rima
            pal_tmp = sub(r'[|:\n]*', '', pal)
            palavra_tmp = sub(r'[|:]*', '', palavra)
            print(pal_tmp, "rima com ", palavra_tmp)
        

def rima_palavra():
    #pipe = subprocess.Popen(["perl", "coisa2"], stdout=sys.stdin)
    #os.system("./coisa2")
    
    print("digite uma palavra:")
    output = subprocess.check_output("./coisa2", shell=True)
    coisa = str(output, 'utf-8')
    print('agora vou imprimir output:')
    print(coisa)
    ler_pal_rima(coisa)

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

