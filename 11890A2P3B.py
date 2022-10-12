#!/usr/bin/env python
"""Convert a text of hex to binary

This bare minimum implementation is a Proof of Concept only.
"""
import argparse

def main(opt):
    """"Read a text file and write a binary file
    """
    try:
        with open(opt.i) as f:
            data = f.read()
    except FileNotFoundError:
        print('Input not found')
    else:
        # Clean data by stripping whitespaces and 0x-prefix.
        txt = [i.strip().removeprefix('0x') for i in data.split(',')]
        file_bytes = bytes.fromhex(''.join(txt))
        with open(opt.o,'wb') as f:
            size = f.write(file_bytes)
            print(f"{opt.o} has {size} bytes")

if __name__	== '__main__':
    parser = argparse.ArgumentParser(prog='txt2bin', description='A txt2bin converter')
    parser.add_argument('-i', required=True, metavar='INPUT')
    parser.add_argument('-o', metavar='OUTPUT', default='myfile.dat')
    main(parser.parse_args())
