import pandas as pd

FILE_NAME = "flights.csv"

# 1. Data Loading and Data Parsing
def load_flight_data(filename):
    """
    Load flight dataset and parse dates from 'FlightDate'.
    """
    try:
        # TODO: Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(filename)

        # Validation: Check if required column exists
        if "FlightDate" not in df.columns:
            print("Error: 'FlightDate' column is missing in the CSV.")
            return pd.DataFrame()

        # TODO: Parse the "FlightDate" column into datetime format
        # Make sure to specify the correct date format (YYYY-MM-DD)
        df["FlightDate"] = pd.to_datetime(df['FlightDate'],format='%Y-%m-%d')
        
        return df
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()


# 2. Data Cleaning
def clean_delay_data(df):
    """
    Assumption: If delay is NaN (empty), it means the flight was On Time (0 delay).
    """

    # TODO: Fill missing values (NaN) in the 'DepartureDelay' column with 0
    if "DepartureDelay" in df.columns:
        df["DepartureDelay"] = df["DepartureDelay"].fillna(0)
    
    return df

# 3. Feature Extraction
def extract_day_features(df):
    """
    Extract the 'Day Name' (Monday, Tuesday...) from the Date column.
    """

    # TODO: Get the name of the day (e.g., "Monday") from the "FlightDate" column
    # Hint: Use Pandas date accessors to find the day name
    df["Day_Name"] =df['FlightDate'].dt.day_name()
    
    return df
