import pytest

from dura import format, parse


def test_seconds_and_minutes():
    assert parse("90s") == 90
    assert parse("2m") == 120


def test_days():
    assert parse("2d") == 172800


def test_rejects_garbage():
    with pytest.raises(ValueError):
        parse("ten minutes")


def test_format_minutes():
    assert format(150) == "2m30s"
