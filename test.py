# -*- coding: utf-8 -*-

import unittest

from pytest import testit


class Test(unittest.TestCase):
    def test_testit(self):
        testit()


if __name__ == '__main__':
    unittest.main()
