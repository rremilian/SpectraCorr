import numpy as np
from generators.BaseGenerator import BaseGenerator

class LorentzianGenerator(BaseGenerator):
    def __init__(self, freqlist, intlist, fmin, fmax, step, sigma):
        super().__init__(freqlist, intlist, fmin, fmax, step, sigma)

    def distribution_function(self, freq, sigma, x):
        return (1.0/np.pi) * (sigma/((x-freq)**2 + sigma**2))