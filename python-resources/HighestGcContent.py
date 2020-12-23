# DNA Toolset/Code testing file
from DNAToolkit import *
import sys
import json

dataset=sys.argv[1]

FASTADict = {}

FASTALabel = ""

for line in dataset.splitlines():
    if '>'  in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

RESULTDict =  {key: gcContent(value) for (key, value) in FASTADict.items()}

print(json.dumps(RESULTDict))