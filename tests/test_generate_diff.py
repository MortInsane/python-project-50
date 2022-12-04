import pytest
from gendiff import generate_diff


result_plain = open('tests/fixtures/result_plain.txt').read()

@pytest.fixture
def json_path1():
    return "./tests/fixtures/file1.json"


@pytest.fixture
def json_path2():
    return "./tests/fixtures/file2.json"


def test_generate_diff(json_path1, json_path2):
    assert generate_diff(json_path1, json_path2) == result_plain
