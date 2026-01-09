import matplotlib.pyplot as plt
import seaborn as sns

def visualize_before_after(df_before, df_after, target_column=None):
    """
    STEP 11:
    Compare before and after cleaning.
    Shows:
    - Missing values
    - Duplicates
    - Target distribution (if provided)
    """

    if df_before is None or df_after is None:
        print("⚠️ Please provide both df_before and df_after for visualization")
        return

    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle("Dataset Cleaning: Before vs After", fontsize=16)

    # 1️⃣ Missing values
    sns.barplot(x=df_before.isna().sum().index, y=df_before.isna().sum().values, ax=axes[0,0])
    axes[0,0].set_title("Missing Values (Before)")
    axes[0,0].tick_params(axis='x', rotation=45)

    sns.barplot(x=df_after.isna().sum().index, y=df_after.isna().sum().values, ax=axes[0,1])
    axes[0,1].set_title("Missing Values (After)")
    axes[0,1].tick_params(axis='x', rotation=45)

    # 2️⃣ Duplicates
    axes[1,0].bar(["Duplicates"], [df_before.duplicated().sum()])
    axes[1,0].set_title("Duplicate Rows (Before)")

    axes[1,1].bar(["Duplicates"], [df_after.duplicated().sum()])
    axes[1,1].set_title("Duplicate Rows (After)")

    # 3️⃣ Target distribution (optional)
    if target_column is not None and target_column in df_before.columns:
        sns.countplot(x=df_before[target_column], ax=axes[2,0])
        axes[2,0].set_title("Target Distribution (Before)")

        sns.countplot(x=df_after[target_column], ax=axes[2,1])
        axes[2,1].set_title("Target Distribution (After)")
    else:
        axes[2,0].axis('off')
        axes[2,1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
