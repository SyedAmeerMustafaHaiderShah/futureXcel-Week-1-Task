import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_categorical_columns(df, columns=None, low_card_threshold=50):
    """
    STEP 10:
    Encode categorical/text columns.
    
    Parameters:
    - df: pandas DataFrame
    - columns: list of columns to encode (default=None → all object columns)
    - low_card_threshold: max unique values for one-hot encoding
    """

    df = df.copy()

    # select object columns if user didn't provide
    if columns is None:
        columns = df.select_dtypes(include="object").columns.tolist()
    else:
        # keep only existing object columns
        columns = [c for c in columns if c in df.columns and df[c].dtype == "object"]

    if not columns:
        print("⚠️ No categorical/text columns selected for encoding")
        return df

    for col in columns:
        n_unique = df[col].nunique()

        if n_unique <= low_card_threshold:
            # One-hot encoding
            dummies = pd.get_dummies(df[col], prefix=col, drop_first=True)
            df = pd.concat([df.drop(col, axis=1), dummies], axis=1)
        else:
            # Label encoding
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])

    return df
