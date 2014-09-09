# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from config.template_middleware import TemplateResponse
from gaeforms.base import Form, IntegerField, DateTimeField
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from course_app import facade
from routes.courses import admin

class FormGenerico(Form):
    idade=IntegerField(required=True,default=7,lower=2)
    data=DateTimeField(required=True)

@login_not_required
@no_csrf
def index():
    form=FormGenerico(idade='2','02')
    error=form.validate()
    logging.error(error)

    cmd = facade.list_courses_cmd()
    courses = cmd()
    public_form = facade.course_public_form()
    course_public_dcts = [public_form.fill_with_model(course) for course in courses]
    context = {'courses': course_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

