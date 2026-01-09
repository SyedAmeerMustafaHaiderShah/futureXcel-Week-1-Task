def remove_duplicates(df):
    """
    STEP 7:
    Remove duplicate rows.
    """

    df = df.copy()
    df = df.drop_duplicates()
    print('removing of duplicated done succesfully')

    return df
