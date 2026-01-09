import os

def save_dataset(df, file_path="cleaned_dataset.csv", overwrite=True):
    """
    STEP 12:
    Save cleaned dataset to CSV.
    
    Parameters:
    - df: DataFrame to save
    - file_path: target CSV file path
    - overwrite: if False, will append a number to filename
    """

    path = file_path

    if not overwrite:
        base, ext = os.path.splitext(file_path)
        i = 1
        while os.path.exists(path):
            path = f"{base}_{i}{ext}"
            i += 1

    df.to_csv(path, index=False)
    print(f"✅ Dataset saved to: {path}")
