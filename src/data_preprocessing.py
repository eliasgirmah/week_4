import sys
import os

# Add the src folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
#from src.utils import setup_logger

from src.utils.utils import setup_logger  # Adjusted import statement


# Set up logger
logger = setup_logger("data_preprocessing", "../logs/data_preprocessing.log")

def load_data(file_path):
    """Function to load raw data."""
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded from {file_path}. Shape: {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None

def clean_data(data):
    """Function to clean and preprocess data."""
    # Example: handling missing values
    try:
        data.fillna(0, inplace=True)
        logger.info("Missing values filled with 0.")
        return data
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
        return None

if __name__ == "__main__":
    # Load and clean data
    raw_data_path = "../data/raw/train.csv"
    data = load_data(raw_data_path)
    
    if data is not None:
        cleaned_data = clean_data(data)
        # Save the cleaned data
        cleaned_data.to_csv("../data/processed/cleaned_data.csv", index=False)
        logger.info("Cleaned data saved.")
