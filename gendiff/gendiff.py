from gendiff import parser
from pathlib import Path
from gendiff.inner_view_diff import inner_view_diff
from gendiff.formats import choose_format


def generate_diff(file1, file2, format_name='stylish'):
    file1 = parser.get_method(Path(file1).suffix)(open(file1))
    file2 = parser.get_method(Path(file2).suffix)(open(file2))

    diff = inner_view_diff(file1, file2)
    format = choose_format(format_name)

    return format(diff)
