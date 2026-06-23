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
    
def visualize_digital_behavior(df):
    """
    Create a side-by-side plot layout.
    """

    # 1. Setup Subplots in 1 Row and 2 Columns
    # TODO: Create a subplot with 1 row and 2 columns
    # Set the figure size to 15 inches by 5 inches
    fig, axes = plt.subplots(1, 2, figsize=(15,5))

    # Assigning axes to variables for easier use
    ax1 = axes[0] # Axis for Plot 1
    ax2 = axes[1] # Axis for Plot 2

    # TODO: Add a main title for the entire figure
    # Main Title: "Project 3: Digital Behaviour Analysis"
    fig.suptitle("Project 3: Digital Behaviour Analysis")

    # === PLOT 1: Daily Trends (Line Plot) ===
    # TODO: Plot 'Date' on X-axis and 'ScreenTime' on Y-axis
    # Add label 'Screen Time'
    ax1.plot(df['Date'],df['ScreenTime'],label='Screen Time')

    # Now plot another line for 'AppUsage' 
    # TODO: Plot 'Date' on X-axis and 'AppUsage' on Y-axis
    # Make this line dashed and add label 'App Usage'
    ax1.plot(df['Date'],df['AppUsage'],linestyle='--',label='App Usage')

    # TODO: Add a horizontal line for the daily limit
    # Use y=DAILY_LIMIT, color='red' and make this line dashed
    # Label it 'Daily Limit'
    ax1.axhline(df['DAILY_LIMIT'],color='red',linestyle='--',label='Daily Limit')
    # Labels
    # TODO: Add a title to ax1 "Daily Usage Trends"
    ax1.set_title('Daily Usage Trends')

    # TODO: Add X axis label 'Date' and Y axis label 'Hours'
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Hours')

    # TODO: Add a legend to axis ax1
    ax1.legend()
    
    # TODO: Rotate date labels by 45 degrees for better readability
    ax1.tick_params(axis='x',rotation=45)
