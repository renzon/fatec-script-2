# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaeforms import base
from gaeforms.ndb.form import ModelForm
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    query = Escravo.query().order(-Escravo.name)
    escravo_form_short = EscravoShort()
    escravos = query.fetch()
    escravos = [escravo_form_short.fill_with_model(e) for e in escravos]
    editar_form_path = router.to_path(editar_form)
    deletar_path = router.to_path(deletar)
    for e in escravos:
        e['editar_path'] = '%s/%s' % (editar_form_path, e['id'])
        e['deletar_path'] = '%s/%s' % (deletar_path, e['id'])

    context = {'lista_de_escravos': escravos}
    return TemplateResponse(context)

def deletar(escravo_id):
    chave=ndb.Key(Escravo,int(escravo_id))
    chave.delete()
    return RedirectResponse(router.to_path(index))

@no_csrf
def editar_form(escravo_id):
    escravo_id = int(escravo_id)
    escravo = Escravo.get_by_id(escravo_id)
    escravo_form=EscravoForm()
    escravo_form.fill_with_model(escravo)
    contexto = {'salvar_path': router.to_path(editar,escravo_id),
                'escravo': escravo_form}
    return TemplateResponse(contexto, 'escravos/form.html')


def editar(escravo_id, **kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'escravo': escravo_form,
                    'erros': erros}
        return TemplateResponse(contexto, 'escravos/form.html')
    else:
        escravo_id = int(escravo_id)
        escravo = Escravo.get_by_id(escravo_id)
        escravo_form.fill_model(escravo)
        escravo.put()
        return RedirectResponse(router.to_path(index))


@no_csrf
def form():
    contexto = {'salvar_path': router.to_path(salvar)}
    return TemplateResponse(contexto)
class Escravo(ndb.Model):

    name = ndb.StringProperty(required=True)
    age = ndb.IntegerProperty()
    birth = ndb.DateProperty(auto_now=True)
    price = ndb.FloatProperty()
    estatura = ndb.FloatProperty()



class EscravoShort(ModelForm):

    _model_class = Escravo
    _include = [Escravo.birth, Escravo.name, Escravo.price]



class EscravoForm(ModelForm):

    _model_class = Escravo
    _exclude = [Escravo.birth]




def salvar(_resp, **kwargs):
    escravo_form = EscravoForm(**kwargs)
    erros = escravo_form.validate()
    if erros:
        contexto = {'salvar_path': router.to_path(salvar),
                    'escravo': escravo_form,
                    'erros': erros}
        return TemplateResponse(contexto, 'escravos/form.html')
    else:
        escravo = escravo_form.fill_model()
        escravo.put()
    return RedirectResponse(router.to_path(index))





