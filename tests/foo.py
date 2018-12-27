#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Sample Open Science App.')
parser.add_argument('-v', action='store_true')
parser.add_argument('args', type=str, nargs='*')


def foo():
    args = parser.parse_args()
    if args.v:
        print("""
        Sample Open Science App v0.0
        BFOROS Id: https://github.com/ficolo/biotea-annotation
        """)
    else:
        print('Foo was called with:' + str(args.args))


if __name__ == "__main__":
    foo()
