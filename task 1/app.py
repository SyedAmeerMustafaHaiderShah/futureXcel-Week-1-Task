from load import load_dataset
from initial_checkup import initial_checks
from clean_colum_name import clean_column_names
from  handling_missing_value  import handle_missing_values
from clean_text_column import clean_text_columns
from removeduplicates import remove_duplicates
from handleoutliner import handle_outliers
from visualization import visualize_before_after
from saving_datset import save_dataset
# this will load you dataset  possible accepted
# format are  xls and csv
df=load_dataset('flood.csv')
# this will give you the repor tof the dataset
# report = initial_checks(df)
# print(report)
df = clean_column_names(df)
# report = initial_checks(df)
# print(report)
df = handle_missing_values(df)
df = clean_text_columns(df)
df = remove_duplicates(df)
df = handle_outliers(df)
df_before = df.copy()
# df = scale_numeric_columns(
#     df,
#     columns=["Max_Temp", "Min_Temp", "Rainfall"]
# )

# df = encode_categorical_columns(df, columns=["station_names", "flood"])

# Apply some cleaning steps
df_after = handle_missing_values(df_before)
df_after = clean_text_columns(df_after)
df_after = remove_duplicates(df_after)


# Visualize
visualize_before_after(df_before, df_after, target_column="flood")






