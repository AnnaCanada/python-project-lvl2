from gendiff import generate_diff
from tests import flat_json


def test_flat_json():
    verifiable = generate_diff('file1.json',
                               'file2.json')
    assert verifiable == flat_json