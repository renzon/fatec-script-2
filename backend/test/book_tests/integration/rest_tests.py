# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from collections import namedtuple
import json
from base import GAETestCase
from mock import Mock
from routes.books import rest


class TestSave(GAETestCase):
    def test_success(self):
        expected_dct = {'title': 'A', 'price': '34'}
        json_response = rest.save(None, **expected_dct)

        self.assertEqual(expected_dct['title'], json_response.context['title'])
        self.assertEqual(expected_dct['price'], json_response.context['price'])
        self.assertIsNotNone(json_response.context.get('creation'))
        self.assertIsNotNone(json_response.context.get('id'))
        json.dumps(json_response.context)

    def test_error(self):
        expected_dct = {'title': 'A', 'price': '34a'}


        resp_mock = Mock()
        json_response = rest.save(resp_mock, **expected_dct)
        self.assertEqual(500, resp_mock.status_code)
        resp_mock.get.assert_called_once_with('nome')
        self.assertIsNotNone(json_response.context.get('price'), 'Deveria ter um erro em preço, pois não é um numero')

        json.dumps(json_response.context)