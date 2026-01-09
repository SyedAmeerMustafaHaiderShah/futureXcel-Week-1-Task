def handle_outliers(df, factor=1.5):
    """
    STEP 8:
    Handle outliers using IQR.
    Applies ONLY to numeric columns.
    """

    df = df.copy()

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - factor * IQR
        upper = Q3 + factor * IQR

        df[col] = df[col].clip(lower, upper)
    print(' done succesfully ')    

    return df
