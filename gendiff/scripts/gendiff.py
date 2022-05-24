#!/usr/bin/python3
import argparse


def parse_cli_arguments():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    parse_cli_arguments()