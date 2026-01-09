from sklearn.preprocessing import StandardScaler

def scale_numeric_columns(df, columns=None):
    """
    STEP 9:
    Scale numeric columns using StandardScaler.

    Parameters:
    - columns: list of numeric columns to scale
               If None → scale ALL numeric columns
    """

    df = df.copy()

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if columns is None:
        columns = numeric_cols
    else:
        # keep only numeric columns
        columns = [c for c in columns if c in numeric_cols]

    if not columns:
        print("⚠️ No numeric columns selected for scaling")
        return df

    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])

    return df
