import pandas as pd

import matplotlib
matplotlib.use("Agg") # Headless mode for saving files

import matplotlib.pyplot as plt

# Constants
FILE_NAME = "digital_behaviour.csv"
DAILY_LIMIT = 6.0

def load_data(filename):
    """
    Load data and convert Date column.
    """
    try:
        # TODO: Read the CSV file into a DataFrame
        df = pd.read_csv(filename)

        # TODO: Convert the 'Date' column to datetime objects
        df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')
        
        # TODO: Sort the DataFrame by 'Date' and return the sorted DataFrame
        return df.sort_values('Date')
        
    except FileNotFoundError:
        print("Error: File not found.")
        return pd.DataFrame()
    
