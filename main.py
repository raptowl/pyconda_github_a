import argparse

from mymodule.mod1 import NormalMyAdder, ListMyAdder, NumpyMyAdder


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-a', '--num_a', help='number a',
                        type=int, required=True)
    parser.add_argument('-b', '--num_b', help='number b',
                        type=int, required=True)
    args = parser.parse_args()

    a = args.num_a
    b = args.num_b
    adder1 = NormalMyAdder(a, b)
    adder2 = ListMyAdder(a, b)
    adder3 = NumpyMyAdder(a, b)
    print(f'{adder1.add()}')
    print(f'{type(adder1.add())}')
    print(f'{adder2.add()}')
    print(f'{type(adder2.add())}')
    print(f'{adder3.add()}')
    print(f'{type(adder3.add())}')
