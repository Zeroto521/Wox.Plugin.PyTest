# -*- coding: utf-8 -*-

import time


def testit(param, file='project.log', mode='a', encoding='utf-8'):
    with open(file=file, mode=mode, encoding=encoding) as f:
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message = "{}, {}\n".format(date, param)
        f.write(message)
