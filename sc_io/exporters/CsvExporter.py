import csv
import os
import numpy as np

class CsvExporter:
    def __init__(self, column1_label, column2_label, delimiter, force):
        self.column1_label = column1_label
        self.column2_label = column2_label
        self.delimiter = delimiter
        self.force = force

    @staticmethod
    def initialize(column1_label, column2_label, delimiter, force=False):
        if not isinstance(column1_label, str) or not isinstance(column2_label, str):
            raise ValueError("Columns labels must be of type str.")
        if not isinstance(delimiter, str):
            raise ValueError("Delimiter variable must be a str.")
        if len(delimiter) != 1:
            raise ValueError("Delimiter variable must have exactly one character.")
        if force != True and force != False:
            raise ValueError("Force variable must be either True or False.")
        return CsvExporter(column1_label, column2_label, delimiter, force)

    def export(self, frequencies, intensities, output_path):  # Added missing colon
        if not isinstance(frequencies, (list, tuple, np.ndarray)) or not isinstance(intensities, (list, tuple, np.ndarray)):
            raise ValueError("Frequencies and intensities must be lists, tuples or numpy arrays.")
        if len(frequencies) != len(intensities):
            raise ValueError("Frequencies and intensities must have the same length.")
        if os.path.isfile(output_path) and not self.force:
            raise FileExistsError("The output path specified already exists...Exiting.")
        with open(output_path, "w", newline='') as csv_output:
            writer = csv.writer(csv_output, delimiter=self.delimiter)
            writer.writerow([self.column1_label, self.column2_label])
            writer.writerows(zip(frequencies, intensities))
