import unittest
from pwnbox import utils

class TestTos(unittest.TestCase):
    def test_dtol(self):
        self.assertEqual(utils.dtol(0x01234567), "\x67\x45\x23\x01")

    def test_dtob(self):
        self.assertEqual(utils.dtob(0x01234567), "\x01\x23\x45\x67")

    def test_qtol(self):
        self.assertEqual(utils.qtol(0x0123456789abcdef), "\xef\xcd\xab\x89\x67\x45\x23\x01")

    def test_qtob(self):
        self.assertEqual(utils.qtob(0x0123456789abcdef), "\x01\x23\x45\x67\x89\xab\xcd\xef")

    def test_ltoi(self):
        self.assertEqual(utils.ltoi("\x67\x45\x23\x01"), 0x01234567)

    def test_btoi(self):
        self.assertEqual(utils.btoi("\x01\x23\x45\x67"), 0x01234567)
