# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from tekton.gae.middleware.json_middleware import JsonResponse, JsonUnsecureResponse
from book_app import facade


@login_required
def index():
    cmd = facade.list_books_cmd()
    book_list = cmd()
    short_form = facade.book_short_form()
    book_short = [short_form.fill_with_model(m) for m in book_list]
    return JsonResponse(book_short)


@login_required
def save(_resp,**book_properties):
    cmd = facade.save_book_cmd(**book_properties)
    return _save_or_update_json_response(_resp,cmd)


def update(_resp,id, **book_properties):
    cmd = facade.update_book_cmd(id, **book_properties)
    return _save_or_update_json_response(_resp,cmd)

@login_required
def delete(id):
    facade.delete_book_cmd(id)()


def _save_or_update_json_response(_resp, cmd):
    try:
        book = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        _resp.get('nome')
        return JsonResponse(cmd.errors)
    short_form = facade.book_short_form()
    model = short_form.fill_with_model(book)
    return JsonResponse(model)

