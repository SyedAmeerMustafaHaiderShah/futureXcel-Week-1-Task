def initial_checks(df):
    """
    STEP 2:
    Basic inspection only.
    No data modification.
    """

    info = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum(),
        "duplicate_rows": df.duplicated().sum(),
        "dtypes": df.dtypes
    }

    return info
