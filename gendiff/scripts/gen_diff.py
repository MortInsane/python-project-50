import argparse


def gendiff_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files ans shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()


def main():
    gendiff_args()


if __name__ == '__main__':
    main()
