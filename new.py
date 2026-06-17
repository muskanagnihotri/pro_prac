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

# 2. Calculate Category Spending Totals
def calculate_category_spending(df):
    """
    Sum total spending for each item category.
    """
    # TODO: Group by 'Category' and sum the 'Total_Price' column
    category_totals = df.groupby('Category')['Total_Price'].sum()

    # TODO: Return the resulting Series
    return category_totals

# 3. Plot Pie Chart for Category Spending Share
def plot_category_pie(category_totals):
    """
    Create and save a pie chart of category spending distribution.
    Shows which category (e.g., Dairy, Fruits) consumes the most budget.
    """

    # TODO: Set figure size to 7 inches by 7 inches
    plt.figure(figsize=(7,7))
    
    # TODO: Create a pie chart
    plt.pie(
        # TODO: Use the values from category_totals
        category_totals.values,

        # TODO: Use the index (category names) as labels
        labels=category_totals.index,

        # TODO: Show percentage upto 1 decimal place
        autopct='%1.1f%%',  

        # TODO: Slightly separate (0.05) all the slices using explode
        explode=[0.05]*len(category_totals)
    )

    # TODO: Set the plot title to "Grocery Spending by Category"
    plt.title('Grocery Spending by Category')
    
    # Save the plot
    output_file = "category_spending_pie_chart.png"
    
    # TODO: Save the figure to output_file with tight layout (bbox_inches='tight')
    plt.savefig(output_file,bbox_inches='tight')
    
    print(f"Pie chart saved to {output_file}")

