"""
    All that our output files need to get live.
"""
import logging
from pathlib import Path

import pandas as pd

logging.basicConfig(filename = 'log.txt', format = '%(levelname)s:%(message)s'\
                    , level = logging.INFO)

def output_(df: pd.DataFrame,out_path: str = Path.cwd()):
    """
        Generate out output
    """
    logging.info("Starting the output generation".center(50,"*"))
    null_columns = [c for c in df.columns if df[c].isnull().any()]
    df_output_bad = df[null_columns]
    df_output_good = df[df.columns.difference(null_columns)]
    logging.info("Generating the files!")
    df_output_bad.to_csv(out_path + '/' + '.bad',index=False)
    df_output_good.to_csv(out_path + '/' + '.out',index=False)
    logging.info("Success")
    try:
        with open('bad_file.txt','w',encoding="UTF-8") as f_:
            for c in null_columns:
                f_.write(f"Column: {c} has some null values\n")
        f_.close()
    except Exception as ex:
        logging.error("Error to create the metadata file.\n %s", ex)
