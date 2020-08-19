import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-a', '--num_a', help='number a',
                        type=int, required=True)
    parser.add_argument('-b', '--num_b', help='number b',
                        type=int, required=True)
    args = parser.parse_args()
