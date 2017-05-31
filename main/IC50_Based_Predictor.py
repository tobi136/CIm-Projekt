#!/usr/bin/env python

import argparse
from random import random

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Random Epitope Binding Predictor")

    parser.add_argument('input', metavar='input file')
    parser.add_argument('output', metavar='output file')

    args = parser.parse_args()

    binderICs = []
    nonBinderICs = []

    with open(args.output, "w") as o:
        with open(args.input, "r") as i:
            for e in i:
                lineSplit = e.split()
                if lineSplit[0] == "Peptide":
                    pass
                else:
                    if int(lineSplit[2]) == 1:
                        binderICs.append(float(lineSplit[1]))
                    else:
                        nonBinderICs.append(float(lineSplit[1]))
            maxBinderIC = max(binderICs)
            minNonBinderIC = min(nonBinderICs)
            print(nonBinderICs)
            print("Maximaler IC für Binder: " + str(maxBinderIC) + ", Minimaler IC für Nichtbinder: " + str(minNonBinderIC))

