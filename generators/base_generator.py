import numpy as np
import os
from core.spectrum import Spectrum


class BaseGenerator:
    def __init__(self, freqlist, intlist, fmin, fmax, step, sigma):
        self.freqlist = freqlist
        self.intlist = intlist
        self.fmin = fmin
        self.fmax = fmax
        self.step = step
        self.sigma = sigma
        self.nstep = int(round((self.fmax - self.fmin)/self.step) + 1)
        self.frequencies = []
        self.intensities = []
        for i in range(self.nstep):
            self.frequencies.append(self.fmin + i * self.step)

    @classmethod
    def initialize(cls, freqlist, intlist, fmin, fmax, step, sigma):
        if not isinstance(freqlist, np.ndarray) or not isinstance(intlist, np.ndarray):
            raise ValueError("The variables 'freqlist' and 'intlist' must be numpy arrays.")
        if not isinstance(fmin, int) or not isinstance(fmax, int):
            raise ValueError("Varibles 'fmin' and 'fmax' must be integers.")
        if fmax <= fmin:
            raise ValueError("'fmax' must be greater than 'fmin'")
        if isinstance(sigma, int):
            sigma = float(sigma)
        if isinstance(step, int):
            step = float(step)
        if not isinstance(sigma, float):
            raise ValueError("The variable 'sigma' must be float.")
        if not isinstance(step, float):
            raise ValueError("The variable 'step' must be integer.")
        
        return cls(freqlist, intlist, fmin, fmax, step, sigma)
    
    def distribution_function(self, freq, sigma, x):
        pass

    def generate_spectrum(self, stype):
        temp = np.empty((self.nstep, len(self.freqlist)))
        for i in range(len(self.freqlist)):
            temp[:,i] = self.intlist[i] * self.distribution_function(self.freqlist[i], self.sigma, np.asarray(self.frequencies))
        self.intensities = np.sum(temp, axis=1, dtype=float)
        return Spectrum(stype, self.frequencies, self.intensities)