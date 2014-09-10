# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from escravo_app.modelos import Escravo
from gaeforms.ndb.form import ModelForm


class EscravoShort(ModelForm):
    _model_class = Escravo
    _include = [Escravo.birth, Escravo.name, Escravo.price]

class EscravoForm(ModelForm):
    _model_class = Escravo
    _include = [Escravo.birth, Escravo.name, Escravo.price, Escravo.age, Escravo.estatura]