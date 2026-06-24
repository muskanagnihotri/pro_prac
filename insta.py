import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

# Constants
FILE_NAME = "instagram_dataset.csv"
# Set a clean visual theme
sns.set_theme(style="whitegrid")


# 1. === Loading Instagram Data ===
def load_instagram_data(filename):
    """
    Loading Instagram post dataset.
    """
    try:
        # TODO: Read the CSV file into a dataframe
        df =pd.read_csv('filename')
        
        print(f"Data Loaded Successfully: {len(df)} posts.")
        print(f"Columns: {list(df.columns)}")
        
        # TODO: Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()