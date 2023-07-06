from importlib.resources import files

import pytest

from mrisim.config import read_config

default = files("mrisim.config") / "config.ini"
directory = files("mrisim.config.tests") / "data"
valid = directory / "config_valid.ini"
invalid1 = directory / "config_invalid_1.ini"
invalid2 = directory / "config_invalid_2.ini"
invalid3 = directory / "config_invalid_3.ini"
invalid4 = directory / "config_invalid_4.ini"
invalid5 = directory / "config_invalid_5.ini"


def test_read_config():
    """Test loading of a valid and invalid configuration."""
    key, repetition, period, wait_start = read_config(valid)
    assert isinstance(key, str)
    assert isinstance(repetition, int)
    assert 0 < repetition
    assert isinstance(period, float)
    assert isinstance(wait_start, float)

    with pytest.raises(FileNotFoundError, match="does not exist"):
        read_config("101.ini")
    with pytest.raises(ValueError, match="4 keys"):
        read_config(invalid1)
    with pytest.raises(ValueError, match="a single 'params' section"):
        read_config(invalid2)
    with pytest.raises(ValueError, match="strictly positive"):
        read_config(invalid3)
    with pytest.raises(ValueError, match="positive number"):
        read_config(invalid4)
    with pytest.raises(ValueError, match="positive number"):
        read_config(invalid5)


def test_read_default_config():
    """Test loading of the default configuration."""
    key, repetition, period, wait_start = read_config(default)
    assert key == "5"
    assert repetition == 5
    assert period == 1.0
    assert wait_start == 15
