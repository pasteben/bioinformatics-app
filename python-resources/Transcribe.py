# DNA Toolset/Code testing file
from DNAToolkit import *
import sys
import json

dnaStr=sys.argv[1]

DNAStr = validateSeq(dnaStr)

print(transcription(DNAStr), end='')