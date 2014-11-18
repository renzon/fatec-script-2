# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from base import GAETestCase
from routes.books import rest


class TestSave(GAETestCase):
    def test_success(self):
        expected_dct={'title':'A','price':'34'}
        json_response = rest.save(None,**expected_dct)

        self.assertEqual(expected_dct['title'],json_response.context['title'])
        self.assertEqual(expected_dct['price'],json_response.context['price'])
        self.assertIsNotNone(json_response.context.get('creation'))
        self.assertIsNotNone(json_response.context.get('id'))
        json.dumps(json_response.context)