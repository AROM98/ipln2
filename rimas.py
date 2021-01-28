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
    tmp_silaba = search(r'(?<=\|)\w+(:*\w*)?\ ?$', pal)
    if tmp_silaba != None:
        silaba = tmp_silaba.group(0)
        ## casos do âo, etc
        tmp_tonica = search(r'[a-záãàâõôóòêéíú]:[a-z]*', silaba)
        if tmp_tonica != None:
            silaba = tmp_tonica.group(0)
    else:
        # como não encontrou, é possivel que a palavra só tenha uma silada, dai:
        tmp_silaba = search(r'[a-záãàâõôóòêéíú]:[a-z]*', pal)
        if tmp_silaba != None:
            silaba = tmp_silaba.group(0)
        else:
            silaba = ''
    silaba = sub(r':', '', silaba)
    return silaba

# encontra a ultima palavra
def acha_ult_pal(verso):
    # as vezes os versos tem ponto final e dá erro na operação seguite.
    verso = sub('\.|\,', '', verso) #logo é tirado os . 
    tmp = search(r'[a-zA-Z:|áãàâõôóòêéíúç]+\ *$', verso)
    if tmp != None:
        ult = tmp.group(0)
        ult = sub(r'\ ', '', ult) ## garante que ultima palavra não tem espaços
    else:
        ult = ''
    return ult

# verifica se rima
def ver_rima(pal1, pal2):
    print('vou verificar', pal1, "---->", pal2)
    vogal_pal1 = acha_vogal(pal1)
    silaba_pal1 = acha_silab(pal1)
    vogal_pal2 = acha_vogal(pal2)
    silaba_pal2 = acha_silab(pal2)
    print([vogal_pal1, silaba_pal1],[vogal_pal2, silaba_pal2])
    if vogal_pal1 == vogal_pal2 and silaba_pal1 == silaba_pal2:
        print('RIMA')
        return True
    else:
        print('NAO RIMA')
        return False


# tudo sobre a opçao de 'palavra'
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
    print("digite uma palavra:")
    output = subprocess.check_output("./coisa2", shell=True)
    coisa = str(output, 'utf-8')
    print('agora vou imprimir output:')
    print(coisa)
    ler_pal_rima(coisa)


# exp para retirar : . | -- >        :|\.|\|
def rima_poema(poema):
    tipo_rima = []
    ults = []
    linhas = 0
    df = pd.read_json(poema)
    print('este poema tem ', len(df.content[0]), 'estrofes')
    print('a estrofe[0], tem ',len(df.content[0][0]), 'versos')
    print(df.content[0][0][0])
    #print(df.data[0]) # este não percebo muito bem como percorrer

    # para cada estrofe do poema
    for estrofe in df.content[0]:
        
        # para cada verso de uma estrofe
        for verso in estrofe:
            #print("verso = ", verso)
            ultima_pal = acha_ult_pal(verso)
            #print("ultima palavra = ", ultima_pal)

            # linhas ocupadas com 'ultimas palavras'
            tam_ults = len(ults) #+ linhas
            print('tam_ults =', tam_ults)

            # se já houver alguma palavra, então compara
            if abs(linhas - tam_ults) != 0:
                rima = False
                for j in range(linhas, tam_ults):
                    val = ver_rima(ultima_pal, ults[j])
                    # se é rima
                    if val:
                        tp_rima = tipo_rima[j]
                        tipo_rima.append(tp_rima)
                        ults.append(ultima_pal)
                        print(ultima_pal, 'rima com', ults[j])
                        rima = True

                if rima == False:
                    tp_rima = ord('A')
                    for j in range(linhas, tam_ults):
                        if ord(tipo_rima[j]) > tp_rima:
                            tp_rima = ord(tipo_rima[j])
                    tp_rima = chr(tp_rima + 1) ## passa para a letre seguinte
                    tipo_rima.append(tp_rima)
                    ults.append(ultima_pal)
                    
            # se não houver, então insere-se a primeira
            else:
                ults.append(ultima_pal)
                tipo_rima.append('A')

        linhas += len(estrofe)
        print('linhas =', linhas)
    
    # no final
    print(tipo_rima)
            












if '-n' in ops:
    print('nome do ficheiro do poema = ', ops['-n'])
    rima_poema(ops['-n'])
elif '-p' in ops:
    rima_palavra()
else:
    print('no no no, plz indicar -p para palavra ou -n para poema!')

