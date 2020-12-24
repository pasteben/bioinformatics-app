# DNA Toolset/Code testing file
from DNAToolkit import *
import sys
import json
import base64

content = json.loads(base64.b64decode(sys.argv[1]))

if "dataset" in content:
    dataset = content["dataset"]

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

if "dna_string" in content:
    DNAStr = validateSeq(content["dna_string"])

    RESULTDict =  {"gc_content":  gcContent(DNAStr)}

    print(json.dumps(RESULTDict))