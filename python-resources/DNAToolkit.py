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

def countNucFrequencySubsec(seq, k=20):
    results = []
    for i in range(0, len(seq) - k + 1,  k):
        subseq = seq[i:i + k]
        result = {
            "subsequence": subseq,
            "nucleotide_count": countNucFrequency(subseq)
        }
        results.append(result)
    return results

def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverseComplement(seq):
    # mapping = str.maketrans('ATCG', 'TAGC')
    # return seq.translate(mapping)[::-1]
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]

def gcContent(seq):
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) *  100), 6)

def gcContentSubsec(seq, k=20):
    results = []
    for i in range(0, len(seq) - k + 1,  k):
        subseq = seq[i:i + k]
        result = {
            "subsequence": subseq,
            "gc_content": gcContent(subseq)
        }
        results.append(result)
    return results

def translate_seq(seq, init_pos=0):
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -  2, 3)]

def translate_subseq(seq, k=20):
    results = []
    for i in range(0, len(seq) - k + 1,  k):
        subseq = seq[i:i + k]
        result = {
            "subsequence": subseq,
            "amino_acid_sequence": translate_seq(subseq)
        }
        results.append(result)
    return results

def codon_usage_single(seq, amino_acid):
    tmpList = []
    for i in range(0, len(seq)  - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == amino_acid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(collections.Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWeight, 2)
    return freqDict

def codon_usage(seq):
    result = {}
    for codon in Codons:
        result[codon] = codon_usage_single(seq, codon)
    return result

def codon_usage_subseq(seq, k=20):
    results = []
    for i in range(0, len(seq) - k + 1,  k):
        subseq = seq[i:i + k]
        result = {
            "subsequence": subseq,
            "codon_usage": codon_usage(subseq)
        }
        results.append(result)
    return results