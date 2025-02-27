import numpy as np

class OrcaParser:
    def __init__(self):
        pass
    def parse_spectral_data(self, hess_file, stype):
        with open(hess_file, 'r') as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]

        start_marker = f'${stype}_spectrum'
        parsing = False
        data = []
        for line in lines:
            if line.startswith('$') and parsing:
                break
            elif line == start_marker:
                parsing = True
                continue
            elif parsing:
                if line:
                    data.append(line)

        data = np.array([line.split() for line in data], dtype=float)
        frequencies = data[:, 0]
        intensities = data[:, 2]
        return (frequencies, intensities)