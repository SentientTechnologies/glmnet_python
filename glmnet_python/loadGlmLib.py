# -*- coding: utf-8 -*-
"""
def loadGlmLib():
=======================
INPUT ARGUMENTS:

                NONE

=======================
OUTPUT ARGUMENTS: 

glmlib          Returns a glmlib object with methods that are equivalent 
                to the fortran functions in GLMnet.f
=======================
"""
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from builtins import range

import ctypes
import os

# glmnet_so = os.path.dirname(__file__) + '/GLMnet.so'
# glmnet_dll = os.path.dirname(__file__) + '/GLMnet.dll'
glmnet_so = os.path.dirname(os.path.abspath(__file__)) + '/GLMnet.so'
glmnet_dll = os.path.dirname(os.path.abspath(__file__)) + '/GLMnet.dll'


def loadGlmLib():
    if os.name == 'posix':
        glmlib = ctypes.cdll.LoadLibrary(glmnet_so)
        return glmlib
    elif os.name == 'nt':
        # this does not currently work
        raise ValueError('loadGlmlib does not currently work for windows')
        # glmlib = ctypes.windll.LoadLibrary(glmnet_dll)
    else:
        raise ValueError('loadGlmLib not yet implemented for non-posix OS')

