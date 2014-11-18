# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

class Quantidade(object):
    default=1;

    def _identificador(self, instance):
        return '_' + str(id(self)) + '-' + str(id(instance))

    def __set__(self, instance, value):
        if value<0:
            raise ValueError('Valor deve ser positivo')
        setattr(instance, self._identificador(instance),value)

    def __get__(self, instance, owner):
        return getattr(instance,self._identificador(instance),0)

class Produto(object):


    def __new__(cls, *more):
        new = super(Produto, cls).__new__(cls, *more)
        return new

    qte=Quantidade()
    peso=Quantidade()

    def __init__(self):
        self.a=1

comp=Produto()
mouse=Produto()

print(comp.qte)
print(mouse.qte)
comp.qte=3
mouse.qte=2
mouse.peso=5

print(comp.qte)
print(mouse.qte)
print(comp.a)
print(mouse.a)