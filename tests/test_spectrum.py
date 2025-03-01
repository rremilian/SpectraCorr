import pytest
import numpy as np
from core.Spectrum import Spectrum

def test_spectrum_initialization(sample_frequencies, sample_intensities):
    spectrum = Spectrum.initialize(sample_frequencies, sample_intensities, "ir")
    assert isinstance(spectrum, Spectrum)
    assert np.array_equal(spectrum.frequencies, sample_frequencies)
    assert np.array_equal(spectrum.intensities, sample_intensities)

def test_invalid_spectrum_type(sample_frequencies, sample_intensities):
    with pytest.raises(ValueError, match="Spectrum type must be IR or Raman"):
        Spectrum.initialize(sample_frequencies, sample_intensities, "invalid")

def test_normalize(sample_frequencies, sample_intensities):
    spectrum = Spectrum.initialize(sample_frequencies, sample_intensities, "ir")
    normalized = spectrum.normalize()
    assert np.max(normalized.intensities) == 1.0

def test_scale(sample_frequencies, sample_intensities):
    spectrum = Spectrum.initialize(sample_frequencies, sample_intensities, "ir")
    scale_factor = 0.5
    scaled = spectrum.scale(scale_factor)
    assert np.allclose(scaled.frequencies, sample_frequencies * scale_factor)

def test_add_label(sample_frequencies, sample_intensities):
    spectrum = Spectrum.initialize(sample_frequencies, sample_intensities, "ir")
    spectrum.add_label("test", "value")
    assert spectrum.labels["test"] == "value"