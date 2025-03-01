import pytest
import numpy as np

@pytest.fixture
def sample_frequencies():
    return np.array([100.0, 200.0, 300.0])

@pytest.fixture
def sample_intensities():
    return np.array([0.5, 1.0, 0.7])

@pytest.fixture
def temp_ir_file(tmp_path):
    d = tmp_path / "test"
    d.mkdir()
    p = d / "test.hess"
    p.write_text("$ir_spectrum\n3\n100.0 0.1 0.5\n200.0 0.2 0.7\n300.0 0.3 0.9\n$end")
    return p

@pytest.fixture
def temp_raman_file(tmp_path):
    d = tmp_path / "test"
    d.mkdir()
    p = d / "test.hess"
    p.write_text("$raman_spectrum\n3\n100.0 0.5 0.1\n200.0 0.7 0.2\n300.0 0.9 0.3\n$end")
    return p

@pytest.fixture
def temp_csv_file(tmp_path):
    d = tmp_path / "test"
    d.mkdir()
    p = d / "test.csv"
    p.write_text("Frequency,Intensity\n100.0,0.5\n200.0,0.7\n300.0,0.9\n")
    return p