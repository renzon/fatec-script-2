# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals



def f(a,b,c='c',d='d'):
    print a,b,c,d

f('a','b')
f('a','b','e')
f('a','b',d='e')

def soma(*argumentos):
    soma=0
    # for a in argumentos:
    #     soma+=a
    print list(argumentos)
    return soma

print soma()
print soma(1)
print soma(1,2)
print soma(1,2,3)

lista=list(range(0,5))
print soma(lista)
print soma(*lista)

def palavras_chave(** kwargs):
    print kwargs

palavras_chave(a='a')
palavras_chave(a='a',b='be')
palavras_chave(a='a',b='be',c='ce')

dct={'a':'a','b':'be','c':'ce'}

palavras_chave(**dct)

def f(*args,**kwargs):
    print args
    print kwargs


f(1234,4567,675687,a='a',b='be')