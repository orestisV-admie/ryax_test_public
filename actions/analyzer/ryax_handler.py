# import pandas as pd
import json
from pathlib import Path

def handle(request: dict)->dict:
    data_file = Path(request["data"])
    # data = pd.read_parquet(data_file)
    data = [1,2,3]
    results = {"rows":len(data)}
    return {"results":json.dumps(results)}