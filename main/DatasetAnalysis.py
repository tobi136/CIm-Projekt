import AminoAcid
import argparse

# TODO: calculate data, create scatter plots or whatever
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Occurence Matrix Generator")

    parser.add_argument('input', metavar='input file')

    args = parser.parse_args()

    # Parse the sequences into two String lists of binder and non-binder sequences
    binders = []
    nonBinders = []
    with open(args.input, "r") as i:
        for e in i:
            lineSplit = e.split()
            if lineSplit[0] == "Peptide":
                pass
            else:
                if int(lineSplit[2]) == 1:
                    binders.append(lineSplit[0])
                else:
                    nonBinders.append(lineSplit[0])