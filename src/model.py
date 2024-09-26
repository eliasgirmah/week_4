from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

def train_model(data):
    """Train a RandomForest model."""
    X = data[['Store', 'Promo', 'Year', 'Month', 'DayOfWeek']]  # Features
    y = data['Sales']  # Target
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model

if __name__ == "__main__":
    # Load data with features
    data = pd.read_csv("../data/processed/data_with_features.csv")
    
    # Train model
    model = train_model(data)
    
    # Save model
    joblib.dump(model, "../models/sales_model.pkl")
