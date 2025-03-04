import numpy as np
from generators.BaseGenerator import BaseGenerator

class GaussianGenerator(BaseGenerator):
    def __init__(self, fmin, fmax, step, sigma):
        super().__init__(fmin, fmax, step, sigma)

    def distribution_function(self, freq, sigma, x):
        return 1.0/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*((x-freq)/sigma)**2)