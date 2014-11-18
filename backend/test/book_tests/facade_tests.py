# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from book_app.facade import delete_book_cmd
from book_app.model import Book
from mommygae import mommy


class DeleteBookTests(GAETestCase):
    def test_delete_non_existent_book(self):
        cmd = delete_book_cmd('1')
        cmd()

    def test_success(self):
        book = mommy.save_one(Book,title='sdfsdf')
        key = book.key
        cmd = delete_book_cmd(key.id())
        cmd()
        self.assertIsNone(key.get())


