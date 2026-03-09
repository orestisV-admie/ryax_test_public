from pathlib import Path
import pandas as pd

def handle(request: dict)->dict:
    # Parameters
    win_len, win_step = 50,10
    
    # Create the output directory
    out_dir = Path("/tmp/windows")
    out_dir.mkdir(exist_ok=True)

    # Scan the file and output the window .parquet
    data_file = Path(request["data"])
    data = pd.read_parquet(data_file)
    for n,t in enumerate(data.rolling(win_len, step=win_step, center=False)):
        if len(t)==win_len:
            t.to_parquet(out_dir.joinpath(f"window_{n}.parquet"))

    return {"windows":out_dir.absolute().as_posix()}