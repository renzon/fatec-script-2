# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from book_app import facade
from routes.books.admin import new, edit


def delete(_handler, book_id):
    facade.delete_book_cmd(book_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    context = {'new_path': router.to_path(new)}
    return TemplateResponse(context)

