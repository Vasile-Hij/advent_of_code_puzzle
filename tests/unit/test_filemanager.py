from utils.config import FileManager
import pytest


def test_filemanager_read_input_creates_file():
    data = FileManager.read_input_file(
        FileManager.INPUT_DAY, year=2025, day=1, method="solve"
    )
    assert isinstance(data, list)
