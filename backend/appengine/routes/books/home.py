# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from book_app import facade
from routes.books import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_books_cmd()
    books = cmd()
    public_form = facade.book_public_form()
    book_public_dcts = [public_form.fill_with_model(book) for book in books]
    context = {'books': book_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

