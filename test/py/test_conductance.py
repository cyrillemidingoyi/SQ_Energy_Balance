'Test generation'

from conductance import *
from math import *
import numpy as np



def test_test1():
    params= conductance(
    zm = 0.13,
    zh = 0.013,
    d = 0.67,
    wind = 124000,
    plantHeight = 0,
     )
    conductance_estimated = round(params, 3)
    conductance_computed = 598.685
    assert (conductance_estimated == conductance_computed)