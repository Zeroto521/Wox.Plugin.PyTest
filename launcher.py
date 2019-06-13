# -*- coding: utf-8 -*-

"""The script is a launcher for Wox plugin.
"""

from pytest import testit

from wox import Wox


class Main(Wox):

    def query(self, key):
        key = key.strip()

        testit(key)

        return [
            {
                'Title': "It's testing now.",
                'IcoPath': 'images/favicon.png',
            }
        ]


if __name__ == "__main__":
    Main()
