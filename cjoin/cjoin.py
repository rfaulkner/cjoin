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
__date__        = "09/02/2013"
__license__     = "GPL (version 2 or later)"

import ext.cjoin_ext

def cjoin(ds_1, ds_2, idx_1, idx_2, conditional=None):
    """ Core cjoin functionality

            conditional==None: default to equality join
    """
    return ds_1 + ds_2