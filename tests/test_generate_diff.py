import pytest
from gendiff import generate_diff


result_plain = open('tests/fixtures/result_plain.txt').read()

@pytest.fixture
def json_path1():
    return "./tests/fixtures/file1.json"


@pytest.fixture
def json_path2():
    return "./tests/fixtures/file2.json"


@pytest.fixture
def yaml_path1():
    return "./tests/fixtures/file1.yaml"


@pytest.fixture
def yaml_path2():
    return "./tests/fixtures/file2.yml"


def test_generate_diff_json(json_path1, json_path2):
    assert generate_diff(json_path1, json_path2) == result_plain


def test_generate_diff_yaml(yaml_path1, yaml_path2):
    assert generate_diff(yaml_path1, yaml_path2) == result_plain