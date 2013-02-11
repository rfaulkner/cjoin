"""
    Defines the conditional join functionality.  This module aims to provide
    the simple function of allowing a call to be made on a pair of datasets
    to be joined over a distribution threshold.

    Example ::

        >>> from cjoin import Cjoin
        >>> Cjoin().cjoin([],[],1,1)
"""

__author__      = "Ryan Faulkner"
__email__       = "ryan.faulkner@mail.mcgill.ca"
__date__        = "09.02.2013"
__license__     = "GPL (version 2 or later)"

import ext.cjoin_ext

class Conditional(object):

    def __init__(self, **kwargs):
        super(self, Conditional).__init__(**kwargs)

    def __eq__(self, val_1, val_2):
        """ Determines whether the input values satisfy equality condition """
        return val_1 == val_2