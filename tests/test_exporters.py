import pytest
import os
import json
from sc_io.exporters.CsvExporter import CsvExporter
from sc_io.exporters.JsonExporter import JsonExporter

class TestCsvExporter:
    def test_invalid_labels(self):
        with pytest.raises(ValueError, match="Columns labels must be of type str."):
            CsvExporter.initialize(123, "Int", ",")
        with pytest.raises(ValueError, match="Columns labels must be of type str."):
            CsvExporter.initialize("Freq", None, ",")

    def test_invalid_delimiter(self):
        with pytest.raises(ValueError, match="Delimiter variable must be a str."):
            CsvExporter.initialize("Freq", "Int", None)
        with pytest.raises(ValueError, match="Delimiter variable must have exactly one character."):
            CsvExporter.initialize("Freq", "Int", ",,")

    def test_export_csv(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test.csv"
        exporter = CsvExporter.initialize("Freq", "Int", ",")
        exporter.export(sample_frequencies, sample_intensities, str(output_file))

        assert output_file.exists()
        content = output_file.read_text()
        lines = content.strip().split('\n')
        assert lines[0] == "Freq,Int"
        assert lines[1] == "100.0,0.5"
        assert lines[2] == "200.0,1.0"
        assert lines[3] == "300.0,0.7"

    def test_file_exists_error(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test.csv"
        output_file.write_text("existing content")

        exporter = CsvExporter.initialize("Freq", "Int", ",")
        with pytest.raises(FileExistsError):
            exporter.export(sample_frequencies, sample_intensities, str(output_file))

    def test_force_overwrite_csv(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test_overwrite.csv"
        output_file.write_text("Old,Data\n1.0,2.0")

        exporter = CsvExporter.initialize("Freq", "Int", ",", force=True)
        exporter.export(sample_frequencies, sample_intensities, str(output_file))

        content = output_file.read_text()
        lines = content.strip().split('\n')
        assert lines[0] == "Freq,Int"
        assert lines[1] == "100.0,0.5"
        assert lines[2] == "200.0,1.0"
        assert lines[3] == "300.0,0.7"

class TestJsonExporter:
    def test_invalid_labels_json(self):
        with pytest.raises(ValueError, match="Labels must be of type str."):
            JsonExporter.initialize(123, "Int")
        with pytest.raises(ValueError, match="Labels must be of type str."):
            JsonExporter.initialize("Freq", None)

    def test_export_json(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test.json"
        exporter = JsonExporter.initialize("Freq", "Int")
        exporter.export(sample_frequencies, sample_intensities, str(output_file))
        
        assert output_file.exists()
        with open(output_file) as f:
            data = json.load(f)
            assert "Freq" in data
            assert "Int" in data
            assert data["Freq"] == [100.0, 200.0, 300.0]
            assert data["Int"] == [0.5, 1.0, 0.7]

    def test_file_exists_error(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test.json"
        output_file.write_text("{}")
        
        exporter = JsonExporter.initialize("Freq", "Int")
        with pytest.raises(FileExistsError):
            exporter.export(sample_frequencies, sample_intensities, str(output_file))

    def test_force_overwrite(self, tmp_path, sample_frequencies, sample_intensities):
        output_file = tmp_path / "test_overwrite.json"
        output_file.write_text("{}")
        
        exporter = JsonExporter.initialize("Freq", "Int", force=True)
        exporter.export(sample_frequencies, sample_intensities, str(output_file))
        
        with open(output_file) as f:
            data = json.load(f)
            assert data["Freq"] == [100.0, 200.0, 300.0]
