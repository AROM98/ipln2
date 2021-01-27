#!python3
#!/usr/local/bin
# encoding: utf-8

import os
import subprocess, sys
from getopt import getopt
import pandas as pd
from re import *
import pandas as pd

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

def acha_vogal(pal):
    tmp_vogal = search(r'[aeiouáãàâõôóòêéíú](?=\:)', pal)
    if tmp_vogal != None:
        return tmp_vogal.group(0)
    else:
        return ''

def acha_silab(pal):
    tmp_silaba = search(r'(?<=\|)\w+(:*\w*)?$', pal)
    if tmp_silaba != None:
        silaba = tmp_silaba.group(0)
        ## casos do âo, etc
        tmp_tonica = search(r'[a-záãàâõôóòêéíú]:[a-z]*', silaba)
        if tmp_tonica != None:
            silaba = tmp_tonica.group(0)
    else:
        silaba = ''
    silaba = sub(r':', '', silaba)
    return silaba


def fazer_coisas(t, pal):
    vogal_pal = acha_vogal(pal)
    print('vogal_pal = ', vogal_pal)

    silaba_pal = acha_silab(pal)
    print('silaba_pal = ', silaba_pal)
    for palavra in t:
        #print("palavra = ", palavra)
        vogal = acha_vogal(palavra)
        
        silaba = acha_silab(palavra)
            
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



def rima_poema(poema):
    df = pd.read_json(poema)
    print(df.content[0][0][0])



if '-n' in ops:
    print('nome do ficheiro do poema = ', ops['-n'])
    rima_poema(ops['-n'])
elif '-p' in ops:
    rima_palavra()
else:
    print('no no no, plz indicar -p para palavra ou -n para poema!')

