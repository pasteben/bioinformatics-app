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
            result["gc_content"] = gcContentSubsec(value, int(content["window"]))
        else:
            result["gc_content"] = gcContent(value)

        data.append(result)

if "sequence" in content:
    sequence = validateSeq(content["sequence"])

    data = {
        "sequence": sequence
    }

    if "window" in content:
        data["gc_content"] = gcContentSubsec(sequence, int(content["window"]))
    else:
        data["gc_content"] = gcContent(sequence)

print(json.dumps({
    "data": data
}))