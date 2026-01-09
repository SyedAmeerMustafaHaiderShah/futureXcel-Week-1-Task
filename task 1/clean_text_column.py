import pandas as pd
import re

def clean_text_columns(df):
    """
    STEP 6: Clean text columns safely.
    - Lowercase text
    - Strip leading/trailing spaces
    - Remove extra spaces
    - DOES NOT encode or convert to numbers
    """

    df = df.copy()

    text_cols = df.select_dtypes(include="object").columns

    for col in text_cols:
        df[col] = (
            df[col]
            .astype(str)
            .str.lower()
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )
    print('"this step done successfully')  

    return df
