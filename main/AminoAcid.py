class AminoAcid(object):
    # Konstruktor
    def __init__(self, one_letter_code, flexibility, weight, iep, hydrophobicity):
        self.one_letter_code = one_letter_code

        self.flexibility = flexibility  # Flexibility of the side chain,
        # one of ["None", "Low", "Limited", "Moderate", "High", "Restricted"]

        self.weight = weight  # Molecular weight (in units, I guess...)
        self.iep = iep  # Isoelectric Point
        self.hydrophobicity = hydrophobicity  # TODO: What unit does hydrophobicity have?


# TODO: Gibt es sinnvolle Methoden?
# End of class definition

# Instances for all possible 20 amino acids
# Data resource: https://www.ncbi.nlm.nih.gov/Class/Structure/aa/aa_explorer.cgi
ala = AminoAcid('A', "Limited", 71, 6.0, 0.806)
cys = AminoAcid('C', "Low", 103, 5.0, 0.721)
asp = AminoAcid('D', "Moderate", 115, 3.0, 0.417)
glu = AminoAcid('E', "High", 129, 3.2, 0.458)

# List all amino acids and their one-letter-codes, then zip them to a dictionary
# This dictionary, 'aminoAcidDict', will be accessed from the main program
aminoAcidList = [ala, cys, asp, glu, ]  # TODO: Complete
oneLetterCodeList = [acid.one_letter_code for acid in aminoAcidList]
aminoAcidDict = {key: value for (key, value) in zip(oneLetterCodeList, aminoAcidList)}
