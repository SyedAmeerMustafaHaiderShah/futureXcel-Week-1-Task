def clean_column_names(df):
    """
    STEP 3:
    Normalize column names only.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w]", "", regex=True)
    )
    print('datatype fixed successfully ')

    return df
