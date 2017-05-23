#!/usr/bin/env python

import argparse
from random import random

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Random Epitope Binding Predictor")
    parser.add_argument('input', metavar='in-file')
    parser.add_argument('output', metavar='out-file')
    args = parser.parse_args()

    with open(args.output, "w") as o:
        with open(args.input, "r") as i:
            for e in i:
                o.write("%s\t%i\n" % (e.strip(), random() >= 0.5))
