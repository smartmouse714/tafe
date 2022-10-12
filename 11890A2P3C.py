#!/usr/bin/env python
"""Permute a list of clues to produce a wordlist

This bare minimum implementation is a Proof of Concept only.
"""
import argparse
import itertools

def main(arg):
    if len(arg.clues) > 2:
        p, u = zip(*list(itertools.product(arg.clues, repeat=2)))
        for (a, b) in ((arg.u, u), (arg.p, p)):
            with open(a, 'w') as f:
                [f.write(i+'\n') for i in b]
    else:
        print('Please enter at least 3 clues')

if __name__	== '__main__':
    parser = argparse.ArgumentParser(prog='permute_clues',
                                     description='A wordlist generator')
    parser.add_argument('-p', help='password filename',
                        metavar='PASS', default='pass')
    parser.add_argument('-u', help='username filename',
                        metavar='USER', default='user')
    parser.add_argument('clues', nargs='*')
    main(parser.parse_args())
