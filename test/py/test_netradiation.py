'Test generation'

from netradiation import *
from math import *
import numpy as np



def test_test1():
    params= netradiation(
    solarRadiation = 3,
    elevation = 0,
    vaporPressure = 6.1,
     )
    netRadiation_estimated = round(params[0], 3)
    netRadiation_computed = 1.566
    assert (netRadiation_estimated == netRadiation_computed)
    netOutGoingLongWaveRadiation_estimated = round(params[1], 3)
    netOutGoingLongWaveRadiation_computed = 0.744
    assert (netOutGoingLongWaveRadiation_estimated == netOutGoingLongWaveRadiation_computed)