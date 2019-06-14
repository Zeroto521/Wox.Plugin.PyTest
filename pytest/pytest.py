# -*- coding: utf-8 -*-

"""
PyTest
=====
Test Python language in Wox plugin.

Example
----------------------------
    >>> from pytest import testit
    >>> testit('Somewords are here.')  # It will log information to local file.

Copyright Zeroto521
----------------------------
"""

import time


def testit(param='', file='project.log', mode='a', encoding='utf-8'):
    with open(file=file, mode=mode, encoding=encoding) as f:
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = "{},{}\n".format(date, param)
        f.write(message)
