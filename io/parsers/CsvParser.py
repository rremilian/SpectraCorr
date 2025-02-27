import csv
import numpy as np

class CsvParser:
    def __init__(self):
        pass
    def parse_spectral_data(self, csv_file, freq_column, int_column, stype):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            frequencies = []
            intensities = []
            for row in reader:
                try:
                    freq = float(row[freq_column])
                    intensity = float(row[int_column])
                    frequencies.append(freq)
                    intensities.append(intensity)
                except (ValueError, IndexError):
                    raise("There was an error when parsing the CSV file.")
        frequencies = np.array(frequencies)
        intensities = np.array(intensities)

        return (frequencies, intensities)