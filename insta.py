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
        df =pd.read_csv(filename)
        
        print(f"Data Loaded Successfully: {len(df)} posts.")
        print(f"Columns: {list(df.columns)}")
        
        # TODO: Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()

# 2. === Correlation Heatmap ===
def plot_engagement_correlation(df):
    """
    Visualize correlation between engagement metrics using a Heatmap.
    """
    # Numeric engagement columns
    engagement_cols = [
        "likes",
        "comments",
        "shares",
        "saves",
        "reach"
    ]
    
    # TODO: Calculate correlation matrix using .corr() on the selected columns
    corr_matrix = df['engagement_cols'].corr()

    # TODO: Set figure size to 10 inches by 8 inches
    plt.figure(figsize=(10,8))

    # TODO: Create a Heatmap
    # Arguments:
    # - Data for this heatmap is the correlation matrix
    # - Show numbers on the blocks (Explore the annot parameter)
    # - Set the color map to "coolwarm"
    # - Format numbers to 2 decimal places (Explore the fmt parameter)
    # - Set the line widths between cells to 0.5
    sns.heatmap(
        corr_matrix,
        annot=True, 
        cmap='coolwarm', 
        fmt='.2f',
        linewidths=0.5
    )

    # TODO: Set the title to "Instagram Engagement Correlation Heatmap"
    plt.title('Instagram Engagement Correlation Heatmap')
    
    # TODO: Adjust layout with tight_layout()
    plt.tight_layout()
    
    # TODO: Save the figure as "engagement_correlation_heatmap.png"
    plt.savefig('engagement_correlation_heatmap.png')
    
    print("Saved: engagement_correlation_heatmap.png")


# 3. === Hashtag Impact Trend (Regression Plot) ===
def plot_hashtag_vs_reach(df):
    """
    Analyze relationship between hashtags and reach using Regression.
    """
    # TODO: Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))

    # TODO: Create a Regression Plot (regplot)
    # Arguments:
    # - X axis: "hashtags_count"
    # - Y axis: "reach"
    # - data: df
    # - Make scatter points green (Explore the scatter_kws parameter)
    # - Make the Trend line red (Explore the line_kws parameter)
    sns.regplot(
        x='hashtags_count',
        y='reach', 
        data=df, 
        scatter_kws={'color':'green'},
        line_kws={'color':'red'}
    )

    # TODO: Set title to "Hashtag Count vs. Reach Trend"
    plt.title('Hashtag Count vs. Reach Trend')
    
    # TODO: Set x-axis label to "Number of Hashtags" and y-axis label to "Post Reach"
    plt.xlabel('Number of Hashtags')
    plt.ylabel('Post Reach')

    # TODO: Adjust layout using tight_layout() and save as "hashtag_reach_trend.png"
    plt.tight_layout()
    plt.savefig('hashtag_reach_trend.png')
    
    print("Saved: hashtag_reach_trend.png")

# 4. === Residual Analysis (Unexpected Viral Behavior) ===
def plot_residual_analysis(df):
    """
    Use a Residual Plot to see 'outlier' performance.
    Points far from 0 line = Posts performing much better/worse than expected.
    """
    # TODO: Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))

    # TODO: Create a Residual Plot (residplot)
    # Arguments:
    # - X axis: "hashtags_count"
    # - Y axis: "reach"
    # - data: df
    # - Make the points purple
    sns.residplot(
        x='hashtags_count',
        y='reach',
        data=df,
        scatter_kws={'color':'purple'}
    )

    # TODO: Add a reference line at 0 (y=0) (Expected Performance)
    # # Color: Black, Linestyle: Dashed ("--")
    plt.axhline(y=0,color='black',linestyle='--')

    # TODO: Set title to "Residual Analysis: Viral Outliers (Observed - Expected)"
    plt.title('Residual Analysis: Viral Outliers (Observed - Expected)')
    
    # TODO: Set x-axis label to "Number of Hashtags"
    plt.xlabel('Number of Hashtags')
    
    # TODO: Set y-axis label to "Residual Reach (Deviation)"
    plt.ylabel('Residual Reach (Deviation)')

    # TODO: Adjust layout using tight_layout() and save as "viral_residual_analysis.png"
    plt.tight_layout()
    plt.savefig('viral_residual_analysis.png')
    
    print("Saved: viral_residual_analysis.png")

if __name__ == "__main__":
    print("### Instagram Viral Trends Analytics ###")

    df = load_instagram_data(FILE_NAME)

    if not df.empty:
        # 1. Correlation Analysis (Heatmap)
        plot_engagement_correlation(df)

        # 2. Hashtag Trend Analysis (Regression)
        plot_hashtag_vs_reach(df)

        # 3. Residual Analysis (Residplot)
        plot_residual_analysis(df)

    else:
        print("Analysis stopped.")

        


