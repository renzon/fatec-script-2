# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from escravo_app.forms import EscravoForm
from escravo_app.modelos import DonoArco
from gaebusiness.gaeutil import SaveCommand, UpdateCommand
from gaegraph.business_base import DestinationsSearch, CreateSingleArc
from gaegraph.model import to_node_key


class ListarDeEscravosPorDataDeCriacao(DestinationsSearch):
    def __init__(self, dono):
        super(ListarDeEscravosPorDataDeCriacao, self).__init__(DonoArco, dono)

    def do_business(self):
        super(ListarDeEscravosPorDataDeCriacao, self).do_business()
        self.result = [e for e in self.result if e != None]

class SalvarEscravo(SaveCommand):
    _model_form_class = EscravoForm

class SalvarEscravoLinkandoComDono(CreateSingleArc):

    def __init__(self,dono,**params):
        super(SalvarEscravoLinkandoComDono, self).__init__(DonoArco, dono,  SalvarEscravo(**params))


class EditarEscravo(UpdateCommand):
    _model_form_class = EscravoForm

    def __init__(self, model_key, **form_parameters):
        model_key=to_node_key(model_key)
        super(EditarEscravo, self).__init__(model_key, **form_parameters)




