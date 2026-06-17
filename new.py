# new pro Project 3: Online Grocery Spending Insights Project! 
import pandas as pd

import matplotlib
matplotlib.use("Agg")  # Headless mode for saving files

import matplotlib.pyplot as plt


# 1. Load Grocery Order Data
def load_grocery_data(filename):
    """
    Load CSV order data into a pandas DataFrame.
    """
    try:
        # TODO: Read the CSV file into a DataFrame
        df = pd.read_csv(filename)
        print("Data loaded successfully.")

        # TODO: Return the DataFrame
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
