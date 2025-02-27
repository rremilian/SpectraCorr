class SpectraCorr:
    def __init__(self):
        pass
    def parseOrca(hess_file, stype):
        from io.parsers.OrcaParser import OrcaParser
        parser = OrcaParser()
        spectral_data = parser.parse_spectral_data(hess_file, stype)
        return spectral_data
    def parseCsv(csv_file, stype, freq_column = 0, int_column = 0):
        from io.parsers.CsvParser import CsvParser
        parser = CsvParser()
        spectral_data = parser.parse_spectral_data(csv_file, stype, 
                                                   freq_column=freq_column, 
                                                   int_column=int_column)
        return spectral_data
    def initSpectrum(frequencies, intensities, stype):
        from core.spectrum import Spectrum
        return Spectrum.initialize(frequencies, intensities, stype)