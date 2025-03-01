import pytest
import numpy as np
from spectracorr import parseOrca, parseCsv, initSpectrum, initGenerator
from core.Spectrum import Spectrum
from generators.GaussianGenerator import GaussianGenerator
from generators.LorentzianGenerator import LorentzianGenerator

class TestSpectracorr:
    
    def test_parse_orca_ir(self, temp_ir_file):
        frequencies, intensities = parseOrca(temp_ir_file, "ir")
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3
        assert len(intensities) == 3
        
    def test_parse_orca_raman(self, temp_raman_file):
        frequencies, intensities = parseOrca(temp_raman_file, "raman")
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3
        assert len(intensities) == 3

    def test_parse_orca_invalid_type(self, temp_ir_file):
        with pytest.raises(ValueError, match="Invalid spectrum type"):
            parseOrca(temp_ir_file, "invalid")

    def test_parse_csv_default_columns(self, temp_csv_file):
        frequencies, intensities = parseCsv(temp_csv_file)
        assert isinstance(frequencies, np.ndarray)
        assert isinstance(intensities, np.ndarray)
        assert len(frequencies) == 3
        assert len(intensities) == 3

    def test_parse_csv_invalid_freq_column(self, temp_csv_file):
        with pytest.raises(IndexError):
            parseCsv(temp_csv_file, freq_column=5, int_column=1)

    def test_parse_csv_invalid_int_column(self, temp_csv_file):
        with pytest.raises(IndexError):
            parseCsv(temp_csv_file, freq_column=0, int_column=5)

    def test_init_spectrum_invalid_type(self, sample_frequencies, sample_intensities):
        with pytest.raises(ValueError, match="Spectrum type must be IR or Raman"):
            initSpectrum(sample_frequencies, sample_intensities, "invalid")

    def test_init_generator_gaussian(self):
        generator = initGenerator(0, 2500, 1.0, 2.0, "gaussian")
        assert isinstance(generator, GaussianGenerator)

    def test_init_generator_lorentzian(self):
        generator = initGenerator(0, 2500, 1.0, 2.0, "lorentzian")
        assert isinstance(generator, LorentzianGenerator)

    def test_init_generator_invalid_dist(self):
        with pytest.raises(ValueError, match="Variable 'dist' must be 'gaussian' or 'lorentzian'"):
            initGenerator(0, 2500, 1.0, 2.0, "invalid")

    def test_init_generator_invalid_fmin(self):
        with pytest.raises(ValueError):
            initGenerator("invalid", 2500, 1.0, 2.0, "gaussian")
    
    def test_init_generator_invalid_fmax(self):
        with pytest.raises(ValueError):
            initGenerator(500, "invalid", 1.0, 2.0, "gaussian")

    def test_init_generator_invalid_step(self):
        with pytest.raises(ValueError):
            initGenerator(500, 2500, "invalid", 2.0, "gaussian")

    def test_init_generator_invalid_sigma(self):
        with pytest.raises(ValueError):
            initGenerator(500, 2500, 1.0, "invalid", "gaussian")

    def test_init_generator_invalid_dist(self):
        with pytest.raises(ValueError):
            initGenerator(500, 2500, 1.0, 2.0, "invalid")