# DNA Toolset/Code testing file
from DNAToolkit import *
import sys
import json

dnaStr=sys.argv[1]
window=sys.argv[2]

DNAStr = validateSeq(dnaStr)

print(json.dumps(gcContentSubsec(DNAStr, int(window))))