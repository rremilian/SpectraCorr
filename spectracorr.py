class SpectraCorr:
    def __init__(self):
        pass
    def parseOrca(self, hess_file, stype):
        from sc_io.parsers.OrcaParser import OrcaParser
        parser = OrcaParser()
        spectral_data = parser.parse_spectral_data(hess_file, stype)
        return spectral_data
    def parseCsv(self, csv_file, stype, freq_column = 0, int_column = 0):
        from sc_io.parsers.CsvParser import CsvParser
        parser = CsvParser()
        spectral_data = parser.parse_spectral_data(csv_file, stype, 
                                                   freq_column=freq_column, 
                                                   int_column=int_column)
        return spectral_data
    def initSpectrum(self, frequencies, intensities, stype):
        from core.spectrum import Spectrum
        return Spectrum.initialize(frequencies, intensities, stype)