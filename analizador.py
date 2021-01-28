from re import *
import sys
import pprint

literals = '</>=""\n'
tokens = ("INICIO", "VERSO", "AUTOR", "PI", "PF", "B")

def t_INICIO(t):
    r'<div class="entry-content">'
    print(f"valorB = {t.value}")

def t_VERSO(t):
    r'[ ]*\w+[\w ,.-]*'
    print(f"valorVerso = {t.value}")
    return t

def t_AUTOR(t):
    r'[(]*\w+[\w ]+[)]*'
    print(f"valorAutor = {t.value}")
    return t

def t_PI(t):
    r'<p>'
    print(f"valorPI = {t.value}")

def t_PF(t):
    r'</p>'
    print(f"valorPF = {t.value}")

def t_B(t):
    r'<br/>'
    print(f"valorB = {t.value}")

def t_error(t):
    print(f"Caracter ilegal em {t.value[0]}, linha {t.lexer.lineno}")

from ply.lex import lex
lexer = lex()

#parser
def p_a(t):"dic : INICIO poema "; print(f" poema={t[1]} autor={t[3]}")

#def p_b(t):"poema : poema"; t[0] = t[[2]] +  t[3]
def p_b(t):"poema : PI versos"; t[0] = [t[2]]

def p_d(t):"autor : PI AUTOR PF "; t[0] = t[2]

#def p_e(t):"estrofe : "; t[0] = t[2]

def p_c(t):"versos : VERSO B versos"; t[0] = [t[1]] + t[3]
def p_d(t):"versos : VERSO PF"; t[0] = [t[1]]


from ply.yacc import yacc
parser = yacc()
parser.parse(open(sys.argv[1]).read())
