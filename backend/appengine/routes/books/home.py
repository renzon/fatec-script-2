# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from book_app import facade
from routes.books import admin, rest


@login_not_required
@no_csrf
def index():
    context = {
        'admin_path': router.to_path(admin),
        'salvar_path': router.to_path(rest.save),
        'editar_path': router.to_path(rest.update),
        'apagar_path': router.to_path(rest.delete),
        'listar_path': router.to_path(rest.index)}
    return TemplateResponse(context, 'books/home.html')

