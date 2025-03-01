import pytest
import numpy as np
from sc_io.parsers.OrcaParser import OrcaParser
from sc_io.parsers.CsvParser import CsvParser

class TestOrcaParser:
    def test_parse_ir_spectrum(self, temp_ir_file):
        parser = OrcaParser()
        frequencies, intensities = parser.parse_spectral_data(temp_ir_file, "ir")
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3

    def test_parse_raman_spectrum(self, temp_raman_file):
        parser = OrcaParser()
        frequencies, intensities = parser.parse_spectral_data(temp_raman_file, "raman")
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3

    def test_invalid_spectrum_type(self, temp_ir_file):
        parser = OrcaParser()
        with pytest.raises(ValueError):
            parser.parse_spectral_data(temp_ir_file, "invalid")

    def test_file_not_found(self):
        parser = OrcaParser()
        with pytest.raises(FileNotFoundError):
            parser.parse_spectral_data("nonexistent.hess", "ir")

class TestCsvParser:
    def test_parse_csv_file(self, temp_csv_file):
        parser = CsvParser()
        frequencies, intensities = parser.parse_spectral_data(temp_csv_file)
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3

    def test_invalid_freq_column(self, temp_csv_file):
        parser = CsvParser()
        with pytest.raises(IndexError):
            parser.parse_spectral_data(temp_csv_file, freq_column=5)

    def test_invalid_int_column(self, temp_csv_file):
        parser = CsvParser()
        with pytest.raises(IndexError):
            parser.parse_spectral_data(temp_csv_file, int_column=5)

    def test_file_not_found(self):
        parser = CsvParser()
        with pytest.raises(FileNotFoundError):
            parser.parse_spectral_data("nonexistent.csv")