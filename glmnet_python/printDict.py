# -*- coding: utf-8 -*-
"""
Prints some info about a dictionary object. Used for troubleshooting.

"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from builtins import range


def printDict(s):
    for keys in s.keys():
        try:
            print('%10s  %20s  %20s' % (keys, type(s[keys]), s[keys].shape))
        except:
            print('%10s  %20s' % (keys, type(s[keys])), '  ', s[keys])
