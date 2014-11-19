# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from config.template import render
from routes.books import home


class TestIndex(GAETestCase):
    def test_success(self):
        template_response = home.index()
        render(template_response.template_path,template_response.context)