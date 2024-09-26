import pandas as pd

def create_features(data):
    """Create new features for the model."""
    data['Year'] = pd.to_datetime(data['Date']).dt.year
    data['Month'] = pd.to_datetime(data['Date']).dt.month
    data['DayOfWeek'] = pd.to_datetime(data['Date']).dt.dayofweek
    # More feature engineering here...
    
    return data

if __name__ == "__main__":
    # Load cleaned data
    cleaned_data = pd.read_csv("../data/processed/cleaned_data.csv")
    
    # Create features
    data_with_features = create_features(cleaned_data)
    
    # Save the feature data
    data_with_features.to_csv("../data/processed/data_with_features.csv", index=False)
