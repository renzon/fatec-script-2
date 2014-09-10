# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from escravo_app.comandos import ListarDeEscravosPorDataDeCriacao, EditarEscravo, SalvarEscravo, \
    SalvarEscravoLinkandoComDono
from escravo_app.forms import EscravoShort, EscravoForm
from escravo_app.modelos import DonoArco
from gaegraph.business_base import DeleteNode, NodeSearch, CreateSingleArc


def listar_escravos_de_dono(dono):
    """
    Método que retornar comando que lista escravos de um dono ordenados
    por data criação
    :param dono: Dono (Usuário) ou um comando que retorne um usuário como resultado
    :return: Comando que retorna lista de escravos como resultado

    """
    return ListarDeEscravosPorDataDeCriacao(dono)


def escravo_form_short(**propriedades):
    return EscravoShort(**propriedades)


def deletar_escravos_cmd(*escravo_id):
    return DeleteNode(*escravo_id)


def escravo_form(**propriedades):
    return EscravoForm(**propriedades)


def get_escravo_por_id_cmd(escravo_id):
    return NodeSearch(escravo_id)


def editar_escravo_cmd(escravo_id, **params):
    return EditarEscravo(escravo_id, **params)


def salvar_escravo(dono, **param):
    return SalvarEscravoLinkandoComDono(dono, **param)

def a():
    pass