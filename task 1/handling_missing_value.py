def handle_missing_values(df):
    """
    STEP 5:
    Handle missing values safely.
    """

    df = df.copy()

    for col in df.columns:
        if df[col].isnull().sum() == 0:
            continue

        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    print("done succesfully")
    return df
