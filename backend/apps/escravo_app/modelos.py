# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc


class Escravo(Node):
    name = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty()
    birth = ndb.DateProperty(auto_now=True)
    price = ndb.FloatProperty()
    estatura = ndb.FloatProperty()


class DonoArco(Arc):
    destination = ndb.KeyProperty(Escravo, required=True)