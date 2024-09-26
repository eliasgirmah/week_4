import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_distribution(data):
    """Plot the distribution of sales."""
    plt.figure(figsize=(10,6))
    sns.histplot(data['Sales'], bins=30, kde=True)
    plt.title("Sales Distribution")
    plt.show()

if __name__ == "__main__":
    # Load the cleaned data
    cleaned_data = pd.read_csv("../data/processed/cleaned_data.csv")
    
    # Plot sales distribution
    plot_sales_distribution(cleaned_data)
