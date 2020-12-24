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

    data = []

    for (key, value) in FASTADict.items():
        result = {
            "label": key,
            "sequence": value
        }
        if "window" in content:
            result["codon_usage"] = codon_usage_subseq(value, int(content["window"]))
        else:
            result["codon_usage"] = codon_usage(value)

        data.append(result)

if "sequence" in content:
    sequence = validateSeq(content["sequence"])

    data = {
        "sequence": sequence
    }

    if "window" in content:
        data["codon_usage"] = codon_usage_subseq(sequence, int(content["window"]))
    else:
        data["codon_usage"] = codon_usage(sequence)

print(json.dumps({
    "data": data
}))