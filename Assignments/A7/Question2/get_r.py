# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:00:23 2018

@author: delor
"""

import numpy as np

def get_r(K, L, alpha, Z, delta):
    "Defining the function for interest rate r_t in a given period of time"
    
    r = alpha * Z * (L/K)**(1-alpha) - delta
    
    assert alpha >= 0 and alpha <= 1, "Alpha should be within the range (0,1)"
    assert delta >= 0 and delta <= 1, "Delta should be within the range (0,1)"
    assert Z > 0, "Z should be greater than 0"

    if type(K) == float and type(L) == float:
        assert type(r) == float, "Function failed to return scalar interest rate for scalars K and L"
    if not np.isscalar(K) and not np.isscalar(L):
        assert not np.isscalar(r), "Function failed to return vector interest rate for vectors K and L"
    return r