import pytest
from gendiff import generate_diff


result = open('tests/fixtures/result.txt').read()
result_tree = open('tests/fixtures/result_tree.txt').read()
result_json = open('tests/fixtures/result_json.txt').read()
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


@pytest.fixture
def json_tree_path1():
    return "./tests/fixtures/file1_tree.json"


@pytest.fixture
def json_tree_path2():
    return "./tests/fixtures/file2_tree.json"


def test_generate_diff_json(json_path1, json_path2):
    assert generate_diff(json_path1, json_path2) == result


def test_generate_diff_yaml(yaml_path1, yaml_path2):
    assert generate_diff(yaml_path1, yaml_path2) == result


def test_generate_diff_tree(json_tree_path1, json_tree_path2):
    assert generate_diff(json_tree_path1, json_tree_path2, format_name='stylish') == result_tree


def test_generate_diff_tree_json(json_tree_path1, json_tree_path2):
    assert generate_diff(json_tree_path1, json_tree_path2, format_name='json') == result_json


def test_generate_diff_plain(json_tree_path1, json_tree_path2):
    assert generate_diff(json_tree_path1, json_tree_path2, format_name='plain') == result_plain
