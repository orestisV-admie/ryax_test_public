import json
from pathlib import Path
import pandas as pd

def handle(request: dict)->dict:
    data_file = Path(request["data"])
    data = pd.read_parquet(data_file)
    results = {"rows":len(data)}
    return {"results":json.dumps(results)}