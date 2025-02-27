import pytest
import sys
import numpy as np
from sc_io.parsers.OrcaParser import OrcaParser
sys.path.insert(1, '../')

@pytest.fixture
def sample_ir_data(tmp_path):
    content = """
$ir_spectrum
3
    100.00    0.10    15.20    0.00
    200.00    0.20    25.30    0.00
    300.00    0.30    35.40    0.00
$end
"""
    test_file = tmp_path / "test_ir.out"
    test_file.write_text(content)
    return str(test_file)

@pytest.fixture
def sample_raman_data(tmp_path):
    content = """
$raman_spectrum
3
    150.00    22.10    0.00    0.00
    250.00    32.20    0.00    0.00
    350.00    42.30    0.00    0.00
$end
"""
    test_file = tmp_path / "test_raman.out"
    test_file.write_text(content)
    return str(test_file)

def test_parse_ir_spectrum(sample_ir_data):
    parser = OrcaParser()
    frequencies, intensities = parser.parse_spectral_data(sample_ir_data, 'ir')
    
    expected_frequencies = np.array([100.0, 200.0, 300.0])
    expected_intensities = np.array([15.20, 25.30, 35.40])
    
    np.testing.assert_array_almost_equal(frequencies, expected_frequencies)
    np.testing.assert_array_almost_equal(intensities, expected_intensities)

def test_parse_raman_spectrum(sample_raman_data):
    parser = OrcaParser()
    frequencies, intensities = parser.parse_spectral_data(sample_raman_data, 'raman')
    
    expected_frequencies = np.array([150.0, 250.0, 350.0])
    expected_intensities = np.array([22.10, 32.20, 42.30])
    
    np.testing.assert_array_almost_equal(frequencies, expected_frequencies)
    np.testing.assert_array_almost_equal(intensities, expected_intensities)

def test_file_not_found():
    parser = OrcaParser()
    with pytest.raises(FileNotFoundError):
        parser.parse_spectral_data('nonexistent_file.out', 'ir')

def test_invalid_spectrum_type(sample_ir_data):
    parser = OrcaParser()
    with pytest.raises(ValueError):
        parser.parse_spectral_data(sample_ir_data, 'invalid_type')