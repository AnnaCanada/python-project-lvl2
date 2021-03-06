import argparse


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f', '--format', help='set format of output',
        choices=['plain', 'stylish', 'json'], default='stylish'
    )

    args = parser.parse_args()
    return args
