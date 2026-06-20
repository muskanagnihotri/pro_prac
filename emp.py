import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")   # Headless mode for saving files
import matplotlib.pyplot as plt


# 1. Load Employee Data
def load_employee_data(filename):
    """
    Load CSV dataset into a pandas DataFrame.
    """
    try:
        # TODO: Read the CSV file into a dataframe
        df = pd.read_csv(filename)

        print("Data loaded successfully.")

        # TODO: Return the dataframe
        return df

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Plot Department Headcounts
def plot_department_counts(df):
    """
    Create a countplot showing how many employees work in each department.
    """
    # TODO: Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))
    
    # TODO: Create a countplot
    # Arguments:
    # - Map the Department to the X-axis.
    # - Separate the counts by Gender (Explore the hue parameter)
    # - data: df
    # - Set the palette to "viridis"
    sns.countplot(
        x='Department', 
        hue='Gender', 
        data=df, 
        palette='viridis'
    )
    
    #TODO: Set the title to "Employee Count by Department"
    plt.title('Employee Count by Department')

    # TODO: Set x-axis label to "Department" and y-axis label to "Number of Employees"
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')

    # TODO: Set the legend title to "Gender"
    plt.legend(title='Gender')
    
    # TODO: Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "department_headcount.png"
    # TODO: Save the figure with bbox_inches='tight'
    plt.savefig(output,bbox_inches='tight')

    print(f"Saved: {output}")


# 3. Plot Salary Distribution
def plot_salary_box(df):
    """
    Compare salary ranges across departments using boxplots.
    """
    # TODO: Set figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))
    
    # TODO: Create a boxplot
    # Arguments:
    # - Map "Department" to the X-axis and "Salary" to the Y-axis.
    # - data: df
    # - Disable the legend
    sns.boxplot(
        x='Department', 
        y='Salary', 
        data=df, 
        legend=False
    )
    
    # TODO: Set the title to "Salary Distribution by Department & Experience"
    plt.title('Salary Distribution by Department & Experience')

    # TODO: Set x-axis label to "Department" and y-axis label to "Annual Salary ($)"
    plt.xlabel('Department')
    plt.ylabel('Annual Salary ($)')
    
    # TODO: Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "salary_boxplot.png"

    # TODO: Save the figure with bbox_inches='tight'
    plt.savefig(output,bbox_inches='tight')

    print(f"Saved: {output}")


# 4. Plot Employee Satisfaction
def plot_satisfaction_violin(df):
    """
    Show satisfaction score distribution using violin plots.
    """

    # TODO: Set the figure size to 10 inches by 6 inches
    plt.figure(figsize=(10,6))
    
    # TODO: Create a violinplot
    # Arguments:
    # - x: "Department"
    # - y: "Satisfaction"
    # - hue: "Gender"
    # - data: df
    # - split: ... (Set to True to merge Male/Female violins)
    # - inner: ... (Show quartiles inside the violins)
    # - Set the palette to "muted"
    sns.violinplot(
        x='Department',
        y='Satisfaction',
        hue='Gender',
        data=df,
        split=True,      
        inner='quartile', 
        palette='muted'
    )
    
    # TODO: Set the title to "Employee Satisfaction Density (Male vs Female)"
    plt.title('Employee Satisfaction Density (Male vs Female)')

    # TODO: Set x-axis label to "Department" and y-axis label to "Satisfaction Score (0-10)"
    plt.xlabel('Department')
    plt.ylabel('Satisfaction Score (0-10)')

    # TODO: Set the legend title to "Gender"
    plt.legend(title='Gender')
    
    # TODO: Rotate x-axis labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "satisfaction_violin.png"

    # TODO: Save the figure with bbox_inches='tight'
    plt.savefig(output,bbox_inches='tight')

    print(f"Saved: {output}")


if __name__ == "__main__":
    file = "employees.csv"
    df = load_employee_data(file)

    if not df.empty:
        print(f"Total Employees: {len(df)}")

        # Who works here?
        print("\nGenerating Department Count Chart...")
        plot_department_counts(df)

        # How much do they make?
        print("\nGenerating Salary Box Plot...")
        plot_salary_box(df)

        # Are they happy?
        print("\nGenerating Satisfaction Violin Plot...")
        plot_satisfaction_violin(df)


