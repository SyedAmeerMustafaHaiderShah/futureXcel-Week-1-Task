import pandas as pd
import os

def load_dataset(file_path):
    """
    STEP 1:
    Load dataset safely.
    Supports CSV, Excel.
    No modification is done here.
    """

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)
        print('loaded succesfully')
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

    return df


