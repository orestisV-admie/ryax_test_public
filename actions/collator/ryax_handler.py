import json
from pathlib import Path
# import pandas as pd

def handle(request: dict)->dict:
    # Get the directory with the results .json
    in_dir = Path(request["results"])

    # Collect the results in a list
    results = []
    for fname in in_dir.glob("*.json"):
        with open(fname, "r") as resf:
            res:dict = json.load(resf)
            if res["anomalous"]:
                results.append(res)

    return {"report":json.dumps(results)}