#!python3
#!/usr/local/bin
# encoding: utf-8

import os
from re import *
import sys
from getopt import getopt
import pandas as pd

os.system("date")

#os.system("poetry -i misc2.txt -o result.json")

# pegar no ficheiro do poema
# retirar metadados e crirar .txt temporario só com poema
# usar coisa2 neste ficheiro, retornar tmp_rimas
# adicionar a tmp_rimas os metadados

ops,args = getopt(sys.argv[1:],"n: ")
ops = dict(ops)

# retirar todos os : do texto antes de converter para JSON
nome_poema = ops['-n']
metadados = ''
poema = ''
with open(nome_poema) as f :
    print('vou ler este ficheiro: ',nome_poema)
    txt = f.read()
    res = split(r'---', txt)
    print('res len = ', len(res))
    metadados = res[1]
    poema = res[2]
    #print(metadados, poema)

# ficheiros temporários
f1 = open("poema_final.txt", 'w')
f2 = open("poema_tmp.txt", 'w')

f1.write("---")
f1.write(metadados)
f1.write("---")
f1.close()

poema = sub(r':', '', poema)
f2.write(poema)
f2.close()

## usar coisa2
os.system("./coisa2 poema_tmp.txt >> poema_final.txt")


command = "poetry -i "
nome = search(r'^\w+', nome_poema).group(0)

tmp = command + "poema_final.txt " + "-o "+nome+".json"
print(tmp)
os.system(tmp)

os.system("rm poema_final.txt")
os.system("rm poema_tmp.txt")

#print(ops['-n'])
#print(poema)





#df = pd.read_json('result.json')
#print(df.content)
#print(df.content[0][0][0])
#print(df.data[0]) metadados 
