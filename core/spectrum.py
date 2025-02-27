import numpy as np
import scipy as sp

class Spectrum:
    def __init__(self, stype, frequencies, intensities):
        self.stype = stype
        self.frequencies = frequencies
        self.intensities = intensities
    
        @staticmethod
        def initialize(stype, frequencies, intensities):
            valid_stypes = ["ir", "raman"]
            if stype.lower() not in valid_stypes:
                raise ValueError("Spectrum type must be IR or Raman")
            if not isinstance(frequencies, np.ndarray):
                raise TypeError("Frequencies must be a numpy array.")
            if not isinstance(intensities, np.ndarray):
                raise TypeError("Intensities must be a numpy array.")
            if frequencies.shape != intensities.shape:
                raise ValueError("You must have an equal number of frequencies and intensities.")
            return Spectrum(stype, frequencies, intensities)
        
        def normalize(self):
            max_val = np.max(self.intensities)
            normalized_intensities = self.intensities / max_val
            return Spectrum(self.stype, self.frequencies, normalized_intensities)
        
        def scale(self, scale_factor):
            if not isinstance(scale_factor, float):
                raise ValueError("Scale factor must be float.")
            scaled_frequencies = self.frequencies / scale_factor
            return Spectrum(self.type, scaled_frequencies, self.intensities)
