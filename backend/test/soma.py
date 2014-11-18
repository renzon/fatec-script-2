# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest import TestCase


def soma(param, param1):
    return param + param1


class SomaTests(TestCase):
    def test_soma_positivos(self):
        resultado= soma(1,2)
        self.assertEqual(3,resultado)
        self.assertEqual(9,soma(2,7))