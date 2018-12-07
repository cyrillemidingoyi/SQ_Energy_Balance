import numpy as np 
from copy import copy
from math import *

def soilevaporation(diffusionLimitedEvaporation=6605.505,
                    energyLimitedEvaporation=448.24):
    """


    SoilEvaporation Model
    Author: Pierre Martre
    Reference: Modelling energy balance in the wheat crop model SiriusQuality2:
            Evapotranspiration and canopy and soil temperature calculations
    Institution: INRA Montpellier
    Abstract: Starting from a soil at field capacity, soil evaporation  is assumed to
                be energy limited during the first phase of evaporation and diffusion limited thereafter.
                Hence, the soil evaporation model considers these two processes taking the minimum between
                the energy limited evaporation (PtSoil) and the diffused limited
                evaporation 

    """
    soilEvaporation = min(diffusionLimitedEvaporation, energyLimitedEvaporation)
    return  soilEvaporation
