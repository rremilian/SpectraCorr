from sc_io.parsers.CsvParser import CsvParser
from sc_io.parsers.OrcaParser import OrcaParser
from sc_io.exporters.CsvExporter import CsvExporter
from core.Spectrum import Spectrum
from generators.GaussianGenerator import GaussianGenerator
from generators.LorentzianGenerator import LorentzianGenerator

def parseOrca(hess_file, stype):
    parser = OrcaParser()
    spectral_data = parser.parse_spectral_data(hess_file, stype)
    return spectral_data

def parseCsv(csv_file, freq_column = 0, int_column = 1):
    parser = CsvParser()
    spectral_data = parser.parse_spectral_data(csv_file, 
                                                freq_column=freq_column, 
                                                int_column=int_column)
    return spectral_data

def initSpectrum(frequencies, intensities, stype):  
    return Spectrum.initialize(frequencies, intensities, stype)

def initGenerator(fmin, fmax, step, sigma, dist):
    if dist not in ["gaussian", "lorentzian"]:
        raise ValueError("Variable 'dist' must be 'gaussian' or 'lorentzian'.")
    if dist == "gaussian":
        generator = GaussianGenerator.initialize(fmin, fmax, step, sigma)
    else:
        generator = LorentzianGenerator.initialize(fmin, fmax, step, sigma)
    return generator

def initCsvExporter(column1_label, column2_label, delimiter):
    return CsvExporter.initialize(column1_label, column2_label, delimiter)