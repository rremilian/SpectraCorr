import numpy as np

class OrcaParser:
    def __init__(self):
        pass
    def parse_spectral_data(self, hess_file, stype):
        with open(hess_file, 'r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        start_marker = f'${stype}_spectrum'
        data = []
        parsing = False
        index = 0
        
        if stype == 'ir':
            intensities_row = 2
        elif stype == 'raman':
            intensities_row = 1

        while index < len(lines):
            line = lines[index]
            if line.startswith('$') and parsing:
                break
            elif line == start_marker:
                index += 1 # Skip the number of atoms
                parsing = True
            elif parsing:
                if line:
                    data.append(line)
            index += 1

        data = np.array([line.split() for line in data], dtype=float)
        frequencies = data[:, 0]
        intensities = data[:, intensities_row]
        return (frequencies, intensities)