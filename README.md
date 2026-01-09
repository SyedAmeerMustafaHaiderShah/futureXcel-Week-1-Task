# futureXcel-Week-1-Task
🧹 AutoCleanML: Generic Data Cleaning & Preprocessing Pipeline

AutoCleanML is a reusable, modular preprocessing pipeline designed to take raw user datasets (CSV / Excel / etc.) and convert them into a clean, ML-ready dataset — without forcing unnecessary steps.

The pipeline is function-based, allowing users to apply only the preprocessing steps they actually need, making it suitable for different datasets and use cases.

🚀 What Problem It Solves

Real-world datasets often contain:

Missing values

Inconsistent column names

Mixed data types

Duplicate rows

Outliers

Categorical text that ML models cannot understand

Optional class imbalance in target variables

AutoCleanML provides a step-by-step, reproducible solution to handle these issues systematically.

🧠 Core Design Philosophy

✅ Generic → Works with any dataset

✅ Modular → Each preprocessing task is a separate function

✅ Optional → User chooses which steps to apply

✅ Safe → Text columns are not destroyed unnecessarily

✅ Reproducible → Same input → same output

No “black-box magic”. Everything is explicit and controlled.

🔁 Pipeline Flow (Visual Overview)
Load Dataset
   ↓
Initial Checks
   ↓
Clean Column Names
   ↓
Fix Data Types
   ↓
Handle Missing Values
   ↓
Clean Text Columns (optional)
   ↓
Remove Duplicates
   ↓
Handle Outliers (optional)
   ↓
Scale Numeric Features (optional)
   ↓
Encode Categorical Features (optional)
   ↓
Handle Target Imbalance (optional)
   ↓
Visualize Before vs After
   ↓
Save Cleaned Dataset


Each step is implemented as an independent function.

🛠️ Key Features
🧹 Data Cleaning

Missing value handling (mean / median / mode / drop)

Column name standardization

Automatic data type correction

Duplicate row removal

Text normalization (lowercasing, trimming, noise removal)

🔢 Feature Preparation

Scaling → Numeric columns only

Encoding → Categorical columns only

Low-cardinality → One-hot encoding

High-cardinality → Label encoding

⚠️ Encoding is never forced. The user decides when to apply it.

⚖️ Imbalanced Dataset Handling (Optional)

Oversampling

Undersampling

Synthetic data generation (SMOTE)

Requires the target column name from the user.

📊 Built-in Visualization

The pipeline can generate before vs after graphs using Seaborn:

Missing values comparison

Duplicate rows comparison

Target class distribution (if provided)

This helps users verify cleaning effects visually.

📦 Supported Input Formats

.csv

.xlsx

.xls

All formats are internally converted to CSV for consistency and speed.

▶️ Example Usage
df = load_dataset("data.xlsx")
df = clean_column_names(df)
df = handle_missing_values(df)
df = remove_duplicates(df)

# Optional steps
df = scale_numeric_columns(df)
df = encode_categorical_columns(df)

save_dataset(df)


Or use the main pipeline function to orchestrate steps in order.

📁 Output

Cleaned dataset saved as CSV

Ready for:

Machine Learning

Data Analysis

Feature Engineering

Model Training Pipelines

🧩 Why This Is a Pipeline (Academically & Practically)

✔ Reproducible
✔ Modular
✔ Automated
✔ Documented
✔ Reusable

This meets standard ML pipeline definitions used in:

University assignments

Industry preprocessing workflows

Scikit-learn–style pipelines (conceptually)

🧠 Important Note

This pipeline focuses on data preprocessing, not model training.
Model-specific decisions (class weights, metrics, algorithms) are intentionally left to the user.

🤝 Future Extensions (Optional)

Sklearn Pipeline integration

Config-based execution (YAML/JSON)

Logging instead of print statements

Feature selection utilities
