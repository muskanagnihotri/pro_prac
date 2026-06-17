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

# 4. Plot Histogram of Order Value
def plot_order_histogram(df):
    """
    Create and save a histogram of individual order values.
    Shows the distribution of order costs (Are most orders cheap or expensive?).
    """

    # TODO: Set figure size to 8 inches by 5 inches
    plt.figure(figsize=(8,5))
    
    # TODO: Create a histogram for the 'Total_Price' column
    plt.hist(
        df['Total_Price'],

        # TODO: Set the number of bins to 10
        bins=10,            

        # TODO: Set the Bar color
        color='skyblue',    

        # TODO: Set the Border color
        edgecolor='black',  

        # TODO: Set the Transparency value
        alpha=0.7           
    )
    
    # TODO: Add Title and Labels
    # Title: "How Much Do Customers Spend? (Order Value Distribution)"
    # X-label: "Total Bill Amount ($)"
    # Y-label: "Number of Orders"
    plt.title('How Much Do Customers Spend? (Order Value Distribution)')
    plt.xlabel('Total Bill Amount ($)')
    plt.ylabel('Number of Orders')

    # TODO: Add gridlines only to the y-axis with transparency of 0.5 for readability
    plt.grid(axis='y',alpha=0.5)
    
    # Save the plot
    output_file = "order_value_histogram.png"

    # TODO: Save the figure to output_file
    plt.savefig(output_file)

    print(f"Histogram saved to {output_file}")

if __name__ == "__main__":

    # Load data
    filename = 'grocery_orders.csv'
    df = load_grocery_data(filename)

    if not df.empty:
        print(f"Total Transactions: {len(df)}")

        # 1. Analysis: Category Spending
        category_totals = calculate_category_spending(df)
        print("\nSpending Breakdown by Category:")
        print(category_totals)

        # 2. Visualization: Pie Chart
        print("\nGenerating Pie Chart...")
        plot_category_pie(category_totals)

        # 3. Visualization: Histogram
        print("\nGenerating Histogram...")
        plot_order_histogram(df)



