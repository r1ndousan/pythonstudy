import pytest
from hw6_2 import merge_and_write

@pytest.fixture
def testing_files(tmp_path):
    file1 = tmp_path / 'file1.txt'
    file2 = tmp_path / 'file2.txt'

    with open(file1, 'w') as f1:
        f1.write('h6')
    with open(file2, 'w') as f2:
        f2.write('w2')
    output_file = tmp_path / 'output.txt'

    return file1, file2, output_file

def testing_output(testing_files):
    file1, file2, output_file = testing_files
    assert merge_and_write(file1, file2, output_file) == 'h6 w2'

def testing_exist(testing_files):
    file1, file2, output_file = testing_files
    assert merge_and_write(file1, 'test.txt', output_file) == "Один из файлов не найден"
    assert merge_and_write('test.txt', file2, output_file) == "Один из файлов не найден"
    assert merge_and_write('test1.txt', 'test2.txt', output_file) == "Один из файлов не найден"