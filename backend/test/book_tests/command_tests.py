# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from decimal import Decimal
from book_app.commands import SaveBookCommand
from book_app.model import Book
from gaebusiness.business import CommandExecutionException


class SaveBookTests(GAETestCase):
    def test_success(self):
        cmd = SaveBookCommand(price='25.88', title='App Engine')
        books = Book.query().fetch()
        self.assertEqual(0, len(books))
        cmd()
        books = Book.query().fetch()
        self.assertEqual(1, len(books))
        b = books[0]
        self.assertEqual(Decimal('25.88'), b.price)
        self.assertEqual('App Engine', b.title)

    def test_missing_title(self):
        cmd = SaveBookCommand(price='25.88')
        self.assertRaises(CommandExecutionException,cmd)





