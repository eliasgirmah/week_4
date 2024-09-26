import joblib
import pandas as pd

def predict_sales(model, data):
    """Generate sales predictions."""
    X = data[['Store', 'Promo', 'Year', 'Month', 'DayOfWeek']]
    predictions = model.predict(X)
    return predictions

if __name__ == "__main__":
    # Load model
    model = joblib.load("../models/sales_model.pkl")
    
    # Load data
    data = pd.read_csv("../data/processed/data_with_features.csv")
    
    # Generate predictions
    predictions = predict_sales(model, data)
    print(predictions)
