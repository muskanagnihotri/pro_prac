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
    
# 2. Load Opponent Mapping Data
def load_opponent_data(filename):
    try:
        # TODO: Load the CSV file using Pandas
        df = pd.read_csv(filename)

        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()
    
# 3. Merge Match + Opponent Data
def merge_match_opponent(match_df, opponent_df):
    """
    Merge match data with opponent full names.
    """

    if "opponent" not in match_df.columns or "opponent" not in opponent_df.columns:
        print("Error: 'opponent' column missing in one of the datasets.")
        return match_df

    # TODO: Merge the two dataframes on the "opponent" column using a left join
    merged_df = pd.merge(merged_df,opponent_df,on='opponent',how='left')
    
    return merged_df