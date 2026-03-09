import json
from pathlib import Path
import pandas as pd
from random import random

def analyse(df:pd.DataFrame)->dict:
    # Dummy 'analysis'
    anomalous = random()<.01
    return {"start":df.index.start, "end":df.index.end, "anomalous":anomalous}

def handle(request: dict)->dict:
    # Get the directory with window .parquet
    in_dir = Path(request["windows"])

    # Analyse the files
    out_dir = Path("/tmp/results")
    out_dir.mkdir(exist_ok=True)
    for file in in_dir.glob("*.parquet"):
        df = pd.read_parquet(file)
        res = analyse(df)
        with open(out_dir.joinpath(f"{file.with_stem}.json"), "w") as jfile:
            json.dump(res, jfile)
    
    return {"results":out_dir.absolute().as_posix()}