import csv
import numpy as np

class CsvParser:
    def __init__(self):
        pass
    def parse_spectral_data(self, csv_file, stype, freq_column = 0, int_column = 1):
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
                except ValueError:
                    raise ValueError(f"Could not convert value to float in row {reader.line_num}: {row}")
                except IndexError:
                    raise IndexError(f"Column index out of range for row {reader.line_num}.")
        frequencies = np.array(frequencies)
        intensities = np.array(intensities)

        return (frequencies, intensities)