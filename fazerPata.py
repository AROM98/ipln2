#!python3
#!/usr/local/bin
from os import write
import sys
from getopt import getopt
import pandas as pd
from re import *
import pprint



ops,args = getopt(sys.argv[1:],"pn: ")
ops = dict(ops)


def retira_merdas(t):
    result = []
    print('tamanho de palist = ',len(t))
    for pal in t:
        #print('verificar palavra = ', pal)
        if(search(r'([^\: \n\t]*\:){2,}', pal) != None):
            pass
        else:
            #print('vou adicionar: ', pal)
            result.append(pal)

    file = open("cc2.txt", "w")
    for pal in result:
        file.write(pal+'\n')
    file.close()
        




for ficheiro in args:
    with open(ficheiro) as f :
        print('vou ler este ficheiro: ',ficheiro)
        txt = f.read()
        res = split(r'\n', txt)
        print('res len = ', len(res))
        retira_merdas(res)
    