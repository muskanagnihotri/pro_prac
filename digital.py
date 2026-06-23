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


    # === PLOT 2: Correlations (Scatter with Color Map) ===
    # TODO: Create a scatter plot on axis ax2
    # x = 'Unlocks', y = 'ScreenTime'
    # This maps color to App Usage
    # Set colormap to 'viridis'
    # Set transparency to 0.7 (Explore alpha parameter)
    scatter = ax2.scatter(
        df['Unlocks'],
        df['ScreenTime'], 
        c=df['AppUsage'], 
        cmap='viridis',
        alpha=0.7
    )

    # Labels
    # TODO: Add title to ax2 "Unlocks vs. Screen Time"
    ax2.set_title('Unlocks vs. Screen Time')

    # TODO: Add X axis label 'Unlocks' and Y axis label 'Screen Time'
    ax2.set_xlabel('Unlocks')
    ax2.set_ylabel('Screen Time')

    # TODO: Add a Colorbar to explain the colors
    # Pass the 'scatter' object and the axis 'ax2'
    # Set the label to 'App Usage (Hours)'
    fig.colorbar(scatter,ax=ax2,label='App Usage (Hours)')

    # TODO: Adjust layout using tight_layout function and save the figure as a PNG file (digital_behaviour_analysis.png)
    plt.tight_layout()
    plt.savefig('digital_behaviour_analysis.png')

    print("Plot saved as 'digital_behaviour_analysis.png'")

if __name__ == "__main__":
    df = load_data(FILE_NAME)
    
    if not df.empty:
        visualize_digital_behavior(df)


