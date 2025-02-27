import numpy as np
import scipy as sp

class Spectrum:
    def __init__(self, stype, frequencies, intensities, labels=None):
        self.stype = stype
        self.frequencies = frequencies
        self.intensities = intensities
        self.labels = labels
    
    @staticmethod
    def initialize(frequencies, intensities, stype):
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
    
    def __str__(self):
        all_info = f"Spectrum type: {self.stype}\n\nFrequencies: \n\n{self.frequencies}\nIntensities: \n\n{self.intensities}\n"
        if self.labels != None:
            extra_info = "\nLabels:"
            for k, v in self.labels.items():
                extra_info += f"\n\tKey: {k}\n\tValue: {v}"
            all_info += extra_info
        return all_info
        
    def normalize(self):
        max_val = np.max(self.intensities)
        normalized_intensities = self.intensities / max_val
        return Spectrum(self.stype, self.frequencies, normalized_intensities)
        
    def scale(self, scale_factor):
        if not isinstance(scale_factor, float):
            raise ValueError("Scale factor must be float.")
        scaled_frequencies = self.frequencies * scale_factor
        return Spectrum(self.stype, scaled_frequencies, self.intensities)
    
    def add_label(self, key, value):
        if not isinstance(self.labels, dict):
            self.labels = {}
        self.labels[key] = value
