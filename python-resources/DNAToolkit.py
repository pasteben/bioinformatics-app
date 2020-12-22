# DNA Toolkit file
import collections
from structures import *

# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverseComplement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]