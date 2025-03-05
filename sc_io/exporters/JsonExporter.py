import json
import os
import numpy as np

class JsonExporter:
    def __init__(self, freq_label, int_label, force):
        self.freq_label = freq_label
        self.int_label = int_label
        self.force = force

    @staticmethod
    def initialize(freq_label, int_label, force=False):
        if not isinstance(freq_label, str) or not isinstance(int_label, str):
            raise ValueError("Labels must be of type str.")
        if force != True and force != False:
            raise ValueError("Force variable must be either True or False.")
        return JsonExporter(freq_label, int_label, force)

    def export(self, frequencies, intensities, output_path):
        if not isinstance(frequencies, (list, tuple, np.ndarray)) or not isinstance(intensities, (list, tuple, np.ndarray)):
            raise ValueError("Frequencies and intensities must be lists, tuples or numpy arrays.")
        if len(frequencies) != len(intensities):
            raise ValueError("Frequencies and intensities must have the same length.")
        if os.path.isfile(output_path) and not self.force:
            raise FileExistsError("The output path specified already exists...Exiting.")
        
        freq_list = frequencies.tolist() if isinstance(frequencies, np.ndarray) else list(frequencies)
        int_list = intensities.tolist() if isinstance(intensities, np.ndarray) else list(intensities)
        
        data = {
            self.freq_label: freq_list,
            self.int_label: int_list
        }
        
        with open(output_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
