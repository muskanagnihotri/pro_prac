import pandas as pd

# 1. Load Virat Match Data
def load_data(filename):
    """
    Load Virat Kohli match-wise performance data and parse dates.
    """
    try:
        # TODO: Load the CSV file using Pandas
        df = pd.read_csv(filename)

        # TODO: Convert 'match_date' column to datetime objects
        # Use this format="%Y-%m-%d"
        df['match_date']=pd.to_datetime(df['match_date'],format='%Y-%m-%d')
        
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
    except Exception:
        print(f"Error loading data.")
        return pd.DataFrame()